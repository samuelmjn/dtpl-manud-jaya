from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('<str:review_token>/', views.review_form, name='review_form'),
]