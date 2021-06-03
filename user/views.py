from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.
def loginform(request):
    if request.method =='POST':
        username=request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username, password=password)
        if user is not  None:
            login(request, user)
            return redirect('user:home')
        else:
            return render(request, 'user/login.html')
        return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')
def registeruser(request):
    if request.method =='POST':
        firstname=request.POST['firstname']
        secondname = request.POST['secondname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        identity = request.POST['id_no']
        phone = request.POST['phone']

        try:
            newuser=User.objects.create_user(username=username, email=email, password=password)
            newuser.profile.firstname=firstname
            newuser.profile.secondname = secondname
            newuser.profile.phone = phone
            newuser.profile.identityno = identity
            newuser.save()
            return render(request, 'user/login.html')
        except:
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')

@login_required()
def home(request):
    items = item.objects.all()
    return render(request, 'user/home.html', {'items':items})

@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=User.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_email(request):
    email=request.POST.get("email")
    email_obj=User.objects.filter(email=email).exists()
    if email_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def checkdetails(request):
    username=request.POST.get("username")
    user_obj=User.objects.filter(username=username).exists()

    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

# update user details
@login_required()
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('user:home')

    def get_object(self, queryset=None):
        return self.request.user

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserEditView, self).dispatch(*args, **kwargs)



def logout_request(request):
    logout(request)
    return redirect("user:login")

@login_required()
def additem(request):
    if request.method=='POST':
        item_name=request.POST.get('item_name')
        description=request.POST.get('description')
        item_image=request.FILES.get('item_image')
        category = request.POST.get('category')
        username=request.POST.get('username')
        start_price = request.POST.get('starting_price')

        items=item(item_name=item_name, description=description, item_image=item_image, category=category, item_price=start_price)
        items.user = request.user
        items.save()
        try:
            items.save()
            current_user = request.user.profile
            messages.success(request, "Item added Successfully!")
            return render(request,'user/additem.html', {'cuser':current_user})
        except:
            current_user=request.user.profile
            return render(request,'user/additem.html', {'cuser':current_user})
    else:
        current_user = request.user.profile
        return render(request, 'user/additem.html',{'cuser':current_user})

@login_required()
def viewitems(request):
    myitems=item.objects.filter(user=request.user)
    return render(request, 'user/viewitems.html', {'myitems':myitems})

def interested(request,pk):
    current_item= item.objects.filter(id=pk)
    return render(request, 'user/interested.html', {'item': current_item})