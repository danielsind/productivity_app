from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers
from .views import ListViewSet, ListItemViewSet


# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'', ListViewSet)
# router.register(r'listitem', ListItemViewSet)
lists_router = routers.NestedSimpleRouter(router, r'', lookup = 'lists')
lists_router.register(r'list-item', ListItemViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(lists_router.urls))
]