from django.db import models

class ActivityLog(models.Model):
    ip_address = models.GenericIPAddressField()
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} visited {self.url} at {self.timestamp}"

