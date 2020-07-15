from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=255)
    author = models.TextField(max_length=255)
    isbn = models.CharField(max_length=13)
    publish_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    borrowedbook = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.TextField(max_length=255, blank=False)
    borrowdate = models.DateTimeField(verbose_name="date borrowed",default=datetime.now(),blank=False)
    returndate = models.DateTimeField(verbose_name="date returned",null=True, blank=True)
    expiryduration = models.CharField(max_length=2, default=14)

    def __str__(self):
        return f"{self.borrowedbook} - {self.borrower}"

    def get_borrow_expiry(self):
        return self.borrowdate.date() + timedelta(days=int(self.expiryduration))