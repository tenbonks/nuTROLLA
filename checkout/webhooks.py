from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Not used just yet, but will be needed
from checkout.webhook_handler import stripeWH_Handler

import json
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """  Listen for webhooks from stripe """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Webhook handler setup
    handler = stripeWH_Handler(request)

    # Map WH events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Get the webhook from stripe
    event_type = event['type']

    # If there isn't a handler for it, get it from event map
    # Use generic by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
