from django.shortcuts import render, redirect, get_object_or_404
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
        print(bag[item_id])
        if bag[item_id] > stock_level:
            bag[item_id] = stock_level

    request.session['bag'] = bag
    return redirect(redirect_url)
