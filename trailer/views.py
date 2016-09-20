from django.shortcuts import render_to_response
from trailer.models import Video
import datetime

# Create your views here.
def current_date(req):
    now = datetime.datetime.now()
    return render_to_response("currentTime.html", {"current_date":now})