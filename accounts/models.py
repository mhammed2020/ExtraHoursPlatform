from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import activate, ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# slug
from django.utils.text import slugify


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User ,verbose_name =_("user")  , on_delete=models.CASCADE)
    name = models.CharField(("الاسم :"), max_length = 60)
    who_i = models.TextField((" من انا : "), max_length = 200)
    image = models.ImageField(_("صورة  شخصية "), upload_to='profile/',blank=True, null=True)
    price = models.IntegerField((" سعر الكشف "),default=10, null=True)
    phone_number = models.CharField(max_length=45,null=True , blank=True)
    address = models.CharField(max_length=100 , blank=True, null=True)
  
    #slug
    slug = models.SlugField(_("slug"),blank=True, null=True)
   
   #slugify
    def save(self,*args,**kwargs):
        #logic
        self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


    def __str__(self):
        return str(self.user)




@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )