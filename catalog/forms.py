from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    error_word = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = Product
        exclude = ('viewed',)

    def clean_name(self):

        name = self.cleaned_data['name']

        if name.lower() in self.error_word:
            raise forms.ValidationError('Запрещенные слова')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']

        if description.lower() in self.error_word:
            raise forms.ValidationError('Запрещенные слова')
        return description
