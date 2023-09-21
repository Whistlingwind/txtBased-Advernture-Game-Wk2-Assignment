import random
#Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont

min_value = 1
max_value = 3 
def castle_foyer():
   print("You find yourself standing in front of the massive Castle Foyer door.")
   print("As you push it open, you're greeted by the dimly lit grand entrance.")
   print("Dusty tapestries hang from the walls, and the air is thick with mystery.")
   print("Two paths lie before you:")
   print("1. The door to the Drill Room is shrouded in shadows.")
   print("2. The entrance to the Armoury gleams with the promise of weapons and secrets.")
   # get an image
   base = Image.open(r'c:\Users\adria\Desktop\Knights Destiny Pictures\Knights Destiny\Knights Destiny\foyer.jpg').convert('RGBA')

   # make a blank image for the text, initialized to transparent text color
   txt = Image.new('RGBA', base.size, (255,255,255,0))

   # get a font
   fnt = ImageFont.truetype(r'c:\\Users\\adria\Desktop\\Knights Destiny Pictures\\Knights Destiny\\Knights Destiny\\Ghost-Battle-Personal.otf', 20)


   # get a drawing context
   d = ImageDraw.Draw(txt)

   # draw text, half opacity
   d.text((6,14), "You find yourself standing in front of the massive Castle Foyer door.", font=fnt, fill=(255,255,255,128))
   d.text((6,38), "As you push it open you are greeted by the dimly lit grand entrance.", font=fnt, fill=(255,255,255,128))
   d.text((6,62), "Dusty tapestries hang from the walls, and the air is thick with mystery.", font=fnt, fill=(255,255,255,128))


   # draw text, full opacity
   d.text((14,110), "Two paths lie before you:", font=fnt, fill=(255,255,255,255))
   d.text((14,134), "1. The door to the Drill Room is shrouded in shadows.", font=fnt, fill=(255,255,255,255))
   d.text((14,158), "2. The entrance to the Armoury gleams with the promise of weapons and secrets.", font=fnt, fill=(255,255,255,255))
   out = Image.alpha_composite(base, txt)

   #Show image
   out.show()
    

   while True:
        choice = input("Enter your choice: ")
        
        if choice in ("1", "2"):  # Check if the choice is either "1" or "2"
            if choice == "1":
                drill_room()
            elif choice == "2":
                guess_number_to_return("Castle Foyer")
            break  # Exit the loop if the choice is valid
        else:
            print("You have to enter a valid location.")
    
def drill_room():
    print("Inside the Drill Room, you're surrounded by ancient weapons and training dummies.")
    print("It is quiet and a single candle flickers on a dusty table.")
    print("Two passages in front of you:")
    print("1. The Museum door is slightly open, revealing glimpses of precious artifacts.")
    print("2. The War Room lies at the end of a corridor, its door imposing and locked.")
    
   # get an image
    base = Image.open(r'C:\Users\adria\Desktop\Knights Destiny Pictures\Knights Destiny\Knights Destiny\drillroom.jpg').convert('RGBA')

   # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

   # get a font
    fnt = ImageFont.truetype(r'c:\\Users\\adria\Desktop\\Knights Destiny Pictures\\Knights Destiny\\Knights Destiny\\Ghost-Battle-Personal.otf', 20)

   # get a drawing context
    d = ImageDraw.Draw(txt)

   # draw text, half opacity
    d.text((6,14), "Inside the Drill Room you are surrounded by ancient weapons and training dummies.", font=fnt, fill=(255,255,255,128))
    d.text((6,38), "It is quiet and a single candle flickers on a dusty table.", font=fnt, fill=(255,255,255,128))


   # draw text, full opacity
    d.text((14,110), "Two passages in front of you:", font=fnt, fill=(255,255,255,255))
    d.text((14,134), "1. The Museum door is slightly open revealing glimpses of precious artifacts.", font=fnt, fill=(255,255,255,255))
    d.text((14,158), "2. The War Room lies at the end of a corridor its door imposing and locked.", font=fnt, fill=(255,255,255,255))
    out = Image.alpha_composite(base, txt)

   #Show image
    out.show()

    while True:
        choice = input("Enter your choice: ")
        
        if choice in ("1", "2"):  # Check if the choice is either "1" or "2"
            if choice == "1":
                museum()
            elif choice == "2":
                guess_number_to_return("Drill Room")
            break  # Exit the loop if the choice is valid
        else:
            print("You have to enter a valid location.")
