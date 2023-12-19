import sys
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from Gamify import settings
from Gamify_Admin.forms import GamifyUserForm, CityForm, CompanyForm, TypeForm, GameForm
from Gamify_Admin.models import City, GamifyUser, Company, Type, Game, Wishlist, Feedback, Cart, OrderDetail, Order
from django.contrib import messages
from datetime import date
import random
import re

def register_user(request):
    city = City.objects.all()
    if request.method == "POST":
        form = GamifyUserForm(request.POST)
        print(f"\n\n\n\n\n--------------------> {form.errors}")

        if form.is_valid():
            try:
                form.save()
                return redirect('/admin_register')

            except Exception as e:
                print(f"\n\n\n\n\n SYSTEM ERROR --------------------> {sys.exc_info()}")
                print(f"\n\n\n\n\n EXCEPTION ERROR --------------------> {e}")

    else:
        form = GamifyUserForm()

    return render(request, 'admin_Register_Login.html', {'form': form, 'city': city})


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = GamifyUser.objects.filter(user_email=email, user_password=password, is_admin=1).count()
        print("-------------------", email, "---------------------", password)
        if val == 1:
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid Username or Password !!!")
            return redirect('/admin_register/')
    else:
        return render(request, "admin_Register_Login.html")


def user_forgot_password(request):
    return render(request, "admin_Forgot_Password.html")


def user_otp(request):
    return render(request, "admin_Otp.html")


def sendotp(request):
    otp1 = random.randint(10000, 99999)

    e = request.POST['fp_email']
    request.session['session_email'] = e

    obj = GamifyUser.objects.filter(user_email=e).count()

    if obj == 1:

        GamifyUser.objects.filter(user_email=e).update(user_otp=otp1, user_otp_used=0)
        subject = 'OTP Verification'
        message = str(f"{otp1} is your OTP to access Gamify. "
                      f"\nFor security reasons, DO NOT share this OTP with anyone.")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'admin_Otp.html')

    else:
        messages.error(request, "Invalid Email !!!")
        return render(request, "admin_Forgot_Password.html")


def set_password(request):
    if request.method == "POST":

        email_otp = request.POST['u_otp']
        new_password = request.POST['u_new_password']
        confirm_cpass = request.POST['u_confirm_password']

        if new_password == confirm_cpass:
            pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
            x = bool(re.match(pattern, new_password))

            if x:
                e = request.session['session_email']
                val = GamifyUser.objects.filter(user_email=e, user_otp=email_otp, user_otp_used=0).count()

                if val == 1:
                    GamifyUser.objects.filter(user_email=e).update(user_otp_used=1, user_password=new_password)
                    return redirect("/admin_register")
                else:
                    messages.error(request, "Invalid OTP !!!")
                    return render(request, "admin_Otp.html")

            else:
                messages.error(request, """Password Credentials :
                                                Contains at least 8 characters, 
                                                Contains at least one uppercase letter,
                                                Contains at least one lowercase letter,
                                                Contains at least one digit,  
                                                Contains at least one special character !!!""")
                return render(request, "admin_Otp.html")

        else:
            messages.error(request, "New password and Confirm password does not match !!!")
            return render(request, "admin_Otp.html")

    else:
        return redirect("/forgot_password")


def show_city(request):
    city = City.objects.all()
    return render(request, "city.html", {"city":city})

def show_user(request):
    user = GamifyUser.objects.all()
    return render(request, "user.html", {"user":user})

def show_company(request):
    company = Company.objects.all()
    return render(request, "company.html", {"company":company})

def show_type(request):
    type = Type.objects.all()
    return render(request, "type.html", {"type":type})

def show_game(request):
    game = Game.objects.all()
    return render(request, "game.html", {"game":game})

def show_wishlist(request):
    wishlist = Wishlist.objects.all()
    return render(request, "wishlist.html", {"wishlist":wishlist})

def show_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, "feedback.html", {"feedback":feedback})

def show_cart(request):
    cart = Cart.objects.all()
    return render(request, "cart.html", {"cart":cart})

def show_order_detail(request):
    order_detail = OrderDetail.objects.all()
    return render(request, "order_detail.html", {"order_detail":order_detail})

def show_order(request):
    order = Order.objects.all()
    return render(request, "order.html", {"order":order})

