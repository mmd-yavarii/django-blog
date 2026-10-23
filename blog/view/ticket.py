from ..models import Ticket
from ..forms import ticketForm
from django.shortcuts import redirect, render


def ticket(request):
    if request.method == "POST":
        form = ticketForm(request.POST)

        print(form.is_valid)

        if form.is_valid():
            cd = form.cleaned_data

            Ticket.objects.create(
                message=cd["message"],
                name=cd["name"],
                email=cd["email"],
                phone=cd["phone"],
                subject=cd["subject"],
            )

            return redirect("blog:posts_list")

    else:
        form = ticketForm()

    return render(request, "forms/ticket.html", {"form": form})