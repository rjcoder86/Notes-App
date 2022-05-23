import datetime

from django.db import models

# Create your models here.

COLOR_CHOICES = (
    ('#11998e, #38ef7d','GREEN'),
    ('#4e54c8, #8f94fb', 'BLUE'),
    ('#ed213a, #93291e','RED'),
    ('#fdc830, #f37335','ORANGE'),
    ('#2193b0, #6dd5ed','SKY BLUE'),
    ('#bc4e9c, #f80759','PINK'),
)

class Note(models.Model):
    title=models.CharField(max_length=30)
    text=models.TextField()
    date=models.DateField(default=datetime.datetime.now().date())
    color=models.CharField(max_length=30,choices=COLOR_CHOICES)

    def save(self, *args, **kwargs):
        if self.date:
            self.date = datetime.datetime.now().date()
        super(Note, self).save(*args, **kwargs)