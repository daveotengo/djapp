from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    #active = models.BooleanField(default=True)
  

    def get_absolute_url(self):
        return reverse("courses:course-detail",kwargs={"pk": self.id})#f"/products/self.id"