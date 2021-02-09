from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New_task")

def index(request):
    if "task" not in request.session:
        request.session["task"] = []
    return render(
        request,
        "task/task.html",
        {"task":request.session["task"]})

def add_task(request):
    if  (request.method == "POST"):
        form = NewTaskForm(request.POST)
        if (form.is_valid()):
            tasks = form.cleaned_data["task"]
            request.session["task"] += [tasks]
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html", {
                "form":form
            })
    return render(request, "task/add.html" , {
        "form":NewTaskForm()
    })
