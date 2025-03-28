from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.blog.urls')),  # Blog app'in URL'lerini dahil et
    path('account/', include('blogapp.account.urls')),  # Eğer başka bir app varsa onu da ekleyebilirsin
]
