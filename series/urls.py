from django.urls import path
from . import views

app_name = "series"

urlpatterns = [
  path('', views.home1, name="home1"),
  path('details/<int:id>/', views.detail, name="detail"),
  path('addseries/', views.add_series, name= "add_series"),
  path('editseries/<int:id>/', views.edit_series, name= "edit_series"),
  path('deleteseries/<int:id>/', views.delete_series, name= "delete_series"),
  path('addreview/<int:id>/', views.add_review, name= "add_review"),
  path('editreview/<int:series_id>/<int:review_id>/', views.edit_review, name= "edit_review"),
  path('deletereview/<int:series_id>/<int:review_id>/', views.delete_review, name= "delete_review"),
  path('contact/',views.contact, name="contact"),
  ]