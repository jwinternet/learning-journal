from django.shortcuts import render


def index(request):
	"""The home page for Learning Journal."""
	return render(request, 'learning_journals/index.html')
