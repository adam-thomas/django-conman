from django.views.generic import ListView, UpdateView

from ..models import Node


class Index(ListView):
    model = Node
    template_name = 'nav_tree/cms/node_list.html'


class NodeUpdate(UpdateView):
    model = Node
    template_name = 'nav_tree/cms/node_form.html'

    def get_success_url(self):
        return self.object.get_cms_url()
