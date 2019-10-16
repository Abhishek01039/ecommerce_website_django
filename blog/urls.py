
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="HomeBlog"),
    path('blogspot/<int:id>',views.blog,name='blogspot')

]
