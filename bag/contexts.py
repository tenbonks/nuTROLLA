

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
