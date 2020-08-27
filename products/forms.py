from django import forms
from .models import Product, Category, Console

from collections import deque


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        cat_friendly_names = ([(c.id, c.get_friendly_name())
                              for c in categories])

        consoles = Console.objects.all()
        con_friendly_names = [(c.id, c.get_friendly_name()) for c in consoles]

        add_null = (None, '------')

        con_ammended_names = deque(con_friendly_names)
        con_ammended_names.appendleft(add_null)

        # change the category input to use friendly names from above
        self.fields['category'].choices = cat_friendly_names

        self.fields['console'].choices = con_ammended_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gray rounded'
