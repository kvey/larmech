from django.db import models

# Create your models here.
class CreatedModifiedModel(models.Model):
    class Meta:
        abstract = True
    created  = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class PartListing(CreatedModifiedModel):
    part_type = models.TextField(null=True, blank=True)
    part_number = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
