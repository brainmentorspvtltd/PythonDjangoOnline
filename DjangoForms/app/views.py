from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def index(req):
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            return render(req, 'result.html', {
                'name' : form.cleaned_data['name'],
                'email' : form.cleaned_data['email']
            })
    else:
        form = RegistrationForm()
    
    return render(req, 'index.html', {'form':form})