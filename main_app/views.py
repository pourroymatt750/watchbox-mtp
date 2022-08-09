from cmath import log
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Watch
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def watches_index(request):
  watches = Watch.objects.filter(user=request.user)
  return render(request, 'watches/index.html', {'watches': watches})

@login_required
def watches_detail(request, watch_id):
  watch = Watch.objects.get(id=watch_id)
  return render(request, 'watches/detail.html', {'watch': watch})

class WatchCreate(LoginRequiredMixin, CreateView):
  model = Watch
  fields = ['brand', 'name', 'reference', 'delivery', 'year']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WatchUpdate(LoginRequiredMixin, UpdateView):
  model = Watch
  fields = ['brand', 'name', 'reference', 'delivery', 'year']

class WatchDelete(LoginRequiredMixin, DeleteView):
  model = Watch
  success_url = '/watches/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('watches_index')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  