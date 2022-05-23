from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.readall,name='readall'),
    path('createnote/',views.create,name='create'),
    path('deletenote/<int:pk>/',views.deletenote,name='deletenote'),
    path('updatenote/<int:id>/',views.updatenote,name='updatenote'),
]
