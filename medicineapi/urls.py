from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login_api'),
    path('logout', views.logout, name='logout_api'),
    path('signup', views.SignupView.as_view(), name='signup_api'),
    path('create', views.CreateMedicine.as_view()),
    path('get', views.ReadMedicine.as_view()),
    path('update/<int:pk>', views.UpdateMedicine.as_view()),
    path('delete/<int:pk>', views.DeleteMedicine.as_view()),
    path('search', views.MedicineSearch.as_view()),

]

