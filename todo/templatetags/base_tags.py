from django import template
from ..models import ToDo

register = template.Library()

@register.simple_tag(takes_context=True)
def current_todos(context):
    request = context['request']
    return ToDo.objects.filter(user=request.user, datecomplete__isnull=True).count()

@register.simple_tag(takes_context=True)
def complete_todos(context):
    request = context['request']
    return ToDo.objects.filter(user=request.user, datecomplete__isnull=False).count()

@register.inclusion_tag('todo/todo_list_templatetags.html', takes_context=True)
def show_latest_todos(context):
    request = context['request']
    latest_todos =  ToDo.objects.filter(user=request.user, datecomplete__isnull=True).order_by('-created')[:3]
    alert = 'شما در حال حاضر کاری برای انجام دادن ندارید.'
    theader = 'تاریخ ایجاد'
    return {'latest_todos': latest_todos, 'title': 'کارهای ایجاد شده اخیر', 'alert': alert, 'theader': theader}

@register.inclusion_tag('todo/todo_list_templatetags.html', takes_context=True)
def show_latest_complete_todos(context):
    request = context['request']
    latest_todos =  ToDo.objects.filter(user=request.user, datecomplete__isnull=False).order_by('-created')[:3]
    alert = 'شما هیچ کار کامل شده ای ندارید.'
    theader = 'تاریخ تکمیل شدن'
    return {'latest_todos': latest_todos, 'title': 'کارهای کامل شده اخیر', 'alert': alert, 'theader': theader}