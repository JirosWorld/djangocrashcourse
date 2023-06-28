from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
]

# Django version 2.0's path() object now doesn't support regular expressions. Use re_path for regular expressions, or leave out the '^'