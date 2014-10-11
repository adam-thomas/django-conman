from django.views.generic import ListView

from ..models import Node


class Index(ListView):
    model = Node
    template_name = 'nav_tree/cms/node_list.html'
