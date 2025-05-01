from django.shortcuts import render,redirect
from .models import Items,BookTable
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    items =  Items.objects.all()
    return render(request, 'index.html',{'items': items})
 
def menu(request):
    items =  Items.objects.all()
    return render(request, 'menu.html', {'items': items})
 
def about(request):
    return render(request,'about.html')
 
def book(request):
    if request.method == 'POST':
        name = request.POST.get('user-name')
        phone_number = request.POST.get('phone-number')
        email = request.POST.get('user-email')
        total_person = request.POST.get('total-person')
        booking_date = request.POST.get('booking-date')

        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_date != '':
            data = BookTable(Name=name, Phone_number=phone_number, Email=email, Total_person=total_person, Booking_date=booking_date)
            data.save()
            return redirect('index') 

    return render(request, 'book.html')
 
def rating(request):
    return render(request,'rating.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
            else:
                user_reg=User.objects.create_user(username=username,email=email, password=password)
                user_reg.save()
                return redirect('index')
        else:
            messages.info(request,"Password does not match")
            
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate (username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info (request, "Invalid Username or Password")
    return render(request,'login.html')
 