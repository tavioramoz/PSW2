from django.forms import ModelForm
from .models import aluno

class AlunoForm(ModelForm):
    
    class Meta:
        model = aluno
        fields = '__all__'