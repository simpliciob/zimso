from django.shortcuts import render
def index(request):
    return render(request, 'eschool/parents.html')

# Create your views here.
