from django.contrib import admin
from django.urls import path, include

from . import views, models

urlpatterns = [
    path('api/ActualTotalLoad/<str:name_of_area>/<str:resol>/date/<int:y>-<int:m>-<int:d>', views.query1a, name='query1a'),
    path('api/ActualTotalLoad/<str:name_of_area>/<str:resol>/month/<int:y>-<int:m>', views.query1b, name='query1b'),
    path('api/ActualTotalLoad/<str:name_of_area>/<str:resol>/year/<int:y>', views.query1c, name='query1c'),
    path('api/AggregatedGenerationPerType/<str:name_of_area>/AllTypes/<str:resol>/date/<int:y>-<int:m>-<int:d>', views.query2a2, name='query2a2'),
    path('api/AggregatedGenerationPerType/<str:name_of_area>/AllTypes/<str:resol>/month/<int:y>-<int:m>', views.query2b2, name='query2b2'),
    path('api/AggregatedGenerationPerType/<str:name_of_area>/AllTypes/<str:resol>/year/<int:y>', views.query2c2, name='query2c2'),
    path('api/AggregatedGenerationPerType/<str:name_of_area>/<str:prod_type>/<str:resol>/date/<int:y>-<int:m>-<int:d>', views.query2a1, name='query2a1'),
    path('api/AggregatedGenerationPerType/<str:name_of_area>/<str:prod_type>/<str:resol>/month/<int:y>-<int:m>', views.query2b1, name='query2b1'),
    path('api/AggregatedGenerationPerType/<str:name_of_area>/<str:prod_type>/<str:resol>/year/<int:y>', views.query2c1, name='query2c1'),
    path('api/DayAheadTotalLoadForecast/<str:name_of_area>/<str:resol>/date/<int:y>-<int:m>-<int:d>', views.query3a, name='query3a'),
    path('api/DayAheadTotalLoadForecast/<str:name_of_area>/<str:resol>/month/<int:y>-<int:m>', views.query3b, name='query3b'),
    path('api/DayAheadTotalLoadForecast/<str:name_of_area>/<str:resol>/year/<int:y>', views.query3c, name='query3c'),
    path('api/ActualvsForecast/<str:name_of_area>/<str:resol>/date/<int:y>-<int:m>-<int:d>', views.query4a, name='query4a'),
    path('api/ActualvsForecast/<str:name_of_area>/<str:resol>/month/<int:y>-<int:m>', views.query4b, name='query4b'),
    path('api/ActualvsForecast/<str:name_of_area>/<str:resol>/year/<int:y>', views.query4c, name='query4c'),
    path('api/admin/ActualTotalLoad', views.upload_file_ATL, name='upload_file_ATL'),
    path('api/admin/AggregatedGenerationPerType', views.upload_file_AGPT, name='upload_file_AGPT'),
    path('api/admin/DayAheadTotalLoadForecast', views.upload_file_DATLF, name='upload_file_DATLF'),
    path('api/admin/users', views.sign_up, name='sign_up'),
    path('api/admin/users/<str:username>', views.modify1, name='modify1'),
    path('api/Reset', views.reset_db, name='reset_db'),
    path('api/HealthCheck', views.check_connection, name='check_connection'),
    path('api/github', views.github, name='github'),
    path('api/', include('django.contrib.auth.urls')),
    path('api/test', views.test, name='test')
]
