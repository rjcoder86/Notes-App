from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.readall,name='readall'),
    path('createnote/',views.create,name='create'),
    path('deletenote/<int:pk>/',views.deletenote,name='deletenote'),
    path('updatenote/<int:id>/',views.updatenote,name='updatenote'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)