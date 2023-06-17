from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'category', views.CategoryViewSet)
urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace="rest_framework"))
]

# urlpatterns = [
# 	path("", POSApp.as_view(), name="pos-app"),
# 	path("category", CategoryView.as_view(), name="category-change")
# ]