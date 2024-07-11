def fahr_to_celsius(temp_fahrenheit):
    celsius = (temp_fahrenheit -32) / 1.8
    return celsius

def temp_classifier(temp_celsius):
    if temp_celsius < -2:
        return "0"
    elif  2 > temp_celsius >= -2:
        return "1"
    elif  15 > temp_celsius >= 2:
        return "2"
    elif temp_celsius >= 15:
        return "3"