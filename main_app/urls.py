from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('dresses/', views.dressess_index, name='index'),
path('dresses/<int:dress_id>/', views.dresses_detail, name='detail'),
path('dresses/<int:dress_id>/accessories/new', views.create_accessory, name='new_accessory'),
]

urlpatterns += staticfiles_urlpatterns()