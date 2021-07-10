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
    print("Face: The grizzled look of someone that's gone through too much shit. If the sketch were any more"
          "detailed, you'd see scars and a landscape of wrinkles unbefit of someone as young as you.")
