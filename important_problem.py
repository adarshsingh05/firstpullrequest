# templete of aletter to send t to various people just by repacing date and name
letter = '''good evening, dear <|NAME|>
you are selected!!!! for the upcoming drdo reasearch program
 and the date of reporting is <|DATE|>'''
name = input("enter your name \n")
date = input("enter the date \n")
letter = letter.replace("<|NAME|>", name)
letter= letter.replace("<|DATE|>", date)
print(letter)