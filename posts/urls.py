from django.urls import path
from posts import views
urlpatterns=[
    path('', views.index, name="index"),
    path('detail/<int:id>', views.detail_view, name="detail"),
]