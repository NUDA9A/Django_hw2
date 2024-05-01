from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import ProductDetailView, ProductListView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView

app_name = MainConfig.name

urlpatterns = [
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name="delete_product"),
    path('', ProductListView.as_view(), name='catalog'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('blog/<slug:blog_slug>', BlogDetailView.as_view(), name='blog_w_slug'),
    path('category/', CategoryListView.as_view(), name='category_list')
]
