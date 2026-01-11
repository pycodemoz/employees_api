from django.db import models
from units.models import Unit


GENDER_CHOICES = (("M", "Masculino"), ("F", "Feminino"))

ACADEMIC_LEVELS = (
    ("ENSINO_BASICO", "Ensino Básico"),
    ("ENSINO_SECUNDARIO", "Ensino Secundário"),
    ("ENSINO_MEDIO", "Ensino Médio / Técnico Profissional"),
    ("LICENCIATURA", "Licenciatura"),
    ("POS_GRADUACAO", "Pós-Graduação"),
    ("MESTRADO", "Mestrado"),
    ("DOUTORAMENTO", "Doutoramento"),
)


CATEGORY_CHOICES = (
    ("Comissário Geral Tributário", "Comissário Geral Tributário"),
    ("Comissário Tributário", "Comissário Tributário"),
    ("Sub-Comissário Tributário", "Sub-Comissário Tributário"),
    ("Superintendente Tributário", "Superintendente Tributário"),
    ("Inspector Tributário", "Inspector Tributário"),
    ("Sub-Inspector Tributário", "Sub-Inspector Tributário"),
    ("Técnico Tributário de 1ª Classe", "Técnico Tributário de 1ª Classe"),
    ("Técnico Tributário de 2ª Classe", "Técnico Tributário de 2ª Classe"),
    ("Auxiliar Tributário de 1ª Classe", "Auxiliar Tributário de 1ª Classe"),
    ("Auxiliar Tributário de 2ª Classe", "Auxiliar Tributário de 2ª Classe"),
    ("Auxiliar Tributário de 3ª Classe", "Auxiliar Tributário de 3ª Classe"),
)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    academic_level = models.CharField(max_length=100, choices=ACADEMIC_LEVELS)
    course = models.CharField(max_length=100, null=True, blank=True)
    id_number = models.CharField(max_length=4, unique=True)
    tax_number = models.CharField(max_length=9, unique=True)
    employee_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    entry_date = models.DateField(null=True, blank=True)
    place_of_work = models.ForeignKey(
        Unit, on_delete=models.SET_NULL, related_name="employee", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
