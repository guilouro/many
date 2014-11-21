from django.shortcuts import render
from core.models import Post

# Create your views here.
def home(request):
	context = {
		"post" : Post.objects.get(pk=1)
	}

	return render(request, 'index.html', context)