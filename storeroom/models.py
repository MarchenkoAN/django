from django.db import models

# Create your models here.
###
### Отдел
class Department(models.Model):
    department = models.CharField(max_length=5, name='Отдел', db_index=True)
    slug = models.SlugField(max_length=5)

    def __str__(self):
        return self.department

