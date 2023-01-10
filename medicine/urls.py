
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicinelist/', views.MedicineListView.as_view(), name='medicines'),
    path('medicine/<int:pk>', views.MedicineDetailView.as_view(), name='medicine-detail'),
    path('medicine/create/', views.MedicineCreate.as_view(), name='medicine_create'),
    path('medicine/<int:pk>/update/', views.MedicineUpdate.as_view(), name='medicine_update'),
    path('medicine/<int:pk>/delete/', views.MedicineDelete.as_view(), name='medicine_delete'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
]
