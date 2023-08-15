from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def login_view(request):
    # check request is Post or Gate
    if request.method == "POST":

        # catch username and password from login.html file
        username = request.POST['username']
        password = request.POST['password']
        # create a authenticate user
        user = authenticate(request, username=username, password=password)
        # check he/she is a authenticate user or not
        if user is not None:
            # login success
            login(request, user)

            search_page_url = reverse('search_page')  # Generate URL for Khoj_the_search_Page
            # User go to search_page of Khoj_the_search_Page app
            return redirect(search_page_url)
        else:
            error_message = "Invalid username and password"
            return render(request, 'authentication/login.html', {'error_message': error_message})
    return render(request, 'authentication/login.html')

def register_view(request):
    if request.method == 'POST':
        # make a user creation form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            success_message = "Registration Completed"
            return render(request, "authentication/login.html", {"success_message": success_message})

    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
