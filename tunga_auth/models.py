from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

from tunga_utils import bitcoin_utils, coinbase_utils
from tunga_utils.constants import PAYMENT_METHOD_BTC_ADDRESS, PAYMENT_METHOD_BTC_WALLET, BTC_WALLET_PROVIDER_COINBASE, \
    USER_TYPE_DEVELOPER, USER_TYPE_PROJECT_OWNER

USER_TYPE_CHOICES = (
    (USER_TYPE_DEVELOPER, 'Developer'),
    (USER_TYPE_PROJECT_OWNER, 'Project Owner')
)


class TungaUser(AbstractUser):
    type = models.IntegerField(choices=USER_TYPE_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)

    class Meta(AbstractUser.Meta):
        unique_together = ('email',)

    def save(self, *args, **kwargs):
        if self.type == USER_TYPE_PROJECT_OWNER:
            self.pending = False
        super(TungaUser, self).save(*args, **kwargs)

    @property
    def display_name(self):
        return (self.get_full_name() or self.username).title()

    @property
    def short_name(self):
        return (self.get_short_name() or self.username).title()

    @property
    def name(self):
        return (self.get_full_name() or self.username).title()

    @property
    def display_type(self):
        return self.get_type_display()

    @property
    def is_developer(self):
        return self.type == USER_TYPE_DEVELOPER

    @property
    def is_project_owner(self):
        return self.type == USER_TYPE_PROJECT_OWNER

    @property
    def avatar_url(self):
        if self.image:
            return self.image.url
        social_accounts = self.socialaccount_set.all()
        if social_accounts:
            return social_accounts[0].get_avatar_url()
        return None

    @property
    def profile(self):
        try:
            return self.userprofile
        except:
            return None

    @property
    def payment_method(self):
        if not self.profile:
            return None
        return self.profile.payment_method

    @property
    def mobile_money_cc(self):
        if not self.profile:
            return None
        return self.profile.mobile_money_cc

    @property
    def mobile_money_number(self):
        if not self.profile:
            return None
        return self.profile.mobile_money_number

    @property
    def btc_address(self):
        if not self.profile:
            return None

        if self.profile.payment_method == PAYMENT_METHOD_BTC_ADDRESS:
            if bitcoin_utils.is_valid_btc_address(self.profile.btc_address):
                return self.profile.btc_address
        elif self.profile.payment_method == PAYMENT_METHOD_BTC_WALLET:
            wallet = self.profile.btc_wallet
            if wallet.provider == BTC_WALLET_PROVIDER_COINBASE:
                client = coinbase_utils.get_oauth_client(wallet.token, wallet.token_secret, self)
                return coinbase_utils.get_new_address(client)
        return None


class EmailVisitor(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email

    class Meta:
        ordering = ['-created_at']
