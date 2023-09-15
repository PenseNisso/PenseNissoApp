from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('ReportCategory', on_delete=models.SET_NULL, null=True)
    links = models.TextField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    user = models.ForeignKey('User',on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
