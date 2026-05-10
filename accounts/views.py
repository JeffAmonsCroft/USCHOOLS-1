from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #checking if eamil already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    return render(request, 'signup.html')

def homepage_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# def password_reset_form_view(request):
#     return render(request, 'password_reset_form.html')

# def password_reset_done_view(request):
#     return render(request, 'password_reset_done.html')


















# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# #
# # from .models import PasswordResetToken

# # User = get_user_model()

# # Create your views here.
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         #checking if eamil already exists
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email is already registered.')
#             return redirect('signup')
        
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         messages.success(request, 'Account created successfully!')
#         return redirect('login')
#     return render(request, 'signup.html')

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         # user = authenticate(request, username=email, password=password)
#         try:
#             user = User.objects.get(email=email, password=password)
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect("home")
#         except User.DoesNotExist:
#             messages.error(request, "Invalid Credentials")
#     return render(request, "login.html")

            
#     #     if user is not None:
#     #         login(request, user)
#     #         return redirect('home')
#     #     else:
#     #         messages.error(request, 'Invalid Credentials')
#     # return render(request, 'login.html')



# def homepage_view(request):
#     return render(request, 'home.html')



# """function for sending emails"""
# # User = get_user_model()


def request_password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            email = email.strip().lower()
            try:
                user = User.objects.get(email__iexact=email)
                token = get_random_string(32)

                # Save token in DB
                PasswordResetToken.objects.create(user=user, token=token)

                reset_link = request.build_absolute_uri(
                    reverse("reset_password", args=[token])
                )

                send_mail(
                    subject="Password Reset Request",
                    message=f"Click the link to reset your password: {reset_link}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                )

                messages.success(request, "Password reset link sent to your email.")
                return redirect("login")

            except User.DoesNotExist:
                messages.error(request, "No account found with that email.")
        else:
            messages.error(request, "Please enter your email.")
    return render(request, "password_reset_form.html")

# """reset password function"""

def reset_password(request, token):
    try:
        reset_entry = PasswordResetToken.objects.get(token=token)
        user = reset_entry.user
    except PasswordResetToken.DoesNotExist:
        messages.error(request, "The reset link is invalid or has expired.")
        return redirect("request_password_reset")

    if request.method == "POST":
        new_password = request.POST.get("password")
        user.set_password(new_password)   # hashes securely
        user.save()
        reset_entry.delete()  # remove token after use
        messages.success(request, "Password reset successful. You can now log in.")
        return redirect("login")

        return render(request, "reset_password.html", {"validlink": True})

