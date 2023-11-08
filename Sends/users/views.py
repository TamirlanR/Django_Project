from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    return render(request, 'Main.html')

@login_required
def restricted_view(request):
    # Your view logic for the restricted content
    return render(request, 'restricted_template.html')
