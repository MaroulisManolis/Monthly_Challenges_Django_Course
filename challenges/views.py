from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
