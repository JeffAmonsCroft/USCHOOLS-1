from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('', views.homepage_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('accounts/password_reset_form/', views.request_password_reset, name='password_reset_form'),
    # path("reset/<str:token>/", views.reset_password, name="reset_password"),
    # path("request-reset/", views.request_password_reset, name="request_password_reset"),
    # path('accounts/password_reset_done/', views.password_reset_done_view, name='password_reset_done'),  
]