def show_dashboard(request):
    order = Order.objects.filter(order_date = date.today())
    total_city = City.objects.all().count()
    total_user = GamifyUser.objects.all().count()
    total_company = Company.objects.all().count()
    total_game = Game.objects.all().count()
    total_type = Type.objects.all().count()
    total_order = Order.objects.all().count()
    total_feedback = Feedback.objects.all().count()
    total_wishlist = Wishlist.objects.all().count()
    return render(request, "dashboard.html",
                  {"city":total_city, "user":total_user,
                   "games":total_game,"company":total_company,
                   "type":total_type, "feedback":total_feedback,
                   "order":total_order,"wishlist":total_wishlist,
                   "o":order})



def destroy_city(request, id):
    c = City.objects.get(city_id=id)
    c.delete()
    return redirect("/city")

def destroy_user(request, id):
    g = GamifyUser.objects.get(user_id=id)
    g.delete()
    return redirect("/user")

def destroy_company(request, id):
    c = Company.objects.get(company_id=id)
    c.delete()
    return redirect("/company")

def destroy_type(request, id):
    t = Type.objects.get(type_id=id)
    t.delete()
    return redirect("/type")

def destroy_game(request, id):
    g = Game.objects.get(game_id=id)
    g.delete()
    return redirect("/game")


# insert

def enter_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        print(f"Form Error = {form.errors}")

        if form.is_valid():
            try:
                form.save()
                return redirect('/city')

            except Exception as e:
                print("\n \n \n")
                print(f'Error = {sys.exc_info()}')
                print(f'Exception = {e}')

    else:
        form = City()
    return render(request, 'city_insert.html', {'form': form})


def enter_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        print(f"Form Error = {form.errors}")

        if form.is_valid():
            try:
                form.save()
                return redirect('/company')

            except Exception as e:
                print("\n \n \n")
                print(f'Error = {sys.exc_info()}')
                print(f'Exception = {e}')

    else:
        form = Company()

    return render(request, 'company_insert.html', {'form': form})



def enter_game(request):
    company = Company.objects.all()
    type_game = Type.objects.all()
    g = Game.objects.all()
    if request.method == "POST":
        form = GameForm(request.POST)
        print(f"Form Error = {form.errors}")

        if form.is_valid():
            availability = request.POST.get(
                'availability')  # Assuming 'availability' is the name attribute in your form
            # Update the availability based on user selection
            if availability == '0':
                g.available = False  # Set to Not available
            elif availability == '1':
                g.available = True  # Set to Available
            try:
                form.save()
                return redirect('/game')

            except Exception as e:
                print("\n \n \n")
                print(f'Error = {sys.exc_info()}')
                print(f'Exception = {e}')

    else:
        form = Game()
    return render(request, 'game_insert.html', {'form': form,'g':g,'company':company,'type':type_game})


def enter_type(request):
    if request.method == "POST":
        form = TypeForm(request.POST)
        print(f"Form Error = {form.errors}")

        if form.is_valid():
            try:
                form.save()
                return redirect('/type')

            except Exception as e:
                print("\n \n \n")
                print(f'Error = {sys.exc_info()}')
                print(f'Exception = {e}')

    else:
        form = Type()

    return render(request, 'type_insert.html', {'form': form})

# update

def change_city(request, id):
    c = City.objects.get(city_id=id)
    form = CityForm(request.POST, instance=c)
    if form.is_valid():
        form.save()
        return redirect("/city")
    return render(request, 'city_update.html', {'c': c})


def change_company(request, id):
    c = Company.objects.get(company_id=id)
    form = CompanyForm(request.POST, instance=c)
    if form.is_valid():
        form.save()
        return redirect("/company")
    return render(request, 'company_update.html', {'c': c})

# type

def change_game(request, id):
    company = Company.objects.all()
    type_game = Type.objects.all()
    g = Game.objects.get(game_id=id)
    year = g.game_launch_date.year
    month = g.game_launch_date.month
    day = g.game_launch_date.day
    date = f"{year}-{month}-{day}"
    form = GameForm(request.POST, instance=g)
    if form.is_valid():
        availability = request.POST.get('availability')  # Assuming 'availability' is the name attribute in your form
        # Update the availability based on user selection
        if availability == '0':
            g.available = False  # Set to Not available
        elif availability == '1':
            g.available = True  # Set to Available
        form.save()
        return redirect("/game")
    return render(request, 'game_update.html', {'g': g,'company':company,'type':type_game, 'date':date})


def change_type(request, id):
    t = Type.objects.get(type_id=id)
    form = TypeForm(request.POST, instance=t)
    if form.is_valid():
        form.save()
        return redirect("/type")
    return render(request, 'type_update.html', {'t': t})

def show_profile(request):
    user = GamifyUser.objects.all()
    return render(request,"profile.html",{'user':user})