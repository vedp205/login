from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import UserCreationform # type: ignore
from django.contrib.auth import login,logout
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationform(request.POST)
        if form.isvalid():
            user = form.save()
            login(request,user) 
    else:
        form=UserCreationform()
        return render(request,'auth/register.html',{'form':form})
def login_view(request):
    pass
def dashboard_view(request):
    pass
def logout_view(request):
    pass

