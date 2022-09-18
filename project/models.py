from django.db import models


class Registered_mail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

