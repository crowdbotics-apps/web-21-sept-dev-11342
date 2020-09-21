from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )
    hgjfhgg = models.OneToOneField(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customtext_hgjfhgg",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    sdrgadrtgwgs = models.BigIntegerField(
        null=True,
        blank=True,
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Hmhgfhgf(models.Model):
    "Generated Model"
    jhgjhgj = models.BigIntegerField(
        blank=True,
    )
    wrewtqwewetq43tq45trtwertwertwertwertertwe = models.ForeignKey(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="hmhgfhgf_hgfhgfhgfh",
    )
    hgfhfgfhgf = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="hmhgfhgf_hgfhfgfhgf",
    )
