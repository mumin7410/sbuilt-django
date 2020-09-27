from django.shortcuts import render
from .models import image
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        msg = request.POST.get('text-area')

        send_mail(
            fullname,
            msg,
            email,
            ['mumin96303@gmail.com'],
        )
        return render(request,'index.html',{'fullname':fullname,'email':email,'text-area':msg})
    else:
        return render(request, 'index.html')

def gallery(request):
    image_data = image.objects.all()
    return render(request,'gallery.html',{'imgs':image_data})

def price(request):
    return render(request,'price.html')

def index2(request):
    return render(request, 'index2.html')



