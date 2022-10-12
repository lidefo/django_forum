from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Topic, Message
from .forms import TopicForm, MessageForm

from pytils.translit import slugify

# Create your views here.
User = get_user_model()


def redirect_to_index(request):
    return HttpResponseRedirect(reverse('index'))


class IndexView(View):
    '''This view for main page.'''

    def get(self, request, *args, **kwargs):
        topics = Topic.objects.order_by('-id')
        messages_count = Message.objects.count()
        topics_count = Topic.objects.count()
        users_count = User.objects.count()
        data = {
            'topics': topics,
            'messages_count': messages_count,
            'topics_count': topics_count,
            'users_count': users_count,
        }
        return render(request, 'topics/index.html', data)


class TopicCreateView(LoginRequiredMixin, CreateView):
    '''This view for create new Topic model. For creating user must be authenticated.'''

    login_url = 'account/login'

    model = Topic
    form_class = TopicForm
    template_name = 'topics/create_topic.html'

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.author = self.request.user
        topic.save()
        slug = slugify(topic.title)
        url = reverse_lazy('topic_view', kwargs={'slug': slug})
        return HttpResponseRedirect(url)


class TopicView(View):
    '''This view for detail info about topic.'''

    def get(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        messages = Message.objects.filter(topic=topic).order_by('-id')
        domain_redirect = 'publish/{}'.format(topic.slug)
        data = {
            'topic': topic,
            'messages': messages,
            'domain_redirect': domain_redirect
        }
        return render(request, 'topics/topic_view.html', data)


class MessageCreateView(LoginRequiredMixin, CreateView):
    '''This view for create new Message model. For creating user must be authenticated.'''

    login_url = '/account/login'

    model = Message
    form_class = MessageForm
    template_name = 'topics/create_message.html'

    def form_valid(self, form):
        message = form.save(commit=False)
        message.author = self.request.user
        slug = self.kwargs['slug']
        message.topic = Topic.objects.get(slug=slug)
        message.save()
        url = reverse_lazy('topic_view', kwargs={'slug': slug})
        return HttpResponseRedirect(url)
