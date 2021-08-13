from datetime import datetime

def convert_to_12hr(tm):
    d = datetime.strptime(tm, "%H:%M")
    return d.strftime("%I:%M %p")

def convert_to_date(s):
    datetime_object = datetime.strptime(s, '%d %b %Y %H:%M:%S')
    return datetime_object