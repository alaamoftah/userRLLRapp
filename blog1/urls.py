from django.contrib import admin
from django.urls import path, include

# Media settings add on
from django.conf.urls.static import static
from django.conf import settings

# import line for register.html which suppose to be in users APP
from users import views as user_views

urlpatterns = [
    path('global/', admin.site.urls),
    path('', include('blogs.urls')),
    path('register/', user_views.register, name='register'),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)