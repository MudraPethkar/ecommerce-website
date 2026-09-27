from django.urls import include, path
from django.contrib.auth.views import LogoutView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
