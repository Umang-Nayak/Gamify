import sys
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from Gamify import settings
from Gamify_Admin.forms import GamifyUserForm
from Gamify_Admin.models import City, GamifyUser
from django.contrib import messages
import random


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
            return redirect('/home/')
        else:
            messages.error(request, "Invalid Username or Password !!!")
            return redirect('/admin_register/')
    else:
        return render(request, "admin_Register_Login.html")


def sendotp(request):
    otp1 = random.randint(10000, 99999)

    e = request.POST['fp_email']
    request.session['session_email'] = e

    obj = GamifyUser.objects.filter(u_email=e).count()

    if obj == 1:

        GamifyUser.objects.filter(u_email=e).update(otp=otp1, otp_used=0)
        subject = 'OTP Verification'
        message = str(f"{otp1} is your OTP to access calculator. "
                      f"\nFor security reasons, DO NOT share this OTP with anyone.")
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'Otp.html')

    else:
        messages.error(request, "Invalid Email !!!")
        return render(request, "Forgot_Password.html")


def set_password(request):
    if request.method == "POST":

        email_otp = request.POST['u_otp']
        new_password = request.POST['u_new_password']
        confirm_cpass = request.POST['u_confirm_password']

        if new_password == confirm_cpass:

            e = request.session['session_email']
            val = GamifyUser.objects.filter(u_email=e, otp=email_otp, otp_used=0).count()

            if val == 1:
                GamifyUser.objects.filter(u_email=e).update(otp_used=1, u_password=new_password)
                return redirect("/user_Signin_Signup")
            else:
                messages.error(request, "Invalid OTP !!!")
                return render(request, "Otp.html")

        else:
            messages.error(request, "New password and Confirm password does not match !!!")
            return render(request, "Otp.html")

    else:
        return redirect("/forgot_password")


def main(request):
    return render(request, "admin_home.html")
