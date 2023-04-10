from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForms
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import OrderItem
from django.contrib import messages



@login_required
def order_datail_view(request):
    order_form = OrderForms()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request,'سبد شما خالی است')
        return redirect('product_detail')
    if request.method == 'POST':
        order_form = OrderForms(request.POST,)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,

                    )
            cart.clear()
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            messages.success(request, 'سفارش شما با موفقیت ثبت شد')
    return render(request, 'orders/order_detail.html', {'form':order_form, })