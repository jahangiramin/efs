from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.

class Company(models.Model):
    name = CharField(max_length=200)
    slug = CharField(max_length=50)

class Period(models.Model):
    name = CharField(max_length=200)
    slug = CharField(max_length=50)
    company = ForeignKey(Company, on_delete=CASCADE)

class Statement(models.Model):
    name = CharField(max_length=200)
    alias = CharField(max_length=50)
    noteref = CharField(max_length=20)
    period = ForeignKey(Period, on_delete=CASCADE)

class FSLI(models.Model):
    name = CharField(max_length=200)

class POV(models.Model):
    name = CharField(max_length=200)

class Grouping(models.Model):
    name = CharField(max_length=200)

class BalanceType(models.Model):
    #Trial balance, manual input, working etc
    name = CharField(max_length=200)

class Balance(models.Model):
    name = CharField(max_length=200)
    type = ForeignKey(BalanceType, on_delete=CASCADE)
    value = IntegerField()
    grouping = ManyToManyField(Grouping)

class Amount(models.Model):
    statement = ForeignKey(Statement, on_delete=CASCADE)
    fsli = ForeignKey(FSLI, on_delete=CASCADE)
    pov = ForeignKey(POV, on_delete=CASCADE)
    amount = ForeignKey(Grouping, on_delete=CASCADE)