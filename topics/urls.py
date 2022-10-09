from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_index, name='index_redirect'),
    path('topics', views.IndexView.as_view(), name='index'),
    #path('topics/<slug:slug>', views.TopicView.as_view(), name='topic_view')
    path('create_topic', views.TopicCreateView.as_view(), name='topic_create'),
    ]
