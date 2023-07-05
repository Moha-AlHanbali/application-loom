from django.shortcuts import render, redirect
from .forms import ApplicationForm, InteractionForm


def create_application(request):
    if request.method == "POST":
        application_form = ApplicationForm(request.POST)
        interaction_form = InteractionForm(request.POST)

        if (
            application_form.is_valid()
            and interaction_form.is_valid()
        ):
            interaction = interaction_form.save()
            application = application_form.save(commit=False)
            application.interactions = interaction
            application.save()

            return redirect("success_page")
    else:
        application_form = ApplicationForm()
        interaction_form = InteractionForm()

    return render(
        request,
        "applications/create_application.html",
        {
            "interaction_form": interaction_form,
            "application_form": application_form,
        },
    )
