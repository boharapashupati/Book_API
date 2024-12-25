from .models import Book
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# Serializers define the API representation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title', 'author', 'publication_date']


# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter , OrderingFilter,DjangoFilterBackend ]
    search_fields = ['title', 'author']
    Ordering_fields = ['id']
    filterset_fields = {'author' :['exact', 'icontains']}


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'book', BookViewSet) # type: ignore

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]