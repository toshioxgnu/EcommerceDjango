from carts.views import _cart_id
from .models import Cart, CartItem

def counter(request):
    cart_items_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if(request.user.is_authenticated):
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])

            for cart_item in cart_items:
                cart_items_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_items_count = 0
        return dict(cart_items_count=cart_items_count)
    