from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You can Login Now!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    context={'form': form}
    return render(request, "account/inscription.html", context)



@login_required
def profile(request):

    return render(request, 'account/profile.html', {})