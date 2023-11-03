from django.db import models

# Create your models here.


class Owner(models.Model):
    """Owner object"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.TextField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=25)
    created_at = models.DateField(auto_now=True)


class Pet(models.Model):
    """Pets object"""

    class Species(models.IntegerChoices):
        CAT = 1
        DOG = 2
        BIRD = 3

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")
    age = models.IntegerField()
    species = models.IntegerField(choices=Species.choices)
    created_at = models.DateField(auto_now=True)
    # When you include a string instead of the class
    # You'll lazy get the relationship


class Record(models.Model):
    """Record entity"""

    class Category(models.IntegerChoices):
        OTHER = 0
        BLOOD_PRESSURE = 1
        BLOOD_SUGAR = 2
        BLOOD_OXYGEN = 3
        VACCINATION = 4

    category = models.IntegerField(choices=Category.choices)
    procedure = models.CharField(max_length=255)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="records")
    date = models.DateField()
