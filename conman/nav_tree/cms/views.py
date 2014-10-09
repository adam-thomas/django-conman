from django.views.generic import ListView

from ..models import Node


class Index(ListView):
    model = Node
