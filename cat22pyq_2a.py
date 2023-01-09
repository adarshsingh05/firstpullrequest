season_no=int(input("enter the season"))
if season_no in range(1,13):
    if season_no in range(3,6):
        print("Spring")
    elif season_no in range(6,9):
        print("Summer")
    elif season_no in range(10,12):
        print("Automn")
    else:
        print("Winter")
else:
    print("invalid input plsease enter between 1 to 12")
