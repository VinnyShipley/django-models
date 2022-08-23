from django.views.generic import ListView

class SnacksListView(ListView):
  template_name = 'snacks_list.html'
  model = 
