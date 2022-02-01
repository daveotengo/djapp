
from django.urls import path
from pages.views import home_view,contact_view,about_view,social_view
from products.views import product_detail_view,product_create_view,product_delete_view,product_list_view,product_update_view

app_name = 'products'
urlpatterns = [

    path('<int:id>/', product_detail_view,name='product-detail'),
    path('create/', product_create_view,name='product-create'), #rendering with initial data
    path('<int:id>/update/', product_update_view,name='product-update'), #rendering with initial data
    path('<int:my_id>/delete/', product_delete_view,name='product-delete'),
    path('', product_list_view,name='product-list'),

]
