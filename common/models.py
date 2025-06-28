from django.db import models
from django.utils.translation import gettext_lazy as _
class MediaFile(models.Model):
    file = models.FileField(upload_to='media_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MediaFile {self.id} - {self.file.name}"

    class Meta:
        verbose_name = 'Media File'
        verbose_name_plural = 'Media Files'
        ordering = ['-uploaded_at']
