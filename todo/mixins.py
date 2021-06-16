from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ToDo


class OwnerMixin(object):    
    def get_queryset(self):        
        qs = super().get_queryset()        
        return qs.filter(user=self.request.user)


class OwnerEditMixin(object):    
    def form_valid(self, form):        
        form.instance.user = self.request.user
        return super().form_valid(form)


class OwnerToDoMixin(OwnerMixin, LoginRequiredMixin):    
    model = ToDo    
    fields = ['title', 'memo', 'important']   
    success_url = reverse_lazy('todo:dashboard')


class OwnerToDoEditMixin(OwnerToDoMixin, OwnerEditMixin):    
    template_name = 'todo/create-update-todo.html'