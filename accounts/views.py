from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


@login_required
def home(request):
    if request.user.is_authenticated:
        user = request.user
        # do something with the user object here
        return render(request, 'db/index.html', {'user': user})
    else:
        return redirect('search:login')


@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search:search')
    else:
        form = SignUpForm()
    return render(request, 'db/signup.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('search:search')
            else:
                form.add_error(None, 'Invalid username or password')
                print("Invalid username or password")
        else:
            print("Form is invalid")
    else:
        form = AuthenticationForm()
    return render(request, 'db/login.html', {'form': form})
