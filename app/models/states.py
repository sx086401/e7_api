from django.utils import timezone
from django.db import models
from .characters import Characters
from .state_details import StateDetails

class States(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.SET_NULL, null=True)
    current_state = models.ForeignKey(StateDetails, on_delete=models.SET_NULL, null=True, related_name='current_state')
    expect_state = models.ForeignKey(StateDetails, on_delete=models.SET_NULL, null=True, related_name='expect_state')
    editor = models.CharField(max_length=50, null=True, blank=True)
    artifact1 = models.CharField(max_length=20, null=True, blank=True)
    artifact2 = models.CharField(max_length=20, null=True, blank=True)
    artifact3 = models.CharField(max_length=20, null=True, blank=True)
    exclusive_equipment = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

