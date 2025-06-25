from django.contrib import admin
from django.urls import include, path


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('emails/', include('send_email.urls', namespace='send_email')),
])
