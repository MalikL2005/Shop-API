from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import UserForm
from .models import Shop_item, Cart
from .serializers import Shop_item_serializer

def index(req):
    return redirect('home')

def home(req):
    return render(req, 'home.html')

class view_shop_items(ListView):
    model = Shop_item
    template_name = "shop_item_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = Shop_item.objects.all()
        serialized_context = Shop_item_serializer(context, many=True).data
        return {'list': serialized_context}
    
class view_cart(ListView):
    model = Shop_item
    template_name = "cart.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = Shop_item.objects.all()
        serialized_context = Shop_item_serializer(context, many=True).data
        return {'list': serialized_context}

def sign_up(req): return render(req, 'sign_up.html', {'form': UserForm})

def view_cart(req):
    if req.user.is_authenticated:
        cart_items = Shop_item.objects.filter(user = req.user).all()


def validate_sign_up(req):
    if req.method == 'POST':
        print(req.POST)
        new_user = UserForm(req.POST)
        print(bool(new_user.is_valid()))
        if new_user.is_valid():
        # confirm via Email
        # make email the pk so sign-up is easier (only email + password)
            new_user.save()
            print('New User created')
            return redirect('/login')
        else: return HttpResponse("Could not create user")
