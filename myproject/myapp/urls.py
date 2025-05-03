from django.urls import path
from . import views


urlpatterns = [path('', views.home, name='months_list'),
                path('events/January/', views.january, name='january'), 
                path('events/<str:month>/', views.events_by_month, name='events_by_month')
]
