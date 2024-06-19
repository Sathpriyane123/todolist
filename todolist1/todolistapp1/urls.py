from django.urls import path
from.import views


urlpatterns= [
    path('',views.home ,name='home'),
    path('del/<int:id>',views.delform,name='del'),
    path('dta',views.form, name='dta'),
]