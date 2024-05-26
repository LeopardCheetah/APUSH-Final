import time
import os
# can't do randomness since i'm pretty sure that isn't possible

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def cline():
    # clear the previous line
    print ("\033[A                                                                       \033[A") # more spaces == more part of the line cleared


def prints(text):
    # print slow
    # text must be one line

    typing_speed = 0.04

    arr = list(text)
    for i in arr:
        print(i, end='', flush=True)
        time.sleep(typing_speed)
    
    print()
    


def printslow(text):
    # print slow
    # text must be one line

    typing_speed = 0.175

    arr = list(text)
    for i in arr:
        print(i, end='', flush=True)
        time.sleep(typing_speed)
    
    print()



# TODO: turn this into a .exe and try to run it

###
cls() # get rid of warnings
##################################################################################################################################################################


def man_16_17():
    cls()

    # time period/situation:
    # you start off in new england
    # we then follow each of your sons as they live until the revolutionary war happens... then we end off there

    # avg lifespan ~40years so 30-ish year time chunks --> 5 people (1620 + 150 = 1770)


    # plot points to hit:
    # British saultary neglect mercantilism 
    # > navigation acts (1651, 60, 63, 73, 96, further on too)

    # King Phillips (1675)
    # northern diverse economy -- show don't tell -- lumber
    # Halfway Covenant (1740s?)
    # Great Awakening (1730s)
    # Enlightenment

    # F&I War
    # Things leading up to the Am. Revl (gamify this portion)





    # holy shit we're gonna downsize hella
    

    
    # plot points to hit:
    # > navigation acts (1651, 60, 63, 73, 96, further on too)

    # King Phillips (1675)
    # northern diverse economy -- show don't tell -- lumber



    main_scene = """
    

    
    +---------------------------------------------------------------+---------------------+
    |                                                               |     ,,,        year:|
    |              x                                                |   _/. .\_       1633|
    |   .-. _______|                             +                  |  (.\_o_/.)          |
    |   |=|/     /  \                            A_                 |  (.`,.`'.')     age:|
    |   | |_____|_""_|---|---|---|---|          /\-\                |   ('.`,'`,)        0|
    |   |_|_[X]_|____|---|---|---|---|      ____||"|____            |    ('.`,'`)         |
    |   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      ~^~^~^~^~^~^            |     `--'"`          |   
    +---------------------------------------------------------------+---------------------+



       
         
    """
    
    print(main_scene)


    # name can't be randomly generated since the random module doesn't work
    name = 'John Taylor'

    s = 'You, '+name+', are born in the Massachusets Bay Colony, in 1633.'
    # text
    prints(s)
    prints("You are born to Adam and Jeannine, a young couple who moved to Massachusets during the the so-called 'Great Migration'.")
    time.sleep(0.25)
    prints("Anyways, a few years earlier, John Winthrop established this city and called it the 'city upon a hill,' or the idea that")
    prints("this city is blessed by God, and that it will act as a model for other colonists to follow in.")
    time.sleep(0.5)
    print()
    prints("Anyways, you are but an infant living on your small farm with your parents.")


    time.sleep(1.5)
    cls()


    scene_two = """

        
    +-----------------------------------------------------------+----------------------+
    |                                                           |                 year:|
    |              x                                   +        |     ,=""=,       1637|
    |   .-. _______|                                  /_\       |     c , _,{          |
    |   |=|/     /  \                       ,%%%______|O|       |     /\  @ )      age:|
    |   | |_____|_""_|---|---|---|---|      %%%/_________\      |    /  ^~~^\         4|
    |   |_|_[X]_|____|---|---|---|---|       %%| /\[][][]|%     |   (_/ ,, ,,)         |
    |   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     ___||_||______|%     |    ~\_(/-\)          |
    +-----------------------------------------------------------+----------------------+




    """

    print(scene_two)
    prints('It is now 1637, four years later.')
    prints("You've grown into a nice baby -- which happens for New England families about 70% of the time (infant mortality was pretty high back then).")
    prints("(We're also ignoring the fact that you are statistically likely to have 3 other brothers and 3 other sisters....)")
    time.sleep(0.5)
    print()
    prints("Anyways, during this time period, you start talking.")
    prints("Your mother, Jeannine Taylor also tries to get you to start reading, but you do not oblige.")
    time.sleep(3)



    cls()
    scene_two_five = """
   
    +-----------------------------------------------------------------+
    |      |\                                                    year:|
    |      || .---.                                               1637|
    |      ||/_____\                                                  |
    |      ||(  '.')                                .,                |
    |      || \_-_/_                       .    ____/__,              |
    |      :-"`'V'//-.                   .' \  / \==\```              |
    |     / ,   |// , `\                /    \ 77 \ |                 |
    |    / /|Ll //Ll|| |               /_.----\\\\__,-----.             | 
    |   /_/||__//   || |           <--(\_|_____<__|_____/             |
    |   \ \/---|[]==|| |               \  ````/|   ``/```             |
    |    \/\__/ |   \| |                `.   / |    I|                |
    |    /\|_   | Ll_\ |                  `./  |    I|                |
    |    `--|`^'''^`||_|                       |____I|                |
    |       |   |   ||/                        !!!!!!!                |
    |       |   |   |                          | | I |                |
    |       |   |   |                          | | I |                |
    |       |   |   |                          \ \ I |                |
    |       L___l___J                          | | I |                |
    |        |_ | _|                          _|_|_I_|                |
    |       (___|___)                        /__/____|                |
    +-----------------------------------------------------------------+


    """



    print(scene_two_five)
    time.sleep(1)
    prints("Also,")
    time.sleep(0.3)
    prints("During 1637,")
    time.sleep(0.3)
    prints("Pequot's War happens.")
    print()
    prints("This war, involving over 700 Native American casualties, with tribes being on both sides of the conflict is one example of")
    prints("the conflicts that colonists caused as a result of their migration westward.")
    time.sleep(1)
    print()
    print()
    prints("Your father, Adam Taylor, goes to fight in this war.")
    prints("And over the course of these next three hard fought years....")
    time.sleep(0.6)
    prints('...')
    time.sleep(0.6)
    prints('...')
    time.sleep(1.6)
    print()
    prints('He survives!')
    prints('-> Nice, your dad didn\'t die :)')
    time.sleep(3)
    cls()

    ###########

    scene_three = """
    +-----------------------------------------------+
    |                                          year:|
    |                 _______                   1641|
    |                /  _.'`~\                      |
    |                \ }    -(                  age:|
    |                ,'-,___.'       .-.           8|
    |               /    |_ /|     __| |__          |
    |              /     ` |_/    [__   __]         |
    |             /   \    /         | |            |
    |            /     '--;_         | |            |
    |           _\          `\       | |            |
    |          / |`-.___.    /       | |            |
    |  ^^^^^^`--`------'`--`^^^^^^^^^^^^^^^         |
    +-----------------------------------------------+

    """

    print()
    print(scene_three)
    prints("In 1641, slavery is sanctioned (allowed) in the Massachusets Bay Colony...")
    time.sleep(1.1)

    print()
    print()
    prints("But you pay no mind. You're only 8 after all!")
    prints("Following your parents, you go to church weekly, and live a deeply moral life.")
    prints("You also like farming a lot. John, your father, is a merchant and so wants you to take over his trade.")
    prints("...But you're 8")
    time.sleep(0.5)
    prints("You literally couldn't care less.")
    print()
    print()
    prints("You also start attending school for a few hours every week, because well")
    prints("that's a thing in New England I guess.")

    time.sleep(3)
    cls()
    ##########################

    # your dad lives to be ~65-70 years cuz of healthiness


    scene_four = """
    
    +-----------------------------------------------+
    |                                          year:|
    |                                           1651|
    |                |    |    |                    |
    |               )_)  )_)  )_)               age:|
    |              )___))___))___)\               18|
    |             )____)____)_____)\\\\               |
    |           _____|____|____|____\\\\\__           |
    |  ---------\                   /---------      |
    |     ^^^^^ ^^^^^^^^^^^^^^^^^^^^^               |
    |       ^^^^      ^^^^     ^^^    ^^            |
    |           ^^^^      ^^^                       |
    +-----------------------------------------------+

    """

    print()
    print(scene_four)

    print()
    print()
    prints("It is the year 1651.")
    prints("Britain passes the Navigation Acts, severely limiting the colonists' right to free trade.")
    prints("As of now, they are legally only allowed to trade with Great Britain*.")
    prints("* - (ok everything has a caveat doesn't it? Lumber didn't need to be imported through Great Britain)")

    print()
    print()
    prints("Your father, a puritan man who swore off the stupid Church of England, who is also a merchant, abhors this law.")
    prints("He gets together with his buddies and they become pirates... (or at least are in the piracy business).")
    time.sleep(1)
    print()
    prints("You don't wanna be caught with your father committing crimes, so you depart for Western New York.")
    prints("To go farming.")

    time.sleep(2)
    print()
    prints("As you are (now) of legal age, and have found a wife, your father agrees to let you go, and gives you 200 euros and bids you farewell.")

    time.sleep(2.5)
    


    cls()

