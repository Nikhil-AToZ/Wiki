from django.shortcuts import render
from markdown import markdown
from . import util 




def r_render(request,header):
    return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "header":header
        })

def index(request):
    return r_render(request,"")


def page(request,title):
    print("page",title)
    with open(f"entries/{title}.md",'r',encoding="utf-8") as f :
        content = f.read()

    html = markdown(content)
    return render(request,"encyclopedia/page.html",{
        "content":html
    })

def search(request):
    entries = util.list_entries()
    merged = "".join(entries)
    if request.method == "POST" :
        task = request.POST["q"].upper()
        
        if task not in merged:
           return r_render(request,"No matching entry found!")
        
        entries = [val for val in entries if task in val]

        # print(task*100)
        # print(entries)
        # print(entries)
    return r_render(request,"!Error Internal server Error!!! refector the all pages to most closest pages ")
    
