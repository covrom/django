from django.db import models
from datetime import datetime, date

class Spectacle(models.Model):
    """Спектакли"""
    name = models.CharField("наименование", max_length=250, db_index=True)
    price = models.DecimalField("цена", max_digits=15, decimal_places=2)
    description = models.TextField("описание")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"

class Contact(models.Model):
    """Прокатчики"""
    name = models.CharField("имя", max_length=250, db_index=True)
    places = models.CharField("города", max_length=250, db_index=True)
    phones = models.CharField("телефоны", max_length=250, db_index=True)
    email = models.EmailField("email", max_length=250, db_index=True)
    requisites = models.TextField("реквизиты")
    comments = models.TextField("комментарии")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Прокатчик"
        verbose_name_plural = "Прокатчики"

class Events(models.Model):
    """События"""
    added = models.DateTimeField(db_index=True, auto_now_add=True)
    todate = models.DateField(db_index=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name="Прокатчик")
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE, verbose_name="Спектакль")
    comments = models.TextField("комментарии")

    def __str__(self):
        return '{0} '.format(self.added)+' '.join([self.contact.name, self.spectacle.name, self.comments.to_python().split('\n', 1)[0]])

    class Meta:
        ordering = ["-added"]
        verbose_name = "Событие"
        verbose_name_plural = "События"
        