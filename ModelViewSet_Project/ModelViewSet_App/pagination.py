
from rest_framework import pagination

class UserPagination(pagination.PageNumberPagination):
    page_size = 3

    page_size_query_param = 'number'

    page_query_param = 'mypage'

    last_page_strings = ('endpage',)

    max_page_size = 4