#####################################


    scene_five = """

    +--------------------------------------------------------+
    |                                                   year:|
    |                              +&-                   1656|
    |                            _.-^-._    .--.             |
    |                         .-'   _   '-. |__|         age:|
    |                        /     |_|     \|  |           23|
    |                       /               \  |             |
    |                      /|     _____     |\ |             |
    |                       |    |==|==|    |  |             |
    |   |---|---|---|---|---|    |--|--|    |  |             |
    |   |---|---|---|---|---|    |==|==|    |  |             |
    |  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^            |
    +--------------------------------------------------------+




    """   
    print(scene_five)
    prints('So now, you\'re in West (present-day) New York, and have married to your glorious wife Lisa, and as farmers, you live near')
    prints('Fort Nassau, near present-day Albany.')
    print()
    time.sleep(2)
    prints('And not much happens over this time period.......')
    time.sleep(2)
    prints('I mean, is there anything too interesting that happens?')
    time.sleep(2)
    cls()

    print()
    print()
    print()
    print()
    prints('Life on the farm goes well.')
    time.sleep(4)
    print()
    prints('One day, however:')
    time.sleep(2)

    cls()



    ################


    scene_six = """
    

    +-----------------------------------+
    |             ,:' `..;         year:|
    |            `. ,;;'%           1675|
    |            +;;'%%%%%              |
    |             /- %,)%%          age:|
    |             `   \ %%            42|
    |              =  )/ \              |
    |              `-'/ / \             |
    |                /\/.-.\            |
    |               |  (    |           |
    |               |  |   ||           |
    |               |  |   ||           |
    |           _.-----'   ||           |
    |          / \________,'|           |
    |         (((/  |       |           |
    |         //    |       |           |
    |        //     |\      |           |
    |       //      | \     |           |
    |      //       |   \   |           |
    |     //        |    \  |           |
    |    //         |    |\ |           |
    |   //          |    | \|           |
    |  //           \    \              |
    | c'            |\    \             |
    |               | \    \            |
    |               |  \    \           |
    |               |.' \    \          |
    |              _\    \.-' \         |
    |             (___.-(__.'\/         |
    +-----------------------------------+




    """
    
    print(scene_six)
    prints("In the spring of 1675, you receive a letter from your father.")
    prints("He tells you he is very sick, and nearing death.")
    prints("(Life expectancy back then was 65-70 years old which was super old for that time period but still, your father is old.)")
    time.sleep(0.7)
    prints("Naturally, you go and visit him.")
    prints("You arrive in the summer of 1675.")

    time.sleep(1.2)
    print()
    prints("Your father seems to also have moved out of the colony -- he couldn't stand being in such a big town where religion was less and less valued.")
    prints("Instead, he retired in a small town in the backcountry of Massachusets.")
    prints("And now you, your wife, and your parents all reunite in this small town.")
    print()
    time.sleep(1)
    prints("You spend a few days, but ultimately,")
    time.sleep(1)
    prints("As you have crops to tend to,")
    time.sleep(1)
    prints("you wish your father goodbye.")
    time.sleep(3)
    print()
    prints("He later dies in the fall.")

    time.sleep(5)


    cls()

    print()
    print()
    print()
    print()
    printslow('However.')
    printslow('A few days into your trip back to NorthWestern New York.')
    printslow('You-')
    print()
    time.sleep(2)
    printslow('Encounter a tribe of natives,')
    printslow('And,')
    printslow('they kill you.')

    print()
    time.sleep(2)
    printslow('.......')
    time.sleep(4)

    for i in range(12): # this should clear the whole screen.
        cline()
        time.sleep(0.6)

    cls()


    scene_seven = """
                                 _____  _____
                                <     `/     |
                                 >          (
                                |   _     _  |
                                |  |_) | |_) |
                                |  | \ | |   |
                                |            |
                 ______.______%_|            |__________  _____
               _/                                       \|     |
              |               J O H N    T A Y L O R           <
              |_____.-._________              ____/|___________|
                                | * 04/03/33 |
                                | + 07/12/75 |
                                |            |
                                |            |
                                |   _        <
                                |__/         |
                                 / `--.      |
                               %|            |%
                           |/.%%|          -< @%%%
                           `\%`@|     v      |@@%@%%    
                         .%%%@@@|%    |    % @@@%%@%%%%
                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%

    """

    print()
    print(scene_seven)
    print()
    print()
    prints('You, now as a ghost, realize that this Native American killing was not isolated -- rather, King Phillip\'s war,')
    prints('another major conflict between settlers and Native Americans,')
    prints('had started.')
    prints('You were merely caught in the crossfire....')


    time.sleep(5)

    print()
    print()
    print('[The End]')
    print('Made by Alex Z')

    print()
    print()
    print()
    print()
    print()
    print()





