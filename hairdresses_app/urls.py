from django.urls import path, re_path
from . import views


urlpatterns = [
    path('clients/', views.list_of_clients, name='list-of-clients'),
    path('hairstyles/', views.list_of_hairstyles, name='list-of-hairstyles'),
    path('additional_services/', views.list_of_additional_services, name='list-of-additional-services'),
    path('bills/', views.list_of_bills, name='list-of-bills'),
    re_path(r'^clients/(?P<pk>[0-9]+)/$', views.ClientView.as_view(), name='client-detailed'),
    re_path(r'^clients/(?P<pk>[0-9]+)/edit/$', views.ClientUpdateView.as_view(), name='client-edit'),
    re_path(r'hairstyles/(?P<pk>[0-9]+)/$', views.HairdoView.as_view(), name='hairdo-detailed'),
    re_path(r'hairstyles/(?P<pk>[0-9]+)/edit/$', views.HairdoUpdateView.as_view(), name='hairdo-edit'),
    re_path(r'^additional_services/(?P<pk>[0-9]+)/$',
            views.AdditionalServiceView.as_view(), name='additional-service-detailed'),
    re_path(r'^additional_services/(?P<pk>[0-9]+)/edit/$',
            views.AdditionalServiceUpdateView.as_view(), name='additional-service-edit'),
    re_path(r'bills/(?P<pk>[0-9]+)/$', views.BillView.as_view(), name='bill-detailed'),
    re_path(r'bills/(?P<pk>[0-9]+)/edit/$', views.BillUpdateView.as_view(), name='bill-edit'),

]
