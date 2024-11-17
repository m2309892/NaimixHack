from datetime import date, time

def convert_bd_data(date: date,
                    time: time,):
    
    year = date.year
    month = date.month
    day = date.day

    hour = time.hour
    minute = time.minute

    converted_data = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
    }

    return converted_data