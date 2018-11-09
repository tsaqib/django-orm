from django.db import models


class Subscriber(models.Model):
    name = models.TextField()
    email = models.TextField()

    class Meta:
        db_table = 'subscribers'
