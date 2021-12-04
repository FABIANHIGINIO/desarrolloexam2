from django.conf.urls import url

from . import views


urlpatterns = [

]
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^comentar/$', views.ComentarView.as_view(), name='comentar'),
    
]