from django.forms import ModelForm
from accounts.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
