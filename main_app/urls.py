from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('watches/', views.watches_index, name='watches_index'),
  path('watches/<int:watch_id>/', views.watches_detail, name='watches_detail'),
  path('watches/create/', views.WatchCreate.as_view(), name='watches_create'),
  path('watches/<int:pk>/update/', views.WatchUpdate.as_view(), name='watches_update'),
  path('watches/<int:pk>/delete/', views.WatchDelete.as_view(), name='watches_delete'),
  path('accounts/signup/', views.signup, name='signup')
]