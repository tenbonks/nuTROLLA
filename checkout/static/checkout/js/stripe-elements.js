/*
    
    The core logic/payment flow in this file comes from:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here:
    https://stripe.com/docs/stripe-js

*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
  base: {
    color: '#32325d',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};

var card = elements.create('card', {
  style: style
});

card.mount('#card-element');

//  Handle realtime validiation errors on the card element
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `
      <span class="icon" role="alert">
        <i class="fas fa-times"></i>
      </span>
      <span>${event.error.message}</span>
      `;

    $(errorDiv).html(html);
  } else {
    errorDiv.textcontent = '';
  }
});

//  Handle form submit
var form = document.getElementById('payment-form');

/* 
  When the submit button is pressed, prevent form from submitting,
  instead it disables the card element and triggers loading overlay
*/
form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  card.update({
    'disabled': true
  });
  $('#submit-button').attr({
    'disabled': true
  });
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);

  // capture form data that can't be passed to payment intent right now
  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  // The element below is created from using {% csrf_token %}
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  // post the captured form data to the cache_checkout_data view
  $.post(url, postData).done(function () {
    // View updates payment intent, returns 200 response, call confirmCardPayment
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          email: $.trim(form.email.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            country: $.trim(form.country.value),
            state: $.trim(form.county.value),
          }
        }
      },
      shipping: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            country: $.trim(form.country.value),
            postal_code: $.trim(form.postcode.value),
            state: $.trim(form.county.value),
          }
      },

    }).then(function (result) {
      // If there is an error in form, hide loading overlay, re-enable the card element
      // and display tthe error to the user
      if (result.error) {
        var errorDiv = document.getElementById('card-errors');
        var html = `
        <span class="icon" role="alert">
          <i class="fas fa-times"></i>
        </span>
        <span>${result.error.message}</span>
        `;
        $(errorDiv).html(html);
        card.update({
          'disabled': false
        });
        $('#submit-button').attr({
          'disabled': false
        });
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
      } else {
        // If all is good, then submit the form
        if (result.paymentIntent.status === 'succeeded') {
          form.submit();
        }
      }
    });
  }).fail(function () {
    // If there is an error posting to the view, just reload page
    // error will be shown in django messages
    location.reload();
  });


});