import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):

    uuid = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _("CustomUser")
        verbose_name_plural = _("CustomUsers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CustomUser_detail", kwargs={"pk": self.pk})
