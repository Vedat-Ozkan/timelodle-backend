from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    dob = models.IntegerField()
    # approx_birth = models.BooleanField()
    # birth_min = models.IntegerField()
    # birth_max = models.IntegerField()
    dod = models.IntegerField()
    # approx_death = models.BooleanField()
    # death_min = models.IntegerField()
    # death_max = models.IntegerField()
    gender = models.CharField(max_length=255)
    popularity = models.SmallIntegerField()
    occupation = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.name
    

