from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.home, name='login'),
    path('register/', views.home, name='register'),
    path('logout/', views.home, name='logout'),
    path('companies/', views.home, name='companyindex'), #list of companies
    path('company/', views.home, name='periodindex'), #financial statement sets of a single company
    path('company/balances/', views.home, name='balance'),
    path('company/period/', views.home, name='period'), #statements of that period
    path('company/period/statement/', views.home, name='statement'), #single statement
    path('company/period/statement/fsli/', views.home, name='fsli'),
    path('company/period/statement/pov/', views.home, name='pov'),
    path('company/period/grouping', views.home, name='grouping'),
]
