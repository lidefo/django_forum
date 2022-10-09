from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Topic
from .forms import TopicForm

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
    success_url = 'topics'  # или '/topics'

    def form_valid(self, form):
        topic = form.save(commit=False)
        topic.author = self.request.user
        topic.save()
        return HttpResponseRedirect(reverse_lazy('index'))
