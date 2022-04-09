from django.shortcuts import render
from django.shortcuts import redirect
from django.http import request
from django.contrib.auth.decorators import login_required
from customers_profile.models import addressInfo
from customers_profile.models import profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files import File

@login_required
def customers_page(request):
    return render(request, 'customers_profile/customers_page.html')
@login_required
def change_image(request):
    return render(request, 'customers_profile/change_profile_image.html')
@login_required
def address_info_page(request, user_pk):
    addressvalues = addressInfo.objects.filter(user_address = user_pk).first()
    return render(request, 'customers_profile/address_info.html', {'addressvalues':addressvalues})

def login_req(request):
    return render(request, 'customers_profile/login_need.html')

def address_change_val(request, user_pk):
    if request.method=='POST':
        addressdetails = request.POST['addressdetails']
        city = request.POST['city']
        state = request.POST['state']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        receivername = request.POST['receivername']
        
        if len(addressdetails) > 1 and len(city)>1 and len(state)>1 and len(phone1)>1 and len(receivername)>1:
            address = addressInfo.objects.create(user_address = request.user, address_details = addressdetails, city = city, state = state,receiverName = receivername, phone1 = phone1, phone2 = phone2)
            address.save()
            messages.success(request, 'Successfully Added!')
            return redirect('address-info-page' ,user_pk)
        else:
            messages.warning(request,'All fields must contain more than one value')
            return redirect('address-info-page' ,user_pk)
    else:
        return render(request, 'customers/home_page.html')

def profile_update(request):
    if request.method == 'POST':
        get_img = request.FILES['get_profile_img']

        profile_obj = profile.objects.get(user = request.user)
        profile_obj.profile_image = get_img
        profile_obj.save()

        messages.success(request, 'Successfully Updated!    ')
        return redirect('profile-img-change')
    else:
        messages.warning(request, "Profile Not Changed!")
        return redirect('profile-img-change')

def update_address(request,user_pk):
    addressdetails = addressInfo.objects.filter(user_address = user_pk).first()
    return render(request, 'customers_profile/update_address_info.html',{'addressdetails':addressdetails})

def update_address_val(request,user_pk):
    if request.method == 'POST':
        addressdetails = request.POST['addressdetails']
        city = request.POST['city']
        state = request.POST['state']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        receivername = request.POST['receivername']

        address = addressInfo.objects.get(user_address = request.user)
        
        address.address_details = addressdetails
        address.city = city
        address.state = state
        address.receiverName = receivername
        address.phone1 = phone1
        address.phone2 = phone2

        address.save()
        messages.success(request, 'Successfully Updated! ')
        return redirect('address-info-page',user_pk)
    else:
        return render(request, 'customers/home_page.html')