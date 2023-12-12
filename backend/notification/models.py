from django.db import models


class Notification(models.Model):


    type = models.CharField(max_length=255, blank=False, null=False)
    message = models.CharField(max_length=255, blank=False, null=False)
    relationship_key = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    class Meta:
        db_table = 'notifications_historic'
