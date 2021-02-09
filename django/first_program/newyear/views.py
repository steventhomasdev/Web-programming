from django.shortcuts import render
import datetime

# Create your views here.

def christmas_check(request):
    now = datetime.datetime.now()
    return render(
        request,
        "christmas_check\christmas_check.html",
        {"christmas": now.month == 12 and now.day == 25}
    )
