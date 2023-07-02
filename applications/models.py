from django.utils.translation import gettext_lazy as _
from django.db import models
from django_countries.fields import CountryField


class Interaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    interaction_date = models.DateField(blank=False, null=False)
    interaction_description = models.TextField(blank=False, null=False)


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = CountryField(blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)


class Insight(models.Model):
    id = models.BigAutoField(primary_key=True)
    cv_match = models.DecimalField(
        max_digits=4, decimal_places=2
    )


class Application(models.Model):
    class ApplicationStatus(models.TextChoices):
        DATED = "DATED", _("Dated")
        PENDING = "PENDING", _("Pending")
        OFFER = "OFFER", _("Offer")
        ACCEPTED = "ACCEPTED", _("Accepted")
        REJECTED = "REJECTED", _("Rejected")

    class WorkModel(models.TextChoices):
        ONSITE = "ONSITE", _("On-Site")
        REMOTE = "REMOTE", _("Remote")
        HYBRID = "HYBRID", _("Hybrid")

    class JobType(models.TextChoices):
        FULL_TIME = "FULL_TIME", _("Full-time")
        PART_TIME = "PART_TIME", _("Part-time")
        CONTRACT = "CONTRACT", _("Contract")
        TEMPORARY = "TEMPORARY", _("Temporary")
        INTERNSHIP = "INTERNSHIP", _("Internship")
        OTHER = "OTHER", _("Other")

    id = models.BigAutoField(primary_key=True)

    application_status = models.CharField(
        max_length=16,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.PENDING,
    )
    application_date = models.DateField(blank=False, null=False)

    post_url = models.URLField()
    company_name = models.CharField(max_length=255, blank=False, null=False)
    company_insights = models.TextField()

    job_title = models.CharField(max_length=255, blank=False, null=False)
    job_location = models.OneToOneField(Location, on_delete=models.CASCADE)
    job_role_and_responsibilities = models.TextField(blank=False, null=False)
    job_requirements = models.TextField(blank=False, null=False)
    job_benefits = models.TextField(blank=False, null=False)

    work_model = models.CharField(
        max_length=16, choices=WorkModel.choices, default=WorkModel.ONSITE
    )

    interactions = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    notes = models.TextField(blank=False, null=False)
