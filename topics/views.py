from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Topic, Message
from .forms import TopicForm, MessageForm

# Create your views here.
User = get_user_model()


def redirect_to_index(request):
    return HttpResponseRedirect(reverse('index'))


class IndexView(View):

    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        return render(request, 'topics/index.html', {'topics': topics})


class TopicCreateView(LoginRequiredMixin, CreateView):
    login_url = 'account/login'

    model = Topic
    form_class = TopicForm
    template_name = 'topics/create_topic.html'
    success_url = 'topics'

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.author = self.request.user
        topic.save()
        return HttpResponseRedirect(reverse_lazy('index'))


class TopicView(View):

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
    login_url = 'account/login'

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

