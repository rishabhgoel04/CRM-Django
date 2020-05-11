from django.contrib import admin
from django.urls import path

from apps.common.views import HomeView, SignUpView
from apps.common.views import HomeView, SignUpView, DashboardView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Authentication 
    path('register/', SignUpView.as_view(), name="register"),

    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'
        ),
        name='login'
    ),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
        ),
        name='logout'
    ),


]