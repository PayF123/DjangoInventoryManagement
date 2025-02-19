from django.urls import  path
from . import views


urlpatterns=[
    path('dashboard/',views.index,name='dashboard-index'),
    path('dashboard/customer_department/', views.customer_page, name='dashboard-customer-department'),
    path('customers/',views.customers,name='dashboard-customers'),
    path('customers/detail/<int:pk>/', views.customer_detail,name='dashboard-customer-detail'),
    path('order/',views.order,name='dashboard-order'),
    path('add_assembly/<int:pk>/',views.add_assembly,name='dashboard-product-add-assembly'),
    path('view_assembly/<int:pk>/',views.view_assembly,name='dashboard-product-view-assembly'),
    path('add_component/<int:pk>/',views.add_component,name='dashboard-product-assembly-add-component'),
    path('view_component/<int:pk>/',views.view_component,name='dashboard-product-assembly-view-component'),
    path('product/',views.product,name='dashboard-product'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
    path('warehouse/',views.warehouse,name='dashboard-warehouse'),
]