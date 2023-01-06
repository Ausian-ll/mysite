from django.shortcuts import render
from .models import Tb_book_info
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def get_page(request):
    all_book = Tb_book_info.objects.filter(is_delete=False)
    if request.method == "GET":
        return render(request,'book/all_book.html',locals())

def detail(request,book_id):
    try:
        book = Tb_book_info.objects.get(book_id = book_id )
    except Tb_book_info.DoesNotExist:
        return HttpResponse("书籍为空")

    if request.method == 'GET':
        return render(request, 'book/detail.html', locals())

def change_status(request):
    book_id = request.GET.get('book_id')
    status = request.GET.get('status')
    if not book_id:
        return HttpResponse("书籍不存存在，请求异常")
    try:
        book = Tb_book_info.objects.get(book_id=book_id,is_delete=0)
    except Exception as e:
        print("--The book_id does nor exist--")
        return HttpResponse("--The book_id does nor exist--")
    if status == '1':
        book.status = '1'
        book.save()
        return HttpResponseRedirect("/book/all_book")
    else:
        book.status = '0'
        book.save()
        return HttpResponseRedirect("/book/all_book")
