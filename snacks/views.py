from django.views.generic import ListView, DetailView
from .models import Snack

class SnacksListView(ListView):
  template_name = 'snacks_list.html'
  model = Snack

class SnacksDetailView(DetailView):
  template_name = 'snacks_detail.html'
  model = Snack