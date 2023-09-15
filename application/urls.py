from django.urls import path
from . import views

urlpatterns = [
    path('',views.endpoint,name='endpoint'),
    path('advocate/',views.Advocate_list .as_view(),name='advocate_list'),
    path('advocate/<str:username>',views.Advocate_details .as_view(),name='advocate_detail'),

    #company urls path
    
    path('company/',views.company_list,name='company'),
]
