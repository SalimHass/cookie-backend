from django.urls import path
from cookies.api.viewsets import (
                            CookieDetailView,
                            CookieListView
                        )
urlpatterns=[
    path('cookie-stand-list',CookieListView.as_view(), name='books_list'),
    path('book-detail/<int:pk>',CookieDetailView.as_view(), name='detail')
]