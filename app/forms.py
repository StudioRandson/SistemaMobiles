from django.forms import ModelForm
from app.models import usuario

# Create the form class.
class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['matricula', 'nome', 'setor', 'funcao','mobile','caf','armario','chave']

