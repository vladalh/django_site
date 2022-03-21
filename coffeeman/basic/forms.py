from .models import Review
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "comments"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес электронной почты'
            }),
            "comments": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите свой отзыв'
            }),
        }
