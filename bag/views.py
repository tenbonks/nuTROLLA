from django.shortcuts import (render, redirect, get_object_or_404,
                              reverse, HttpResponse)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of a specific product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)
    stock_level = product.stock

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        if bag[item_id] > stock_level:
            bag[item_id] = stock_level
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')
        if bag[item_id] > stock_level:
            bag[item_id] = stock_level

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of a specified product, to the specified amount """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)
    stock_level = product.stock

    if quantity > 0:
        bag[item_id] = quantity
        if bag[item_id] > stock_level:
            bag[item_id] = stock_level
    else:

        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the bag """

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
