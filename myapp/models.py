from django.db import models

class TimestampRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    region = models.IntegerField(default=1)

    def __str__(self):
        return str(self.timestamp)

