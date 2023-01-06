from django.urls import path
from . import views




urlpatterns = [
    path('all_book',views.get_page),
    path('detail/<str:book_id>',views.detail),
    path('change_status',views.change_status)
]