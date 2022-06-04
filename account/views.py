from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import CustomRegisterFrom
from django.contrib import messages




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password= password)

        if user is not None:
            login (request, user)
            messages.success(request, "signin successfully complete!!")
            return redirect('gallery')
        else:
            messages.error(request, "Password or username wrong! please try again")

    return render(request, 'account/signin.html')

    
def signup(request):
    form = CustomRegisterFrom ()
    if request.method == 'POST':
        form = CustomRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully Complete.")
            return redirect("signin")

            # subject = 'welcome to GFG world'
            # # message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
            # message = render_to_string('account/accountmail.html')
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [User.email, ]
            # send_mail( subject, message, email_from, recipient_list )
            # return redirect("signin")
        
    return render(request, 'account/signup.html', {'form':form} )


@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, "logout successfully Complete.")
    return redirect("gallery")



    
