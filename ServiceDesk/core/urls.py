from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('self_service/', views.self_service, name='self_service'),
    path('asset_tracking/', views.asset_tracking, name='asset_tracking'),
    path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
    path('track_tickets/', views.track_tickets, name='track_tickets'),
    path('logout/', views.user_logout, name='logout'),
    path('resolve_tickets/', views.resolve_tickets, name='resolve_tickets'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('reports/', views.reports, name='reports'),
    
]

