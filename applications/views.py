from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ApplicationForm, InteractionForm, CareerBoardForm


# @login_required
def create_career_board(request):
    if request.method == 'POST':
        form = CareerBoardForm(request.POST)
        if form.is_valid():
            career_board = form.save(commit=False)
            career_board.user = request.user
            career_board.save()
            return redirect('career_board_list') #WIP
    else:
        form = CareerBoardForm()

    return render(request, 'applications/create_career_board.html', {'form': form})


# @login_required
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
