from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                       "Oops, there's nothing in your bag to checkout")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':
        'pk_test_51HHs1zLcwsQSSuynU2fk6ywqCzdqi4T4J7LFQgKTMDu8Yk\
            SQZ5SEXIJTWVZ8asvGK91kcQwiJGW59uAbCcpdIr4700O7qWieI8',
        'client_secret': 'placeholder text',
    }
    return render(request, template, context)
