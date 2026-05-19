from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = (
            "name",
            "description",
            "photo",
            "category",
            "price",
        )

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }