from django import forms

from main.models import Product, Version


class StyleForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForm, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        illegal_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                         'радар']
        for name in illegal_names:
            if name in cleaned_data.lower():
                raise forms.ValidationError(f"Недопустимое слово в названии: {name}")

            return cleaned_data


class VersionForm(StyleForm, forms.ModelForm):
    model = Version
    fields = '__all__'

    class Meta:
        model = Version
        fields = '__all__'
