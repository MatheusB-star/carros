from contas.models import usuario
from django import forms

class usuario_form(forms.ModelForm):

    class Meta:
        model = usuario
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        cpf = self.cleaned_data.get('usuario_cpf')
        nome = self.cleaned_data.get('usuario_nome')
        senha = self.cleaned_data.get('usuario_senha')
        
        if not cpf:
            self.add_error('usuario_cpf', 'O CPF do usuário deve ser informado')
        else:
            if len(cpf) < 2:
                self.add_error('usuario_cpf', 'O CPF deve conter 2 ou mais caracteres')

        if not nome:
            self.add_error('usuario_nome', 'O nome do usuário deve ser informado')
        else:
            if len(nome) < 4:
                self.add_error('usuario_nome', 'O nome deve conter 4 ou mais caracteres')

        if not senha:
            self.add_error('usuario_senha', 'A senha do usuário deve ser informada')
        else:
            if len(senha) < 3:
                self.add_error('usuario_senha', 'A senha deve conter 3 ou mais caracteres')

            if not any(char.isdigit() for char in senha):
                self.add_error('usuario_senha', 'A senha deve conter pelo menos um número')

        return cleaned_data
