from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log user in
            return redirect('#')
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user in
            user=form.get_user()
            login(request,user)
            return redirect('#')

    else:
        form=AuthenticationForm()

    return  render(request,'login.html',{'form':form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('#')