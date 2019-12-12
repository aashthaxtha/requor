# to handle forms
from django import forms
from .models import QuestionModel,AnswerModel,CategoryModel


class QuestionForm(forms.ModelForm):
    class Meta: 
        model = QuestionModel
        # category = CategoryModel
        fields = '__all__'
