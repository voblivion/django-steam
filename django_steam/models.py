from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_openid_auth.models import UserOpenID
from django_steam_api.models import Player
from django.conf import settings
import re


class UserSteam(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='steam')
    player = models.OneToOneField(Player, related_name='steam')


@receiver(post_save, sender=UserOpenID, dispatch_uid="save_steam_player")
def save_steam_player(sender, instance, **kwargs):
    regex = r'http://steamcommunity.com/openid/id/(\w+)'
    match = re.findall(regex, instance.claimed_id)
    if len(match) > 0:
        steam_id = match[0]
        if Player.objects.filter(id=steam_id).count() == 0:
            player = Player.objects.steam_create(steam_id=steam_id)
            UserSteam.objects.create(user=instance.user, player=player)
