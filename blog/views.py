from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def pricing(request):
    return render(request, 'blog/pricing.html', {})

def team(request):
    return render(request, 'blog/team.html', {})
