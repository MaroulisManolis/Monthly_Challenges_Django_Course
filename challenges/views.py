from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Learn Django for at least 20 minutes per day!",
    "february": "Walk for at least 30 minutes per day!",
    "march": "Tend to your garden for at least 40 minutes per day!",
    "april": "Have a dinner with friends at least once per week!",
    "may": "Buy birthday presents for all your friends!",
    "june": "Update your CV and look after for a descent job!",
    "july": "Go to the sea for at least 4 days per week!",
    "august": "Organise your summer vacation!",
    "september": "Plant your winter time plants!",
    "october": "Start exercising for at least 30 minutes per day!",
    "november": "Organise your vacation for abroad",
    "december": "Pass Christmas time with all family members!"
}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
