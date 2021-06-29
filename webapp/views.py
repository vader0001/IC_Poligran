from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Item, Order, OrderItem


class OrderListView(ListView):

    model = Order
    paginate_by = 100  # if pagination is desired

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

class ItemListView(ListView):

    model = Item
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        category = self.request.GET.get('category', '')
        if category == 'product':
            category = 'Productos'
        elif category == 'service':
            category = 'Servicios'
        else:
            category = ''
        context['category'] = category
        return context

    def get_queryset(self):
        category = self.request.GET.get('category', '')
        if category == 'product':
            category = 'product'
        elif category == 'service':
            category = 'service'
        else:
            category = ''
        if category:
            print('category', category)
            return Item.objects.filter(
                Item_type=category
            )
        return Item.objects.all()

class ItemDetailView(DetailView):

    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['category'] = self.object.categoria
        return context

def welcome(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    return redirect('/login')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')


    return render(request, "login.html", {'form': form})

def logout(request):
    do_logout(request)
    return redirect('/')


def OrderItemView(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        room = request.POST.get('room')
        item = OrderItem(item=item, quantity=quantity)
        item.save()
        order = Order(customer=request.user, room_number=room, item=item)
        order.save()
        return redirect('/order/' + str(order.id))
    return render(request, 'webapp/item_order.html', {'item': item})

class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
