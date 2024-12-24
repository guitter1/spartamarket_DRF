from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from .models import Product

class ProductPagination(PageNumberPagination):
    page_size = 10  
    max_page_size = 100  

class ProductLISTAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        paginator = ProductPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    
    def author_check(self, product, user):
        if product.author != user:
            raise PermissionDenied("작성자만 수정/삭제 가능")
    
    def get(self, request, pk):
        product=self.get_object(pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product=self.get_object(pk)
        self.author_check(product, request.user)
        serializer=ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        product=self.get_object(pk)
        self.author_check(product, request.user)       
        product.delete()
        data={"pk":f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)