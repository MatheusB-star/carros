from django import forms
from cars import models as md


class carroForm(forms.Form):
    modelo = forms.CharField(max_length=200)
    marca = forms.ModelChoiceField(md.marca.objects.all())
    ano_fabricacao = forms.IntegerField()
    ano_modelo = forms.IntegerField()
    placa = forms.CharField(max_length=10)
    valor = forms.FloatField()
    carro_foto = forms.ImageField()


    def salvar(self):
        carro = md.carro(
            modelo = self.cleaned_data['modelo'],
            marca = self.cleaned_data['marca'],
            ano_fabricacao = self.cleaned_data['ano_fabricacao'],
            ano_modelo = self.cleaned_data['ano_modelo'],
            placa = self.cleaned_data['placa'],
            valor = self.cleaned_data['valor'],
            carro_foto = self.cleaned_data['carro_foto'],
        )

        carro.save()
        return carro


class carromodelform(forms.ModelForm):
    
    class Meta:
        model = md.carro
        fields = '__all__'



    def clean_ano_fabricacao(self):
        ano_fabricacao = self.cleaned_data.get('ano_fabricacao')


        if not ano_fabricacao:
            self.add_error('ano_fabricacao', 'O ano de fabricação deve ser informado')
        else:
            if ano_fabricacao < 2000:
                self.add_error('ano_fabricacao', 'O ano deve ser maior ou igual a 2000')
        return ano_fabricacao
    


    def clean_valor(self):
        valor = self.cleaned_data.get('valor')

        if not valor:
            self.add_error('valor', 'O valor do carro deve ser informado')
        else:

            if valor < 20000:
                self.add_error('valor', 'O valor de venda não pode ser inferior a R$20.000 reais')

        return valor


