from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        massage = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")
    return render(request, 'contacts.html')
