from . import views
from django.urls import path

urlpatterns = [
    path('', views.LogentryList.as_view(), name='home'),
    path('<slug:slug>/', views.LogentryDetail.as_view(), name='logentry_detail'),
    path('add_logentry/', views.AddLogentry.as_view(), name='add_logentry'),
]
