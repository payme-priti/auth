from django.urls import path
from .views import login_view, signup_view, forget_password_view, logout_view

urlpatterns = [
     path('login/', login_view, name='api_login'),
    path('signup/', signup_view, name='api_signup'),
    path('forget_password/', forget_password_view, name='api_forget_password'),
    path('logout/', logout_view, name='api_logout'),
]
