from django.urls import path


from . import views
app_name = 'accounts'
urlpatterns = [
path('signup',views.sign_up,name = 'signup'),
path('profile',views.profile,name = 'profile'),
path('profile/edit',views.profile_edit,name = 'profile_edit'),


#user

path('doctors/',views.doctor_list,name = 'doctor_list'),
path('<slug:slug>/',views.doctor_detail,name = 'doctor_detail'),

]
