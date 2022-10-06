from djangoimport forms
from forms import ModelForm
from .models import Quote

class QuoteForm(ModelForm):
    
    required_css_class = 'required'

    class Meta:
        Model = Quote
        fields = [
                 'name', 'position', 'company', 'address',
                 'phone', 'email', 'web', 'description',
                 'sitestatus', 'priority', 'jobfile'
                 ]


