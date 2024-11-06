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
        # Очистка сессии при загрузке страницы
        request.session['links'] = []
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # Сохранение объекта, включая генерацию уникального хэша
        paste = form.save()

        # Генерация уникальной ссылки
        unique_link = self.request.build_absolute_uri(f'/{paste.unique_hash}/')

        # Добавляем ссылку в сессию
        links = self.request.session.get('links', [])
        links.append(unique_link)
        self.request.session['links'] = links

        # Отображение страницы с обновленным списком ссылок
        return self.render_to_response(self.get_context_data(links=links))


from django.shortcuts import render, get_object_or_404
from .models import PasteBin


def check_text(request, unique_hash):
    # Извлекаем объект PasteBin по уникальному хэшу или возвращаем 404, если не найден
    text_object = get_object_or_404(PasteBin, unique_hash=unique_hash)

    # Передаем текст и уникальный хэш в шаблон
    return render(request, 'api/user_text.html', {
        'text': text_object.content,  # текст, который нужно отобразить
        'unique_hash': unique_hash  # уникальный хэш для отображения ссылки
    })


class UpdateText(UpdateView):
    model = PasteBin
    fields = ['content']
    template_name = 'api/user_update.html'  # Шаблон для редактирования текста
    context_object_name = 'pastebin'

    def get_object(self, queryset=None):
        # Ищем объект по уникальному хэшу
        unique_hash = self.kwargs.get('unique_hash')
        return get_object_or_404(PasteBin, unique_hash=unique_hash)

    def get_success_url(self):
        # После успешного редактирования перенаправляем пользователя обратно на страницу просмотра текста
        return reverse_lazy('text', kwargs={'unique_hash': self.object.unique_hash})