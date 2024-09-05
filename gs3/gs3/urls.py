
from django.contrib import admin
from django.urls import path
from api import views

# Django URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('studentapi/', views.student_api),  # Custom API endpoint for student data
]
