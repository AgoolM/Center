from tokenize import group
from turtle import title
from unicodedata import category
from django.db import models


# Create your models here.

class Cuorse(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()
    price=models.PositiveIntegerField()
    lesson_qty = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Mentor(models.Model):
    GENDR = [
        ("Erkak","Erkak"),
        ("Ayol","Ayol"),
    ]
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=5, choices=GENDR, default="Erkak")
    birth_date = models.DateField()
    phone = models.CharField(max_length=13)
    passport = models.CharField(max_length=9)
    
    def __str__(self):
        return self.full_name


class Group(models.Model):
    title = models.CharField(max_length=60)
    cuorse = models.ForeignKey(Cuorse, on_delete=models.SET_NULL,blank=True, null=True )
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL,blank=True, null=True )
    group_qyt= models.PositiveIntegerField()

    def __str__(self):
        return self.title



class Mentee(models.Model):
    PAY=[
        ("PAYMENT","PAYMENT"),
        ("ANPAYMENT","ANPAYMENT")
    ]
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=13)
    passport = models.CharField(max_length=9)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,blank=True, null=True )
    payment = models.CharField(max_length=9, choices=PAY, default="ANPAYMENT")
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class VideoContent(models.Model):
    VIDEO_CATEGORY = [
        ("Logistic", "Logistic"), 
        ("Programing", "Programing"),
        ("Interesting", "Interesting"),
    ]
    LANGUAGE_CATEGORY = [
        ("Uzbek", "Uzbek"), 
        ("Russian", "Russian"),
        ("English", "English"),
    ]
    category = models.CharField(max_length=12, choices=VIDEO_CATEGORY, default="Interesting")
    language = models.CharField(max_length=8, choices=LANGUAGE_CATEGORY, default="Uzbek")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(max_length=500)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


