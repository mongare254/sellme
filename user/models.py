from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50, null=True)
    secondname=models.CharField(max_length=50, null=True)
    identityno=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    profile_image=models.ImageField(upload_to='profilepics', blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class item(models.Model):
    item_name=models.CharField(max_length=50)
    item_price=models.FloatField()
    item_image=models.ImageField(upload_to='images/', blank=True)
    description=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    approval_status=models.CharField(max_length=50, default="Waiting")
    auction_status=models.CharField(max_length=50, default="Scheduled")
    date_added=models.DateTimeField(auto_now=True)
    category=models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.item_name

class Payment(models.Model):
    payment_code=models.CharField(max_length=50)
    item=models.ForeignKey(item, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type=models.CharField(max_length=50)

class returned_item(models.Model):
    item=models.ForeignKey(item,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date_returned=models.DateTimeField(auto_now=True)
    reason=models.TextField()
    seller=models.CharField( max_length=50)

class bidder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    bidder_price=models.FloatField()
    date_bid=models.DateTimeField(auto_now=True)

class sold_item(models.Model):
    item_id=models.ForeignKey(item, on_delete=models.CASCADE)
    buyer=models.CharField(max_length=100)
    seller=models.CharField(max_length=100)

class chats(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.CharField(max_length=1000, default="My Message")

class interested(models.Model):
    username=models.CharField(max_length=50, blank=True)
    item_name=models.CharField(max_length=50, blank=True)
    amount_paid=models.IntegerField(blank=True, default="500")

    def __str__(self):
        return self.username +" " +self.item_name


