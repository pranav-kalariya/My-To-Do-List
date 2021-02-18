from django.shortcuts import render
from django.contrib.auth import login, authenticate
from todo_list_app.forms import SignUpForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ToDo
from .serializers import TasksSerializer

# Create your views here.
@csrf_exempt
def index(request):
    if request.user.is_authenticated:
        return render(request, 'my_todo.html')
    if request.method == 'GET':
        return render(request, 'login.html', {})
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        my_user = User.objects.filter(username=data['username']).first()
        print(User.objects.all())
        my_pass = data['password']
        if my_user is not None:
            if my_user.check_password(my_pass):
                print("Logging in")
                login(request, my_user)
                return render(request, "my_todo.html",{})
            else:
                return HttpResponse('{"error": "Wrong Creds"}')
        else:
            return HttpResponse('{"error": "User does not exist"}')
        return render(request, "my_todo.html",{})

def register_view(request):
    if request.method == 'GET':
        print(User.objects.all())
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    if request.method == 'POST':
        # print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user.set_password(password)
            user.save()
            print(User.objects.all())
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("user: {}".format(user))
                if user.is_active:
                    login(request, user)
                    return redirect('index')
            return redirect("index")
        return HttpResponse('{"error": "Try Again"}')
@csrf_exempt
def tasks_list(request, user_todo=None):
    print("In tasks")
    if request.method == 'GET':
        # print("user_todo = {}".format(user_todo))
        # user_todo = "test"
        # print("data = {}".format())
        my_user = User.objects.filter(username=user_todo).first()
        tasks = ToDo.objects.filter(user=user_todo)
        print(tasks)
        serializer = TasksSerializer(tasks, many=True, context={'request': request})
        for message in tasks:
            message.is_done = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print("In tasks post")
        data = JSONParser().parse(request)
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            print("In serializer")
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def delete_tasks(request, user_todo):
    if request.method == 'GET':
        # print("user_todo = {}".format(user_todo))
        # user_todo = "test"
        # print("data = {}".format())
        tasks = ToDo.objects.filter(user=user_todo)
        tasks.delete()
        return render(request, "my_todo.html",{})