"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from .models import Comment
from.models import Blog
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class poolForm(forms.Form):
	age = forms.IntegerField(label = 'Ваш возраст', min_value = 10, max_value = 100, required = True) 
	sex = forms.ChoiceField(label = 'Пол',
							choices = [('1', 'Мужской'), ('2','Женский')],
							widget = forms.RadioSelect,
							required = True, initial = 1)
	game = forms.MultipleChoiceField(label = 'Ваш жанр', choices = [('1', 'RPG'), ('2', 'Шутеры'), ('3', 'Кампания')],
											widget = forms.CheckboxSelectMultiple,
											required = True)
class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('text',) 
        labels = {'text': "Комментарий"}
        

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}

        

