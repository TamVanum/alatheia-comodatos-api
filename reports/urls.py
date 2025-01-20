
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from reports import views

router = DefaultRouter()


urlpatterns = [
    path("sample-report", views.sample_report),
    path("", include(router.urls))
]