##################




def woman_16_17():
    pass
    
    # 1600s scene






###########################################################      OPENING SCENE     #######################################################################


# TODO: change game name later
# for the cool text use this link: https://patorjk.com/software/taag/#p=display&h=0&v=0&f=Sub-Zero&t=America%20Game
# ascii art generator: https://www.asciiart.eu/image-to-ascii

# invalid escape sequence problems but whatever 
before_title = "\nNote: if at any time the program just straight up dies (probably because of a wrong input), just restart it, and it should work fine\nNote 2: this program is now more of just an exposition -- no input is really needed, everything just sort of flows\nNote 3: Please make your window full screen."
title = """
\t \t \t \t \t \t \t Welcome to....
 ______     __    __     ______     ______     __     ______     ______        ______     ______     __    __     ______   
/\  __ \   /\ "-./  \   /\  ___\   /\  == \   /\ \   /\  ___\   /\  __ \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \  __ \  \ \ \-./\ \  \ \  __\   \ \  __<   \ \ \  \ \ \____  \ \  __ \     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\ 
 \ \_\ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\  \ \_\  \ \_____\  \ \_\ \_\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
  \/_/\/_/   \/_/  \/_/   \/_____/   \/_/ /_/   \/_/   \/_____/   \/_/\/_/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 
 
"""


