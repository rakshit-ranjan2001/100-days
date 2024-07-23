while True:
    print("""Welcome to Treasure Island.\nYour mission is to find the treasure.""")
    dir = input("""You're at a crossroad. Do you want to go "left" of "right"?\n""")
    if dir == "left":
        print("""You got out of the forest, and seen an island at sight.""")
        dir2 = input("""Will you "swim" or "wait"?\n""")
        if dir2 == "wait":
            print("""You can see a boat afar, after which you convinced them to help you get to the island.""")
            dir3 = input("""At the island, you see 3 doors; "red", "blue" and "yellow". Which door will you choose?\n""")
            if dir3 == "yellow":
                print("Congratulations! You found the treasure. Now you can go back to your main quest.")
                break
            elif dir3 == "red":
                print("""When you opened the red door, flames spout out engulfing you.\nGame Over!""")
                break
            elif dir3 == "blue":
                print("""When you opened the blue door, multiple beasts rushed out the door and attacked you.\nGame Over!""")
                break
            else:
                print("""You didn't choose any door, the doors vanished and the island sunk, taking you with it.\nGame Over!""")
                break
        elif dir2 == "swim":
            print("""You were attacked by a trout.\nGame Over!""")
            break
        else:
            print("""You were attacked by the pirates.\nGame Over!""")
            break
    elif dir == "right":
        print("""You fell into a hole.\nGame Over!""")
        break
    else:
        print("""You were dazed by the spirits of the forest, and were never seen again.\nGame Over!""")
        