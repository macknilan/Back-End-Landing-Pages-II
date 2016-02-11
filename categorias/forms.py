# -*- coding: utf-8 -*-

from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
    """
    FORMULARIO PARA MOSTRAR EN CONTACTO, VALIDA LOS CAMPOS,
    NO SE OCUPA UN MODELO PARA GUARDARLO EN BD
    """
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'max_length': 50, 'size': 50, 'class': 'validate', 'title': 'Nombre(s)/Titulo',
        'required': True}),  # 'placeholder': 'Nombre'
        validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Escribir solo letras en el campo de titulo')],
    )
    sender = forms.EmailField(widget=forms.EmailInput(attrs={
        'max_length': 50, 'size': 50, 'class': 'validate', 'title': 'Correo electrònico',
        'required': True,  # 'placeholder': 'Correo electrònico',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'title': 'Escribe aquì tus comentarios', 'rows': 10, 'cols': 10, 'required': True,
        'id': 'textarea1', 'class': 'materialize-textarea',  # 'placeholder': 'Escribe tus comentarios...',
    }))
