import datetime

#This function gets events that are not overdue. Only evnts not held are displayed
def get_valid_upcoming_events(get_upcomingevents):
    todays_date = datetime.date.today()
    valid_upcomingevents = []
    for item in get_upcomingevents:
        date_diff = (item.start_day - todays_date).days
        if date_diff > -1 :
            valid_upcomingevents.append(item)
        else :
            pass
    return valid_upcomingevents
