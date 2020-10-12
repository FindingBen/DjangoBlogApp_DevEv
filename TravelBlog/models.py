from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Journey(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='journey_pics')


    def save(self):
        super().save()

        img = Image.open(self.image.path)
        #resizes the image
        if img.height > 600 or img.width > 600:
            output_size = (350, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)

    #prints out the object by its title, the str aka magic command
    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse('journey-detail',kwargs={'pk':self.pk})


