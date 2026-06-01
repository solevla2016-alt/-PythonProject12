from django import forms
from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

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

    def clean_name(self):

        name = self.cleaned_data["name"]

        for word in FORBIDDEN_WORDS:

            if word.lower() in name.lower():

                raise forms.ValidationError(
                    f'Слово "{word}" запрещено'
                )

        return name

    def clean_description(self):

        description = self.cleaned_data["description"]

        if description:

            for word in FORBIDDEN_WORDS:

                if word.lower() in description.lower():
                    raise forms.ValidationError(
                        f'Слово "{word}" запрещено'
                    )

        return description

    def clean_photo(self):

        photo = self.cleaned_data.get("photo")

        if not photo:
            return photo

        # Проверка размера файла
        if photo.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "Размер изображения не должен превышать 5 МБ."
            )

        # Проверяем тип только для нового загружаемого файла
        if hasattr(photo, "content_type"):

            allowed_types = [
                "image/jpeg",
                "image/png",
            ]

            if photo.content_type not in allowed_types:
                raise forms.ValidationError(
                    "Разрешены только изображения JPG и PNG."
                )

        return photo


