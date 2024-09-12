
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# create Router Object
router=DefaultRouter()

# Register StudentViewSet with Router
# router.register('studentapi', views.StudentModelViewSet, basename='student')
router.register('studentapi', views.StudentReadOnlyModelViewSet, basename='student')
# No need to manage studentapi/<int> urls, because Router will manage it.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
