from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('dresses/', views.dressess_index, name='index'),
path('accessories/', views.all_accessories, name='accessories'),
path('dresses/<int:dress_id>/', views.dresses_detail, name='detail'),
path('dresses/<int:dress_id>/accessories/new', views.list_accessories, name='list_accessories'),
path('dresses/<int:dress_id>/accessories/<int:accessory_id>/add', views.add_accessory, name='add_accessory'),
path('accounts/signup/', views.signup, name='signup'),
# path('dresses/<int:dress_id>/reviews/new',views.add_review, name='add_review'),
path('dresses/create/', views.DressCreate.as_view(), name='dresses_create'), 
path('dresses/<int:pk>/update/', views.DressUpdate.as_view(), name='dresses_update'),                   
path('dresses/<int:pk>/delete/', views.DressDelete.as_view(), name='dresses_delete'),
]

urlpatterns += staticfiles_urlpatterns()