from django.urls import path
from . import views

app_name = 'house'

urlpatterns = [
  path('regist_house', views.regist_house, name='regist_house'),
  path('list_house', views.list_house, name='list_house'),
  path('edit_house/<int:id>', views.edit_house, name='edit_house'),
  path('delete_house/<int:id>', views.delete_house, name='delete_house'),
  path('post_house_comments/<int:house_id>', views.post_house_comments, name='post_house_comments'), 
  path('detail_house', views.detail_house, name='detail_house'), 
]