from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_graph, name='show_graph'),
    url(r'^show_new_graph/$', views.show_new_graph, name='show_new_graph'),
    url(r'^store_data/$', views.store_data, name='store_data'),
    url(r'^get_cbp_data/$', views.get_cbp_data, name='get_cbp_data'),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^set_data/$', views.set_data, name='set_data'),
]
