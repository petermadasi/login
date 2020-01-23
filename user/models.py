from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # custom fields for user
    phone= models.CharField(null=False,max_length=250)
    address=models.CharField(max_length=250)  

    def _self_(self):
        return self.phone  