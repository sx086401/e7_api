from django.db import models
from .characters import Characters
from .state_details import StateDetails

class States(models.Model):
    character = models.ForeignKey(Characters, on_delete=models.SET_NULL, null=True)
    current_state = models.ForeignKey(StateDetails, on_delete=models.SET_NULL, null=True, related_name='current_state')
    expect_state = models.ForeignKey(StateDetails, on_delete=models.SET_NULL, null=True, related_name='expect_state')
    editor = models.CharField(max_length=50, null=True, blank=True)
