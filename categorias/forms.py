# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    """
    FORMULARIO PARA MOSTRAR EN CONTACTO, VALIDA LOS CAMPOS, NO SE OCUPA UN MODELO PARA GUARDARLO EN BD
    """
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'max_length': 50, 'size': 50, 'class': 'name plain buffer', 'title': 'Nombre(s)/Titulo',
        'placeholder': 'Nombre', 'required': True}),
        validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Escribir solo letras en el campo de titulo')],
    )
    sender = forms.EmailField(widget=forms.EmailInput(attrs={
        'max_length': 50, 'size': 50, 'class': 'name plain buffer', 'title': 'Correo electrònico',
        'placeholder': 'Correo electrònico', 'required': True,
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Escribe tus comentarios...', 'title': 'Escribe aquì tus comentarios',
        'rows': 10, 'cols': 10, 'required': True,
    }))
