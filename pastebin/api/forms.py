from django import forms
from .models import PasteBin
class TextInputForm(forms.ModelForm):
    class Meta:
        model = PasteBin
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }
        labels = {
            'content': '',  # Убираем label
        }
    def clean_text(self):
        text = self.cleaned_data.get('content')
        max_size = 10 * 1024 * 1024  # 10 МБ в байтах

        if len(text.encode('utf-8')) > max_size:
            raise forms.ValidationError("Текст превышает допустимый размер 10 МБ.")

        return text
