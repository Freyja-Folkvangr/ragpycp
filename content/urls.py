from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('get-feed/', views.get_feed, name='get_feed'),
    path('new-entry/', views.new_entry, name='new_entry'),
    path('<int:post_id>/', views.view_responses, name='view_responses'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
    # path('<int:char_id>/reset_appearance/', views.char_reset_appearence, name='char_reset_appearence'),
    # path('<int:char_id>/reset_map/', views.char_reset_map, name='char_reset_map'),
    # path('<int:char_id>/reset_position/', views.char_reset_position, name='char_reset_position'),
]
