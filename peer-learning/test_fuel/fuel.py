def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percent = convert(fraction)
            print(gauge(percent))
            break

        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction:str):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError #Raising the exception for the test to identify
        
        if x > y:
            raise ValueError
        if x < 0 or y < 0:
            raise ValueError

        return round((x/y) * 100)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()