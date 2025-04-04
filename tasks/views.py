from django.shortcuts import render, redirect

tasks = []  # Simple list to store tasks

def index(request):
    return render(request, "tasks/index.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            tasks.append(task)
    return redirect("index")
