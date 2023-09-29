from django.forms import ModelForm
from django import forms
from .models import Question
from django.core.validators import RegexValidator


class PostForm(ModelForm):
    phone_number = forms.CharField(
        min_length=11,
        required=True,
        validators=[
            RegexValidator(
                '^(8|\\+7)(\\ |\\(| \\(|\\-|)\\d{3}(\\ |\\) |-|\\)|)(\\d{7}|\\d{3}-\\d{2}-\\d{2}|\\d{3} \\d{2} \\d{2})$',
                message="Неправильный формат номера"
            )
        ]
    )

    class Meta:
        model = Question
        fields = ['addressee', 'name', 'question', 'email', 'text_of_question', 'phone_number']
