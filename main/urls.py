from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('material/search/', views.material_search, name="material_search"),
    path('universities/', views.university_list, name="university_list"),
    path('university/<slug:slug>', views.university_detail, name="university_detail"),
    path('about/', views.about, name="about"),
    path('courses/', views.course_list, name='courses'),
    path('course/<slug:slug>', views.course_detail, name='course'),
    path('contact/', views.contact, name="contact"),
    path('ajax/load-depts', views.load_depts, name='ajax_load_depts')
]