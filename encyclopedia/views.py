from django.shortcuts import render
from markdown import markdown
from . import util 
from django import forms 
from django.http import HttpResponseRedirect
from django.urls import reverse
def html(request,content):
    if content is None :
        return r_render(request,"Error loading file","All Pages")
    html_cont =  markdown(content)
    return render(request,"encyclopedia/page.html",{
            "content":html_cont
        })

def r_render(request,header,h1):
    return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "header":header,
            "H1":h1
        })

def index(request):

    return r_render(request,"",'All Pages')


def page(request,title):
    print(title)
    content = util.get_entry(title)
    return html(request,content)

def search(request):
    
    entries = util.list_entries()
    merged = "".join(entries)
    task = request.POST["q"].lower()
    if util.get_entry(task) != None:
            return page(request,task)
    if task not in merged:
           return r_render(request,"No matching entry found!",'All other Pages')
        
    entries = [val for val in entries if task in val]
    return render(request,"encyclopedia/index.html",{
            "entries":entries,
            "header" : "No matching Page found",
            "H1":"Closet Pages"
             })


class newform(forms.Form):
    page_name = forms.CharField(
        label="Enter the page name",
        widget=forms.TextInput(attrs={
            "class": "form-input",
            "placeholder": "Enter page name"
        })
    )

    page_content = forms.CharField(
        label="Enter page content",
        widget=forms.Textarea(attrs={
            "class": "form-input",
            "placeholder": "Enter page content",
            "id":"page_content"
        })
    )

def Add_page(request):
    url = "encyclopedia/Add_page.html"
    if request.method == "POST":
        form = newform(request.POST)
        if form.is_valid():
            Title = request.POST["page_name"]
            content = request.POST["page_content"]
            util.save_entry(Title,content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else :
             return render(request,url,{"form":form})
    return render(request,url ,{
        "form":newform()
     })