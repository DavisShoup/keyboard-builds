from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Keyboard(models.Model):
  name = models.CharField(max_length=100)
  keyboard = models.CharField(max_length=100)
  switch = models.CharField(max_length=100)
  keycaps = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'keyboard_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for keyboard_id: {self.keyboard_id} @{self.url}"



## FILLER DATA BELOW
# keyboards = [
#   Keyboard('budget friendly', 'g413', 'red', 'GMK Alpaca'),
#   Keyboard('TKL lovers dream', 'GMMK pro', 'black inks', 'ePBT keycaps'),
#   Keyboard('Out of the box banger', 'Razer Huntman', 'blue', 'Razer keycaps')
# ]



