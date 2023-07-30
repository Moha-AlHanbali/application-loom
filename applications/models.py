from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


class CareerBoard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Interaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    interaction_highlight = models.CharField(max_length=255, blank=False, null=False)
    interaction_date = models.DateField(blank=False, null=False)
    interaction_description = models.TextField(blank=False, null=False)

    def get_company_name(self):
        try:
            application = self.application_set.first()
            if application:
                return f"{application.application_date} - {application.company_name} - {application.job_title}"
            else:
                return None
        except Application.DoesNotExist:
            return None
    
    def __str__(self):
        return f"{self.get_company_name()} - {self.interaction_highlight}"


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

    career_board = models.ForeignKey(CareerBoard, on_delete=models.CASCADE, blank=True, null=True)

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

    job_country = CountryField(blank=False, null=False)
    job_city = models.CharField(max_length=255, blank=False, null=False)
    job_address = models.CharField(max_length=255, blank=False, null=False)

    job_role_and_responsibilities = models.TextField(blank=False, null=False)
    job_requirements = models.TextField(blank=False, null=False)
    job_benefits = models.TextField(blank=False, null=False)

    work_model = models.CharField(
        max_length=16, choices=WorkModel.choices, default=WorkModel.ONSITE
    )

    interactions = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    notes = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.job_title}: {self.company_name}"