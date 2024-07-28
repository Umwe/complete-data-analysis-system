from django.db import models

class Analysis(models.Model):
    file = models.FileField(upload_to='uploads/')
    result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
