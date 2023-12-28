from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__' # ['first_name', 'last_name', 'email']
        # exclude = ('first_name',)
        labels = {
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email'),
        }
        # help_texts = {'email': _('Valid email only!')}
        error_messages = {
            'first_name': {
                'required': _('First name is required')
            }
        } 
    
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError('Invalid name')
    #     return data
    
    # def validate_comma(value):
    #     if ',' in value:
    #         raise forms.ValidationError('Invalid')
    #     return value
    
    # first_name = forms.CharField(max_length=100, validators=[validate_comma])
    # last_name = forms.CharField(max_length=100, label='First Name', required=False)
    # email = forms.EmailField(max_length=100, help_text='Valid email only!')
    