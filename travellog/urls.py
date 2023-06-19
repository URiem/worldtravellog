from . import views
from django.urls import path

urlpatterns = [
    path('add_logentry/', views.AddLogentry.as_view(), name='add_logentry'),
    path('user_logentry/', views.UserLogentryList.as_view(), name='user_logentry'),
    path('', views.LogentryList.as_view(), name='home'),
    path('<slug:slug>/', views.LogentryDetail.as_view(), name='logentry_detail'),
    path('update/<slug:slug>', views.UpdateLogentry.as_view(), name='update'),
    path('delete/<slug:slug>', views.DeleteLogentry.as_view(), name='delete'),
    path('<int:pk>/delete_image', views.delete_image, name='delete_image'),
]
