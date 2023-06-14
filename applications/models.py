from django.utils.translation import gettext_lazy as _
from django.db import models


class Interaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    interaction_date = models.DateField(blank=False, null=False)
    interaction_description = models.TextField(blank=False, null=False)


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)


class Application(models.Model):
    class ApplicationStatus(models.TextChoices):
        DATED = "DATED", _("Dated")
        PENDING = "PENDING", _("Pending")
        OFFER = "OFFER", _("Offer")
        ACCEPTED = "ACCEPTED", _("Accepted")
        REJECTED = "REJECTED", _("Rejected")

    class WorkModel(models.TextChoices):
        ONSITE = "On-site", _("On-Site")
        REMOTE = "Remote", _("Remote")
        Hybrid = "Hybrid", _("Hybrid")

    id = models.BigAutoField(primary_key=True)

    application_status = models.CharField(
        max_length=16,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.PENDING,
    )
    work_model = models.CharField(
        max_length=16, choices=WorkModel.choices, default=WorkModel.ONSITE
    )
    application_date = models.DateField(blank=False, null=False)
    post_url = models.URLField()
    company_name = models.CharField(max_length=255, blank=False, null=False)
    job_title = models.CharField(max_length=255, blank=False, null=False)
    job_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    job_role_and_responsibilities = models.TextField(blank=False, null=False)
    job_requirements = models.TextField(blank=False, null=False)
    job_benefits = models.TextField(blank=False, null=False)
    notes = models.TextField(blank=False, null=False)
    interactions = models.ForeignKey(Interaction, on_delete=models.CASCADE)