def museum():
    print("Entering the Museum, you're surrounded by rows of gleaming weapons and suits of armor.")
    print("The room is filled with the smell of polished steel and leather.")
    print("Two paths lay ahead:")
    print("1. A door with an unknown destination. Will this be your Final Destination? Do you dare to open it?")
    print("2. The Courtyard appears hidden behind a heavy metal door, promising escape. But are your enemies waiting there?")

   # get an image
    base = Image.open(r'c:\Users\adria\Desktop\Knights Destiny Pictures\Knights Destiny\Knights Destiny\museum.jpg').convert('RGBA')

   # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

   # get a font
    fnt = ImageFont.truetype(r'c:\\Users\\adria\Desktop\\Knights Destiny Pictures\\Knights Destiny\\Knights Destiny\\Ghost-Battle-Personal.otf', 20)

   # get a drawing context
    d = ImageDraw.Draw(txt)

   # draw text, half opacity
    d.text((6,14), "Entering the Museum you are surrounded by rows of gleaming weapons and suits of armor.", font=fnt, fill=(255,255,255,128))
    d.text((6,38), "The room is filled with the smell of polished steel and leather.", font=fnt, fill=(255,255,255,128))


   # draw text, full opacity
    d.text((14,110), "Two paths lay ahead:", font=fnt, fill=(255,255,255,255))
    d.text((14,134), "1. A door with an unknown destination. Will this be your Final Destination? Do you dare to open it?", font=fnt, fill=(255,255,255,255))
    d.text((14,158), "2. The Courtyard appears hidden behind a heavy metal door, promising escape. But are your enemies waiting there?", font=fnt, fill=(255,255,255,255))
    out = Image.alpha_composite(base, txt)

   #Show image
    out.show()

    while True:
        choice = input("Enter your choice: ")
        
        if choice in ("1", "2"):  # Check if the choice is either "1" or "2"
            if choice == "1":
                print("Congratulations! You have reached the Secret Passage!")

   # get an image
                base = Image.open(r'c:\Users\adria\Desktop\Knights Destiny Pictures\Knights Destiny\Knights Destiny\secretpassage.jpg').convert('RGBA')

   # make a blank image for the text, initialized to transparent text color
                txt = Image.new('RGBA', base.size, (255,255,255,0))

   # get a font
                fnt = ImageFont.truetype(r'c:\\Users\\adria\Desktop\\Knights Destiny Pictures\\Knights Destiny\\Knights Destiny\\Ghost-Battle-Personal.otf', 20)

   # get a drawing context
                d = ImageDraw.Draw(txt)




   # draw text, full opacity
                d.text((14,110), "Congratulations! ", font=fnt, fill=(255,255,255,255))
                d.text((14,158), "You have reached the Secret Passage!", font=fnt, fill=(255,255,255,255))

                out = Image.alpha_composite(base, txt)

   #Show image
                out.show()





            elif choice == "2":
                guess_number_to_return("Museum")
            break  # Exit the loop if the choice is valid
        else:
            print("You have to enter a valid location.")
def guess_number_to_return(location):
    print(f"DEAD END! If you guess the correct number from 1 to 3, you will go back to {location}")
    while True:
        correct_number = random.randint(min_value, max_value)
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            if min_value <= guess <= max_value:
                if guess == correct_number:
                    print(f"Correct! You can now return to the {location}.")
                    if location == "Castle Foyer":
                        castle_foyer()
                    elif location == "Drill Room":
                        drill_room()
                    elif location == "Museum":
                        museum()
                    break
                else:
                    print("Wrong guess. Try again.")
            else:
                print("Please enter a valid value from 1 to 3.")
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
# Start the game in the Castle Foyer
castle_foyer()
