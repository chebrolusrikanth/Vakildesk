from django.urls import path
from . import views

urlpatterns=[
path('',views.top_customers_view)
]