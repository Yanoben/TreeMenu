from django.urls import path
from .views import IndexView
# from menus.views import menu_item

app_name = 'Tree'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', IndexView.as_view(), name='index'),
]