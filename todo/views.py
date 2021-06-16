from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import ToDo
from .mixins import OwnerToDoMixin, OwnerToDoEditMixin

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


class CurrentToDoList(ListView):
    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user, datecomplete__isnull=True)
    template_name = 'todo/current.html'


class CompleteToDoList(ListView):
    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user, datecomplete__isnull=False)
    template_name = 'todo/complete.html'


class ToDoCreate(SuccessMessageMixin, OwnerToDoEditMixin, CreateView):
    success_message = "تودو با موفقیت ایجاد شد."


class ToDoUpdate(SuccessMessageMixin, OwnerToDoEditMixin, UpdateView):
    success_message = "تودو با موفقیت ویرایش شد."


class ToDoDelete(SuccessMessageMixin, OwnerToDoMixin, DeleteView):
    template_name = 'todo/delete-todo.html'


@login_required
def complete_todo(request, pk):
    todo = get_object_or_404(ToDo, id=pk, user=request.user)
    if request.method == "POST":
        todo.datecomplete = timezone.now()
        todo.save()
        messages.success(request, 'تودو با موفقیت کامل شد.')
        return redirect('todo:dashboard')
    else:
        messages.error(request, 'تودو کامل نشد.')
        return redirect('todo:dashboard')
