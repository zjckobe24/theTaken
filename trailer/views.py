from django.shortcuts import render_to_response
import datetime

# Create your views here.
def current_date(req):
    now = datetime.datetime.now()
    return render_to_response("currentTime.html", {"current_date":now})