from django.shortcuts import render
from medicine.models import Medicine
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from medicine.models import Medicine



# Create your views here.

def index(request):
    """View function for home page of site."""

    num_medicines = Medicine.objects.all().count()
    
    context = {
        'num_medicines': num_medicines,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MedicineListView(LoginRequiredMixin,generic.ListView):
    model = Medicine
    paginate_by = 10


class MedicineDetailView(LoginRequiredMixin,generic.DetailView):
    model = Medicine



class MedicineCreate(LoginRequiredMixin,CreateView):
    model = Medicine
    fields = '__all__'
    initial = {'date_of_manufacture': '06/12/2022'}

class MedicineUpdate(LoginRequiredMixin,UpdateView):
    model = Medicine
    fields = '__all__'
class MedicineDelete(LoginRequiredMixin,DeleteView):
    model = Medicine
    success_url = reverse_lazy('medicines')

class SearchResultsView(LoginRequiredMixin,generic.ListView):
    model = Medicine
    template_name = "search_results.html"

    def get_queryset(self): 
        query = self.request.GET.get("search",None)
        if query: 
            return Medicine.objects.filter(product_name__icontains=query)
