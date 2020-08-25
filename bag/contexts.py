from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib import messages
from .views import remove_from_bag


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    items_to_remove = []

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        if quantity < product.stock:
            total += quantity * product.price
            product_count += quantity

            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

        else:
            total += product.stock * product.price
            product_count += product.stock

            if product.stock != 0:
                bag_items.append({
                    'item_id': item_id,
                    'quantity': product.stock,
                    'product': product,
                })
            else:
                messages.error(request,
                               f'{product.name} is now out of stock')
                items_to_remove.append(item_id)

    for item_id in items_to_remove:
        if item_id:
            print(item_id)
            remove_from_bag(request, item_id)
    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
