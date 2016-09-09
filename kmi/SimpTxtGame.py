while True:
    game=input("Type start to begin quest. Or quit to exit program.").lower()
    if game=="start":
        while True:
            story=input("Once upon a time a legendary hero was called to go on a quest. "
                        +"You can start by going through the mountains or the plains. "
                        +"Type your choice to continue.").lower()
            if story=="mountains":
                while True:
                    mountains=input("You wander along the mountain trail until you get to a cave. "
                                    +"Type continue to move forward or cave to go in.").lower()
                    if mountains=="continue":
                        print("You continue down the path and complete the quest bringing you unfathomable wealth and glory.")
                    elif mountains=="cave":
                        print("You encountered a foe stronger than you and died a horrible death.")
                    else:
                        print("Could not accept input please retry.")
            elif story=="plains":
                print("You easily complete the quest without encountering anything along your way.")
            else:
                print("Could not accept input please retry.")
    elif game=="quit":
        break
    else:
        print("Could not accept input please retry.")