from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    weight = models.IntegerField()
    primary_type = models.CharField(max_length=100)
    secondary_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
    
