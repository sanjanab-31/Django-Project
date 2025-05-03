from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):  
     months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']  
     
     return render(request, 'myapp/months.html', {'months': months})

def january(request):

        return HttpResponse("Here are January events")

def events_by_month(request, month):    
     # Hardcoded events for demo    
    events = {
        "January": ["New Year Party", "Republic Day Parade"],
        "February": ["Valentine's Concert", "Science Fair"],
        "March": ["Holi Festival", "Startup Meetup"],
        "April": ["Spring Festival", "Earth Day Celebration"],
        "May": ["Memorial Day Parade", "Summer Kickoff"],
        "June": ["Graduation Ceremony", "Music Festival"],
        "July": ["Independence Day Celebration", "Beach Party"],
        "August": ["Summer Fair", "Back to School Bash"],
        "September": ["Labor Day Picnic", "Fall Festival"],
        "October": ["Halloween Party", "Pumpkin Carving Contest"],
        "November": ["Thanksgiving Dinner", "Black Friday Sales"],
        "December": ["Christmas Celebration", "New Year's Eve Party"],
        # Add more months if you want
    }
    event_list = events.get(month, ["No events found for this month."])
    return HttpResponse(f"Events in {month}: {', '.join(event_list)}") 
