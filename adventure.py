def start():
    print("A ray of sunlight beams across your eyes."
          " You are instantly comforted by the rigorous rocking of the waves.")
    print("To your left: a chair bolted down to the sturdy wooden flooring.\n"
          "To your right: a small window with a brief glimpse at the deep blue sea beyond.")
    print("Temptation swathes over you like the wide stroke of a brush,\n"
          "look outside or sit on the chair?")

    answer = input(">").lower()
    if "look outside" in answer:
        window_glance()
    elif "sit on the chair" in answer:
        tableside_read()
    else:
        print("Invalid argument.")


def window_glance():
    print("You have a look out the window and catch a whiff of the ocean's salty breeze.\n"
          "You feel alive.\n"
          "The feeling lasts but a moment.")
    print("Your eyes turn to an open doorway\nThe ship is alive with movement\nNobody glances into your cabin.\n"
          "PARIAH")
    print("Before leaving the cabin you want to have a look at your journal.\n"
          "\n"
          "Don't you?")

    answer = input(">").lower()
    if "yes" in answer:
        print("Of course you do.")
        tableside_read()
    elif "no" in answer:
        print("This is why they don't like you.")
        tableside_read()


def tableside_read():
    print("The chair is hard, uncomfortable, yet familiar.\nWithin reach is a small dark journal."
          " Its leather-bound cover has faded, the surface scratched beyond repair.\n"
          "You could continue staring at it all day, or you could open the damned thing.")

    answer = input(">").lower()
    if "open" in answer:
        print("A rather well-created sketch of yourself stares back at you.\n"
              "Some information has been noted beside it:")
        facial_features()
        print("That's definitely you.")
    else:
        print("Some things are best left forgotten.")


def facial_features():
    print("Eyes:")
    eye = input(">").lower()
    if "brown" in eye:
        print("Brown eyes. As basic as they come.")
    elif "green" in eye:
        print("Green eyes. Like staring at a pair emeralds.")
    elif "yellow" in eye:
        print("Yellow eyes. Some would akin them to a midday sun, others would call them sickly.")
    elif "blue" in eye:
        print("Blue eyes. The colour of the sea.")
    else:
        print("What does it matter; nobody looks there anyway.")
    print("Hair:")
    hair = input(">").lower()
    if "black" in hair:
        print("Black hair. You'd blend in well into the night.")
    elif "red" in hair:
        print("Red hair. Uncommon among your kind. Always draws attention to you.")
    elif "white" in hair:
        print("White hair. Many have asked if you've dyed it.")
    else:
        print("As if your hair colour would make you any special.")
    print("Face: Short and angular snout, a single triangular ear, and a small black nose. As Vulper as they come.")


start()
