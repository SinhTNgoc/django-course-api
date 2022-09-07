from rest_framework.pagination import PageNumberPagination

class BasePaginate(PageNumberPagination):
     page_size = 20
     