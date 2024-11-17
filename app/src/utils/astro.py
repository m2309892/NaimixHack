from kerykeion import AstrologicalSubject, relationship_score, KerykeionChartSVG, ChartType, RelationshipScore
import os

def get_natal_user_map(data: dict):
    name = data.get("name", "user")
    year = data.get("year", None)
    month = data.get("month", None)
    day = data.get("day", None)
    hour = data.get("hour", 12)
    minute = data.get("minute", 00)
    
    return AstrologicalSubject(name, year, month, day, hour, minute, lng=50, lat=50, tz_str="Europe/Rome", city="Rome")



def get_natal_svg(data: dict):
    name = data.get("name", "user")
    year = data.get("year", None)
    month = data.get("month", None)
    day = data.get("day", None)
    hour = data.get("hour", 12)
    minute = data.get("minute", 00)

    employee = AstrologicalSubject(name, year, month, day, hour, minute, lng=50, lat=50, tz_str="Europe/Rome", city="Rome")
    
    synastry_chart = KerykeionChartSVG(employee, "Natal")
    svg_content = synastry_chart.makeSVG()
    
    if svg_content is None:
        return {"error": "Не удалось сгенерировать SVG-контент"}
# Сохранение SVG-файла
    home_directory = os.path.expanduser("~")
    file_path = os.path.join(home_directory, "synastry_chart.svg")
    
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)
        
    return file_path



def get_two_users_synstry_svg(data1: dict, data2: dict):
    emp1 = get_natal_user_map(data1)
    emp2 = get_natal_user_map(data2)
    
    synastry_chart = KerykeionChartSVG(emp1, "Synastry", emp2)
    svg_content = synastry_chart.makeSVG()
    
    if svg_content is None:
        return {"error": "Не удалось сгенерировать SVG-контент"}
    
# Сохранение SVG-файла
    home_directory = os.path.expanduser("~")
    file_path = os.path.join(home_directory, "synastry_chart.svg")
    
    with open(file_path, "w") as svg_file:
        svg_file.write(svg_content)
        
    return file_path



def get_score(data1: dict, data2: dict):
    emp1 = get_natal_user_map(data1)
    emp2 = get_natal_user_map(data2)
    
    return RelationshipScore(emp1, emp2).score
