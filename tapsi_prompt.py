from station import *
if __name__ == "__main__":

# Dictionary of taxis
    taxis = {
    1: True,
    2: True,
    3: True,
    4: False,
    44: True,
    443: False,
    4432: True,
    55: False,
    22: False,
    123: True
    }

    while True:
        print("Welcome to HolbieTapsi a great app to order taxis in Barranquilla city")
        print("What would you like to do?")
        print("Write 1 - To dispatch a HolbieTapsi")
        print("Write 2 - To Add a taxi to the station")
        orden = int(input("Enter your option -> "))
        if orden == 1:
            dispatch(taxis)
        elif orden == 2:
            add_taxi(taxis)
        else:
            print("")
            print("Enter a valid option ")
            print("")






