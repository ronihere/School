from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('contactus/delete_todo/<int:id>',views.delete_todo,name='delete_todo'),
    path('contactus/',views.admin_,name='admin_'),
    path('FAQs/',views.faqs,name='FAQs'),
    path('course_notice/',views.course_notice,name='course_notice'),
    path('faculty/',views.faculty,name='faculty'),
    path('form/',views.form,name='form'),
    path('register/',views.form,name='form'),
    path('form/show/',views.show,name='show'),
    path('links/',views.links,name='links'),
    path('upcoming_events/',views.upcoming_events,name='upcoming_events'),
    path('covid/',views.covid,name='covid')
    # path('add/',views.add,name='add'),
    ]