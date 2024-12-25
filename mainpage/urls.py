from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.resume_detail, name='resume_detail'),
    path('resume/<int:pk>/download/', views.generate_pdf, name='download_pdf')

]
