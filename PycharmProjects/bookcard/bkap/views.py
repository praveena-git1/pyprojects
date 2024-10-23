from django.shortcuts import render,redirect
from .models import book
# Create your views here.

def add_book(request):
    if request.method == "POST":
        book_obj = book()
        book_obj.id = request.POST.get('id')
        book_obj.name = request.POST.get('name')
        book_obj.author = request.POST.get('author')
        book_obj.image = request.POST.get('image')  # Corrected field name
        book_obj.save()
        return redirect('show')
    return render(request, 'bookid.html')
def show_book(request):
    book_obj=book.objects.all()
    return render(request,'showbook.html',context={'data':book_obj})
def delete(request,id):
    book_obj=book.objects.get(id=id)
    book_obj.delete()

    return redirect('/show')
def update(request,id):
    book_obj = book.objects.get(id=id)
    if request.method == "POST":
        book_obj.id = request.POST.get('id')
        book_obj.name = request.POST.get('name')
        book_obj.author = request.POST.get('author')
        book_obj.save()
        return redirect('/newbook')
    return render(request, 'editbook.html', {'data': book_obj})
