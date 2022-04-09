from PIL.Image import ID
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from products.models import category,product
from order.models import OrderItem,Order

# Create your views here.
def home(request):
    product_obj = product.objects.all()
    top_sales = product.objects.filter(top_sale = True)
    content = {
        'product_obj':product_obj,
        'top_sales':top_sales
    }
    return render(request, 'customers/home_page.html',content)

def register_page(request):
    return render(request, 'customers/register_page.html')

def register_form(request):
    if request.method == 'POST':
        register_username = request.POST['register-username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        register_email = request.POST['register-email']
        register_password = request.POST['register-password']
        register_password2 = request.POST['register-password2']

        if register_password == register_password2:
            if User.objects.filter(username = register_username).exists():
                messages.warning(request, "Username already exists!")
                return redirect('register-page')
            else:
                if User.objects.filter(email = register_email).exists():
                    messages.warning(request, "Email is already used by a user!")
                    return redirect('register-page')
                else:
                    #registration process
                    user_info = User.objects.create_user(username = register_username, first_name = firstname, last_name=lastname, email = register_email, password = register_password)
                    user_info.save()
                    messages.success(request, "You have been registered.")
                    return redirect('login-page')
        else:
            messages.warning(request,'passwords dont match!')
            return redirect('register-page')
        
    else:
        return render(request, 'customers/home_page.html')

def login_page(request):
    return render(request, 'customers/login_page.html')

def login_form(request):
    if request.method == "POST":
        login_username = request.POST["username"]
        login_password = request.POST["password"]

        user = auth.authenticate(username = login_username, password = login_password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect('customer-page')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login-page')
    else:
        messages.warning(request, "Sorry, Login Failed.(^_^)")
        return render(request,'customers/login_page.html')

def logout_control(request):
    auth.logout(request)
    messages.success(request,"You are logged out!")
    return redirect('login-page')

#SEARCH FUNCTIONALITIES
def serach_for_product(request):
    if request.method == "POST":
        search_value = request.POST["search-value"]
        result = product.objects.filter(product_name__icontains = search_value)
        content = {
            "result":result,
            "word":search_value
        }
        return render(request, 'customers/search_result.html',content)
    else:
        return redirect('home-page')

def search_by_category(request):
    if request.method == "POST":
        category_value = request.POST['category-value']
        try:
            categories = category.objects.filter(category_name = category_value).first().id
            result = product.objects.filter(product_category = categories)
        except:
            return redirect("home-page")
        content = {
            "result":result,
            "word":category_value
        }
        return render(request, 'customers/search_category.html',content)
    else:
        return redirect("home-page")