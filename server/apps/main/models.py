from django.db import models
from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    userid = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    profilepic = models.ImageField(upload_to='profile_image')

    class Meta:
        verbose_name_plural = "Userprofile"

        def __str__(self):
            return self.profilepic


class Password(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='passwords',
    )
    url = models.CharField(max_length=256)
    encrypted_password = models.CharField(max_length=256)
    device = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Password"

    def __str__(self):
        return 'Password=' + self.encrypted_password


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Password Categories"

    def __str__(self):
        return self.category_name
