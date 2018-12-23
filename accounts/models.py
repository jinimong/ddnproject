from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.mail import send_mail

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)
        
        # send mail
        send_mail(
            '반갑습니다.',
            '회원이 된 걸 환영합니다.',
            'contact@datadriven.kr',
            [user.email],
            fail_silently = False,
        )

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
