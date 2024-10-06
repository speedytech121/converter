from django.shortcuts import render

# View for homepage
def home(request):
    return render(request, 'converter/home.html')
