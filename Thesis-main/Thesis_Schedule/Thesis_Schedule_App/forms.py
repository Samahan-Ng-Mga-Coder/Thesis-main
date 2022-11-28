from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ('id_number', 'first_name', 'last_name', 'suffix_name', 'address', 'phone_number', 'birthday', 'rank', 'age', 'status', 'email', 'username', 'password')
        labels = {
            'id_number': ' ID Number',
            'first_name' : 'First Name'
        }
    def __init__(self, *args, **kwargs):
        super(ProfessorForm,self).__init__(*args, **kwargs)
        self.fields['rank'].empty_label = "Select"