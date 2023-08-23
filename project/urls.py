from django.contrib import admin
from django.urls import path, include
from shop.views import (CategoryViewSet, ProductViewSet, ArticleViewSet,
                        AdminCategoryViewSet, AdminArticleViewSet)
from rest_framework import routers

router = routers.SimpleRouter()  # création du routeur

router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('article', ArticleViewSet, basename='article')
router.register('admin/category', AdminCategoryViewSet, basename='admin-category')
router.register('admin/article', AdminArticleViewSet, basename='admin-article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

]
