# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, BooleanField
from wtforms import SelectField, FormField, FieldList
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'

class UczenForm(FlaskForm):
    id = HiddenField("")
    imie = StringField("Imie")
    nazwisko = StringField("Nazwisko")


class KlasaForm(FlaskForm):
    id = HiddenField("klasa id")
    klasa = StringField("Numer klasy:")
    rok_naboru






