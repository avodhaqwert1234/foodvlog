from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    # path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='detail'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='detaills'),
    path('search',views.searching,name='search'),
]