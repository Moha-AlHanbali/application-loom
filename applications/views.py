from django.shortcuts import render, redirect
from .forms import ApplicationForm, InteractionForm, LocationForm


def create_application(request):
    if request.method == "POST":
        application_form = ApplicationForm(request.POST)
        location_form = LocationForm(request.POST)
        interaction_form = InteractionForm(request.POST)

        if (
            application_form.is_valid()
            and location_form.is_valid()
            and interaction_form.is_valid()
        ):
            interaction = interaction_form.save()
            location = location_form.save()
            application = application_form.save(commit=False)
            application.interactions = interaction
            application.job_location = location
            application.save()

            return redirect("success_page")
    else:
        application_form = ApplicationForm()
        location_form = LocationForm()
        interaction_form = InteractionForm()

    return render(
        request,
        "applications/create_application.html",
        {
            "interaction_form": interaction_form,
            "location_form": location_form,
            "application_form": application_form,
        },
    )
