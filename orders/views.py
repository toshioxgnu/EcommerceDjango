
import django.http
from django.shortcuts import redirect, render
from carts.models import CartItem
from orders.forms import OrderForm
import datetime
from .models import Order

# Create your views here.

def payments(request):
    return render(request, 'orders/payments.html')

def place_order(request, total=0, quantity=0):

    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)

    if (cart_items.count() <= 0):
        return redirect('store')
    
    grand_total = 0
    tax = 0

    for cartItem in cart_items:
        total = (cartItem.product.product_price * cartItem.quantity)
        quantity += cartItem.quantity
        grand_total += total

    tax = grand_total * 0.19
    grand_total = grand_total+tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.address2 = form.cleaned_data['address2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.ip = request.META.get('REMOTE_ADDR')
            data.tax= tax
            data.order_total = grand_total
            data.save()

            # Generate order number
            year = int(datetime.date.today().strftime('%Y'))
            month = int(datetime.date.today().strftime('%m'))
            day = int(datetime.date.today().strftime('%d'))
            date = datetime.date(year, month, day)
            current_date = date.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order' : order,
                'cart_items': cart_items,
                'total': total,
                'tax' : tax,
                'grand_total': grand_total,
            }

            # Order Complete
            return render(request, 'orders/payments.html', context=context)
    else:
        return redirect('checkout')
