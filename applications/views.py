from django.shortcuts import render, redirect
from .forms import ApplicationForm


def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list') 
    else:
        form = ApplicationForm()
    return render(request, 'applications/create_application.html', {'form': form})
