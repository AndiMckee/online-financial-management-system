from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.salary, name='salary'),
    url(r'details/(?P<salary_id>\d+)/$', views.details, name='salary_details'),
    url(r'^(?P<company_uuid>.+)/(?P<page_num>\d+)/$', views.salary, name='salary_with_params'),
    url(r'delete/$', views.delete, name='delete_salary'),
    url(r'create/$', views.create, name='create_salary'),
]