# i don't think the \ts are needed here but whatever
opening_flag = """

                                 o  \t \t \t \t  
                                /\ \t \t \t \t 
                               /::\  \t \t \t \t 
                              /::::\    \t \t \t   
                ,a_a         /\::::/\    \t \t \t   
               {/ ''\_      /\ \::/\ \    \t \t \t  
               {\ ,_oo)    /\ \ \/\ \ \    \t \t \t  
               {/  (_^____/  \ \ \ \ \ \    \t \t \t  
     .=.      {/ \___)))*)    \ \ \ \ \/    \t \t \t 
    (.=.`\   {/   /=;  ~/      \ \ \ \/    \t \t \t 
        \ `\{/(   \/\  /        \ \ \/    \t \t \t 
         \  `. `\  ) )           \ \/    \t \t \t 
          \    // /_/_            \/    \t \t \t 
           '==''---))))

"""


                                                                                                                            
def main():

    cls()
    print(before_title)
    time.sleep(7)
    cls()


    # opening scene
    print(title)
    print(opening_flag)

    print()
    print()


    # used to be a to do:  change this later
    c = 'M'
    # c = input("Would you like to play as a man [M] or woman [W]? \n> ")

    cline()
    cline() 


    # t = input("What time period would you like to play? \n\t 1600s-1700s [A]    |    1700s-1800s [B]   |   1800s-1900s[C] \n> ")
    t = 'a'


    cline()
    cline()
    cline()


    print()
    print()

    try:
        response = input("Press [Enter] to start the game :)\n")
    except:
        print('\n\nSomething went wrong :<')
        return

    try:
        if response.strip() != '':
            print()
            print()
            print('...')
            time.sleep(0.6)
            print('that was not the [Enter] key :/ ')
            time.sleep(0.6)
            print('Aborting...')
            print()
            print()
            return
    except:
        print('\n\nUhh something went wrong')
        return

    flag = 0

    try:
        f = True

        while f:
            if c.strip().lower()[0] == 'm':
                f = False
                flag = 1
                continue
            
            elif c.strip().lower()[0] == 'w':
                f = False
                flag = 2
                continue

            else:
                c = input("Would you like to play as a man [M] or woman [W]? \n> ")
                cline()
                cline()
            
            continue

    except:
        print()
        prints('Something went wrong :(')
        prints('Most likely you entered some bad input')
        prints('Aborting...')
        print()

        return

    if flag == 1:
        man_16_17()
        return
        # lowkey just doing this for readability
    elif flag == 2:
        woman_16_17()
        return






main()
