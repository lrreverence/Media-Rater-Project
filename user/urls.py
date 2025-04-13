from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import signup

app_name = 'user'

urlpatterns=[
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]