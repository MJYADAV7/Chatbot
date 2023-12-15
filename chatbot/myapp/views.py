from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mybot(request):
    print("Manjeet Yadav")
    s='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><script>(function(w, d) { w.CollectId = "6405bc91a33baf3b4b821c92"; var h = d.head || d.getElementsByTagName("head")[0]; var s = d.createElement("script"); s.setAttribute("type", "text/javascript"); s.async=true; s.setAttribute("src", "https://collectcdn.com/launcher.js"); h.appendChild(s); })(window, document);</script><title>Document</title></head><body></body></html>'
    return HttpResponse(s)
