from django.http import HttpResponse

def pagen_views(request,page):
    html="<h1>这是编号为%s的网页</h1>"%(page)
    return HttpResponse(html)