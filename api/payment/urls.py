from django.urls import path, include
from . import views

urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.generate_token, name="token.generate"),
    path('proccess/<str:id>/<str:token>/', views.proccess_payment, name="payment.proccess"),    
]
