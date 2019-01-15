from rest_framework.pagination import PageNumberPagination


class PageLimitPagination(PageNumberPagination):
    """
    分页器
    """
    page_query_param = 'page'
    page_query_description = '页数'
    page_size_query_param = 'limit'
    page_size_query_description = '每页显示条数'
