from django.db import models

# Средства разработки
class IDE(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# Языки программирования
class Lang(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()
    IDE_id = models.ForeignKey(IDE, on_delete=models.CASCADE)
    def __str__(self):
        return self.name