from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import PasteBin
from .forms import TextInputForm
from .utils import DataMixin


class Main(FormView):
    form_class = TextInputForm
    template_name = 'api/input.html'

    def get(self, request, *args, **kwargs):
        request.session['links'] = []
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        paste = form.save()
        unique_link = self.request.build_absolute_uri(f'/{paste.unique_hash}/')
        links = self.request.session.get('links', [])
        links.append(unique_link)
        self.request.session['links'] = links
        return self.render_to_response(self.get_context_data(links=links))


from django.shortcuts import render, get_object_or_404
from .models import PasteBin


def check_text(request, unique_hash):
    text_object = get_object_or_404(PasteBin, unique_hash=unique_hash)
    return render(request, 'api/user_text.html', {
        'text': text_object.content,
        'unique_hash': unique_hash 
    })


class UpdateText(UpdateView):
    model = PasteBin
    fields = ['content']
    template_name = 'api/user_update.html'
    context_object_name = 'pastebin'

    def get_object(self, queryset=None):
        unique_hash = self.kwargs.get('unique_hash')
        return get_object_or_404(PasteBin, unique_hash=unique_hash)

    def get_success_url(self):
        return reverse_lazy('text', kwargs={'unique_hash': self.object.unique_hash})
