import os
from django.shortcuts import render,get_object_or_404,redirect
from .form import New_User_Form
from datetime import datetime
from .models import New_user

# Install xlrd version 1.2.0 if not installed
os.system('python -m pip install xlrd==1.2.0')

# Check if requests library is installed, install it if not
try:
    import requests
except ImportError:
    os.system('python -m pip install requests')
    import requests  # Import requests after installation
def index(request):
    url = 'https://api.quotable.io/random'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
    else:
        quote = "Error fetching quote."
        author = "Unknown"
    today=datetime.now()
    context = {
        'quote': quote,
        'author': author,
        'today':today
    }
    return render(request,'home.html',context)
def user(request):
    if request.method=='POST':
        form=New_User_Form(request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            email=request.POST.get('email')
            form.save()
            form=New_User_Form()
            context={
                'username':username,
                'email':email,
                'form':form
            }
            return render(request,'new_user.html',context)
    form=New_User_Form()
    return render(request,'new_user.html',{'form':form})

def exist_user(request):
    users=New_user.objects.all()
    return render(request,'exist_user.html',{'users':users})
def delete(request, user_id):
    user = get_object_or_404(New_user, id=user_id)
    user.delete()
    return redirect('exist_user')


