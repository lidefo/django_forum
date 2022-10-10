from django import forms
from .models import Topic, Message


class TopicForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    class Meta:
        model = Topic
        exclude = ['author', 'create_date', 'slug']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['author', 'create_date', 'topic']