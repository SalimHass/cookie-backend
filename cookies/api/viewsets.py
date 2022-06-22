from http.cookiejar import Cookie
from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )


from cookies.models import CookieStand
from .serializers import CookieSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated



class CookieListView(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated )
   


class CookieDetailView(RetrieveUpdateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated )
    