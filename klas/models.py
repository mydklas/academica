from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django import forms

choice_schedule = [
    ('Mon2', 'Mon 2pm-4pm'),
    ('Mon4', 'Mon 4pm-6pm'),
    ('Mon8', 'Mon 8pm-10pm'),
    ('Tue2', 'Tue 2pm-4pm'),
    ('Tue4', 'Tue 4pm-6pm'),
    ('Tue8', 'Tue 8pm-10pm'),
    ('Wed2', 'Wed 2p-4pm'),
    ('Wed4', 'Wed 4pm-6pm'),
    ('Wed8', 'Wed 8pm-10pm'),
    ('Thu2', 'Thu 2p-4pm'),
    ('Thu4', 'Thu 4pm-6pm'),
    ('Thu8', 'Thu 8pm-10pm'),
    ('Fri2', 'Fri 2p-4pm'),
    ('Fri4', 'Fri 4pm-6pm'),
    ('Fri8', 'Fri 8pm-10pm'),
    ]
choice_class = [
    ('8Beg', '8-12 Beginner'),
    ('8Int', '8-12 Intermediate'),
    ('13Be', '13-17 Beginner'),
    ('13In', '13-17 Intermediate'),
    ('13Ad', '13-17 Advance'),
    ]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, related_name="+", on_delete=models.CASCADE)
    image_post = models.ImageField(default="defaultpost.png", upload_to='post_pics')
    caption = models.CharField(default="Caption image", max_length=200)

    def __str__(self):
        return self.title, self.caption

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Booking(models.Model):
    #student = models.OneToOneField(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    klas = models.CharField(max_length=50)

    time_schedule = models.CharField(max_length=50)

    date_started = models.DateField()

    def __str__(self):
        return f'{self.fname,self.lname} Booking'

    # def save(self, *args, **kwargs):
    #     super(Booking, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('booking', kwargs={'pk': self.pk})
        # return reverse('booking', kwargs={'pk': self.pk})

class Text(models.Model):

    date_teks = models.DateField(default=timezone.now)
    image_teks = models.ImageField(default="defaulttext.jpg", upload_to='text_pics')
    caption_teks = models.CharField(default='Caption picture here',max_length=100)

    content_teks = models.TextField(max_length=1000)
    author_teks = models.ForeignKey(User, null=True, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_teks} content has been saved !'

    def get_absolute_url(self):
        # return reverse('text-home', kwargs={'pk': self.pk})
        return reverse('text-home',kwargs=None)