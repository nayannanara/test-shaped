from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Patient(models.Model):
    name = models.CharField('Nome', max_length=100)
    age = models.IntegerField('Idade', validators=[
        MaxValueValidator(110),
        MinValueValidator(1)
    ])
    cep = models.CharField('CEP', null=True, max_length=11)
    address = models.CharField('Logradouro', null=True, blank=True, max_length=40)
    number = models.CharField('Numero', null=True, max_length=10)
    complement = models.CharField('Complemento', null=True, blank=True, max_length=60)
    district = models.CharField('Bairro', max_length=40)
    state = models.CharField('Estado', max_length=26)
    city = models.CharField('Cidade', max_length=30)

    def __str__(self):
        return self.name


class Exam(models.Model):
    professional = models.CharField('Profissional', max_length=100)
    exam_date = models.DateField(auto_now_add=True)
    weight = models.FloatField('Peso')
    height = models.FloatField('Altura')
    patient = models.ForeignKey(
        Patient,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'{self.professional, {self.patient.name}, {self.exam_date}}'