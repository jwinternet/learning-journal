from django.shortcuts import render

from .models import Topic


def index(request):
	"""The home page for Learning Journal."""
	return render(request, 'learning_journals/index.html')


def topics(request):
	"""show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_journals/topics.html', context)

