from django import forms
from .models import Topic, Message


class TopicForm(forms.ModelForm):
    '''Form for creating Topic model.'''
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    class Meta:
        model = Topic
        exclude = ['author', 'create_date', 'slug']


class MessageForm(forms.ModelForm):
    '''Form for creating Message model.'''
    class Meta:
        model = Message
        exclude = ['author', 'create_date', 'topic']