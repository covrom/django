from django.db import models
from datetime import datetime, date

class Spectacle(models.Model):
    """Спектакли"""
    name = models.CharField("наименование", max_length=250, db_index=True)
    price = models.DecimalField("цена", max_digits=15, decimal_places=2, blank=True)
    description = models.TextField("описание", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"

class Contact(models.Model):
    """Прокатчики"""
    name = models.CharField("имя", max_length=250, db_index=True)
    places = models.CharField("города", max_length=250, db_index=True, blank=True)
    phones = models.CharField("телефоны", max_length=250, db_index=True, blank=True)
    email = models.EmailField("email", max_length=250, db_index=True, blank=True)
    requisites = models.TextField("реквизиты", blank=True)
    comments = models.TextField("комментарии", blank=True)
    lastevent = models.CharField("последнее событие", max_length=250, db_index=True, blank=True, editable=False)

    def get_lastevent(self):
        evset = '\n'.join([str(i) for i in self.events_set.order_by('-id')[:1]])
        return evset

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.lastevent = self.get_lastevent()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Прокатчик"
        verbose_name_plural = "Прокатчики"
    


class Events(models.Model):
    """События"""
    added = models.DateTimeField("добавлено", db_index=True, auto_now_add=True)
    reminder_date = models.DateField("дата напоминания", db_index=True, blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name="Прокатчик")
    spectacle = models.ForeignKey(Spectacle, on_delete=models.CASCADE, verbose_name="Спектакль")
    spectacle_date = models.DateField("дата спектакля", db_index=True, blank=True, null=True)
    comments = models.TextField("комментарии", blank=True)

    def __str__(self):
        return '{0:%Y-%m-%d %H:%M} {1}'.format(self.added,self.comments.split('\n', 1)[0])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #теперь обновим контакт
        self.contact.save()

    class Meta:
        ordering = ["-id"]
        verbose_name = "Событие"
        verbose_name_plural = "События"
        