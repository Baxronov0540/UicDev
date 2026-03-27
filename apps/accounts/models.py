from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.choices import GenderChoices
from apps.accounts.managers import UserManager
from apps.common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone = models.CharField(_("phone"), max_length=20, unique=True, validators=[RegexValidator(r"^\+?1?\d{9,15}$")])
    first_name = models.CharField(verbose_name=_("first_name"), max_length=30, null=True, blank=True)
    last_name = models.CharField(verbose_name=_("last_name"), max_length=30, null=True, blank=True)
    gender = models.CharField(
        verbose_name=_("gender"), max_length=10, choices=GenderChoices.choices, null=True, blank=True
    )
    avatar = models.ForeignKey(
        "common.Media",
        verbose_name=_("avatar"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_avatars",
    )
    bio = models.CharField(verbose_name=_("bio"), max_length=255, null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name=_("age"), null=True, blank=True)
    country = models.ForeignKey(
        "common.Country",
        verbose_name=_("country"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_countries",
    )
    region = models.ForeignKey(
        "common.Region",
        verbose_name=_("region"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_regions",
    )
    is_staff = models.BooleanField(default=False, verbose_name=_("is staff"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("is deleted"))
    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.phone


class Education(BaseModel):
    name = models.CharField(_("name"), max_length=255)
    type = models.CharField(_("type"), max_length=100)
    website_url = models.URLField(_("website URL"), max_length=500, blank=True)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        verbose_name = _("education")
        verbose_name_plural = _("education")

    def __str__(self):
        return self.name


class UserEducation(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="educations",
        verbose_name=_("user"),
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE,
        related_name="user_educations",
        verbose_name=_("education"),
    )
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"), null=True, blank=True)

    class Meta:
        verbose_name = _("user education")
        verbose_name_plural = _("user educations")

    def __str__(self):
        return f"{self.user} - {self.education}"


class UserExperience(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiences",
        verbose_name=_("user"),
    )
    name = models.CharField(_("name"), max_length=255)
    position = models.CharField(_("position"), max_length=255)
    website_url = models.URLField(_("website URL"), max_length=500, blank=True)
    skills = models.TextField(_("skills"), blank=True)
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"), null=True, blank=True)

    class Meta:
        verbose_name = _("user experience")
        verbose_name_plural = _("user experiences")

    def __str__(self):
        return f"{self.user} - {self.name}"


class UserCertificate(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name=_("user"),
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name=_("course"),
    )
    name = models.CharField(_("name"), max_length=255)
    attachment = models.ForeignKey(
        "common.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="certificate_attachments",
        verbose_name=_("attachment"),
    )

    class Meta:
        verbose_name = _("user certificate")
        verbose_name_plural = _("user certificates")

    def __str__(self):
        return self.name


class Author(BaseModel):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ForeignKey(
        "common.Media",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="author_avatars",
        verbose_name=_("avatar"),
    )
    experience_years = models.PositiveIntegerField(_("experience years"), default=0)

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
