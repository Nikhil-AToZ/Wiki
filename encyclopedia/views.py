from django.shortcuts import render
from markdown import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request,title):
    
    with open(f"entries/{title}.md",'r') as f :
        content = f.read()

    html = markdown(content)
    return render(request,"encyclopedia/page.html",{
        "content":html
    })

