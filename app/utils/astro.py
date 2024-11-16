from kerykeion import AstrologicalSubject, relationship_score, KerykeionChartSVG, ChartType


def get_natal_user_map(data: dict):
    name = data.get("name", "user")
    year = data.get("year", None)
    month = data.get("month", None)
    day = data.get("day", None)
    hour = data.get("hour", 12)
    minute = data.get("minute", 00)
    city = data.get("city", "London")
    
    return AstrologicalSubject(name, year, month, day, hour, minute, city)



def get_natal_svg(data: dict):
    name = data.get("name", "user")
    year = data.get("year", None)
    month = data.get("month", None)
    day = data.get("day", None)
    hour = data.get("hour", 12)
    minute = data.get("minute", 00)
    city = data.get("city", "London")

    employee = AstrologicalSubject(name, year, month, day, hour, minute, city)
    
    return KerykeionChartSVG(employee, "Natal")



def get_two_users_synstry_svg(data1: dict, data2: dict):
    emp1 = get_natal_user_map(data1)
    emp2 = get_natal_user_map(data2)
    
    return KerykeionChartSVG(emp1, "Synastry", emp2)



def get_score(data1: dict, data2: dict):
    emp1 = get_natal_user_map(data1)
    emp2 = get_natal_user_map(data2)
    
    return relationship_score(emp1, "Synastry", emp2)
