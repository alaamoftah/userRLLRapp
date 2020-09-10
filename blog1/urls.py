from django.contrib import admin
from django.urls import path, include

# Media settings add on
from django.conf.urls.static import static
from django.conf import settings

# import line for register.html which suppose to be in users APP
from users import views as user_views

# user login logout authentications 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('global/', admin.site.urls),
    path('', include('blogs.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)