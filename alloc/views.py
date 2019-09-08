from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.views.generic import ListView, DetailView
from django.db.models import Q #Help in multiple filtering
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

# def alloc(request):
#     return render(request, 'alloc.html')

class projectCreateView(CreateView):
    model = Project
    template_name = 'alloc.html'
    fields = ['regno', 'name', 'email', 'department','projecttype', 'statement', 'aims', 'suplist']
    
    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, 'You have succesfully submitted your project topic!')
        return redirect('alloc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submitted"] = Project.objects.filter(manager=self.request.user).count() 
        return context

class projectAllocView(ListView):
    template_name = 'viewalloc.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        projects = super().get_queryset()
        return projects.filter(manager=self.request.user)