from django.shortcuts import render, redirect
from .forms import RegisterUser

# Create your views here.
def index(req):
    if req.method == 'POST':
        form = RegisterUser(req.POST)

        if form.is_valid():
            form.save()
            return redirect('/app/')
    else:
        form = RegisterUser()
    context = {'form':form}
    return render(req, 'index.html', context)