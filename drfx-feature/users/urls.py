from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.UserListView.as_view()),
    path('index/', views.index, name='index'),
]