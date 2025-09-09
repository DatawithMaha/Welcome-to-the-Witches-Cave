print(r'''
*******************************************************************************
             __,,,
                                 _.--'    /
                              .-'        /
                            .'          |
                          .'           /
                         /_____________|
                       /`~~~~~~~~~~~~~~/
                     /`               /
      ____,....----'/_________________|---....,___
,--""`             `~~~~~~~~~~~~~~~~~~`           `""--,
`'----------------.----,------------------------,-------'`
               _,'.--. \                         \
             .'  (o   ) \                        |
            c   , '--'  |                        /
           /    )'-.    \                       /
          |  .-;        \                       |
          \_/  |___,'    |                    .-'
         .---.___|_      |                   /
        (          `     |               .--'
         '.         __,-'\             .'
           `'-----'`      \        __.'
                           `-..--'`
*******************************************************************************
''')
print("Welcome to the witches cave.")
print("Your mission is to find the potion of youth.")

witches_cave = (input('You\'re in the witches cave. Do you go to the kitchen '
                    'or to the bedroom? \nType "kitchen" or "bedroom"\n')).lower()
if witches_cave == "kitchen":
    cauldron_dilemma = input('You see the witches cauldron, with some potion bottles next to it. '
                             'Do you look inside the cauldron or go to inspect the bottles? '
                             '\nSelect "cauldron" or "bottles"\n').lower()
    if cauldron_dilemma == "bottles":
        potion_of_choice = input('You find 3 bottles of potions but with no labels. One of them is the potion of youth you\'re '
                                 'looking for.'
                                 '\nChoose "red", "blue" or "yellow".\n').lower()
        if potion_of_choice == "yellow":
            print("You drink this potion and feel all tingly. You've found the potion of youth! "
                  "You can now live forever looking young. WIN!")
        elif potion_of_choice== "red":
            print("You drink this potion and it gives you red painful boils all over your body! You cant stand the pain"
                  " and end up jumping off the witches cave into your death. GAME OVER!")
        elif potion_of_choice == "blue":
            print("You drink this potion and turn invisible. There is no antidote so you end up living your whole life "
                  "being invisible. You can\'t stand the loneliness and end up killing yourself. GAME OVER!")
        else:
            print("No such potion exits. Since you took too long to decide, the witch woke up and turned you into a frog!"
                  "GAME OVER!")
    else:
        print("You accidentally drop a newts eye that was sitting on the edge of the cauldron when you went to get closer."
              "This resulted in a big explosion and you died due to it. GAME OVER!")
else:
    print("You woke the witch up from her sleep and she turns you into a frog. GAME OVER!")

