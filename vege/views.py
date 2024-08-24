from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        # print(receipe_name, receipe_description, receipe_image)

        Receipe.objects.create(receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image)

        return redirect('/')

    queryset=Receipe.objects.all()

    if request.GET.get('search'):
        search_query = request.GET.get('search')
        queryset = Receipe.objects.filter(receipe_name__icontains=search_query)
        
    context={'receipes':queryset}
    return render(request, 'receipes.html', context)

@login_required(login_url='/login/')
def update(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == 'POST':

        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context={'receipe':queryset}
    return render(request, 'update.html', context)
    

def delete(request, id):
    receipe=Receipe.objects.get(id=id)
    receipe.delete()
    return redirect('/')

def login_page(request):

    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'Invalid username')
            return redirect('/login/')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.add_message(request, messages.ERROR, 'Invalid credentials')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):

    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, messages.ERROR, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create_user(
            username=username, 
            first_name=first_name, 
            last_name=last_name
            )

        user.set_password(password)
        user.save()

        messages.add_message(request, messages.SUCCESS, 'User created successfully')
 
        return redirect('/register/')

    return render(request, 'register.html')