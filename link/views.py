from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import LinkForm

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link = form.save()

            return redirect('/')
    else:
        form = LinkForm()

    return render(request, 'link/add_link.html',{
        'form':form
    })