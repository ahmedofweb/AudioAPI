from django.db import models

class Topic(models.Model):
    nom = models.CharField(max_length=100)
    qoshilgan_sana = models.DateField()
    def __str__(self):
        return self.nom

class Suhbat(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sarlavha = models.CharField(max_length=50)
    fayl = models.FileField()
    davomiylik = models.CharField(max_length=50, null=True, blank=True)
    hajm = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.sarlavha

