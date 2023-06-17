from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category

class InventoryMan(TemplateView):
    template_name = 'index.html'
    
class SignUp(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'signup.html', {"form": form })
        
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = authenticate(
				username=form.cleaned_data['username'],
    			password=form.cleaned_data['password1']
			)
            login(request, user)            
            return redirect("inventory-man")
        
        return render(request, 'signup.html', {'form': form})

# The meat in the application is mostly down here, 
class Dashboard(View):
    def  get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by("id")
        return render(request, 'dashboard.html', {"items": items})
    
class FakaIzinto(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'put_tings.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class Edit(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'put_tings.html'
    success_url = reverse_lazy('dashboard')
    
class Khipha(DeleteView):
	model = InventoryItem
	template_name = 'khipha_daideng.html'
	success_url = reverse_lazy('dashboard')
	context_object_name = 'item'