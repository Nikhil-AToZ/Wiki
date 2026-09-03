from django.shortcuts import render
from markdown import markdown
from . import util 


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
    content = util.get_entry(title)
    return html(request,content)

def search(request):
    entries = util.list_entries()
    merged = "".join(entries)
    
    if request.method == "POST" :
        task = request.POST["q"].lower()
    
        if task in entries :
            return page(request,task)
        if task not in merged:
           return r_render(request,"No matching entry found!",'All other Pages')
        
        entries = [val for val in entries if task in val]
        return render(request,"encyclopedia/index.html",{
            "entries":entries,
            "header" : "No matching Page found",
            "H1":"Closet Pages"
        })
