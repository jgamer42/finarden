from django.shortcuts import render
from django.contrib.auth.models import Group
# Create your views here.
from users.forms import SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            group = Group.objects.get(name="app_user")
            user = form.save()
            user.refresh_from_db()  
            user.is_staff = True
            user.groups.add(group) 
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})

def converter(request):
    return render(request, 'converter.html')