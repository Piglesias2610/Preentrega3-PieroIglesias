from django import forms

class curso_formulario(forms.Form):
    curso=forms.CharField()
    comision=forms.IntegerField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()