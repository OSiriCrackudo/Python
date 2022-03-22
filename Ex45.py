



import os
from textwrap import dedent



class Hero(object):
    

    def __init__(self, Hname, Hhealth, Hattack, Hdefence, Hagility, 
                 Hranged, Hlevel, Hnexlevel):
        
        self.name       = Hname
        self.health     = Hhealth
        self.attack     = Hattack
        self.defence    = Hdefence,
        self.agility    = Hagility
        self.ranged     = Hranged
        self.lvl        = Hlevel
        self.nxtlvl     = Hnexlevel
        

        stats_dic = {
            1 : self.name,
            2 : self.health,
            3 : self.attack,
            4 : self.defence,    
            5 : self.agility, 
            6 : self.ranged, 
            7 : self.lvl, 
            8 : self.nxtlvl     
        }
        

        def getstat(self, stats_number):
            
            stat = stats_dic[stats_number] 
            return stat
        
        def setstats(self, stats_number, new_stat):
            
            stats_dic[stats_number] = new_stat

class Inventory(object):
    pass

def CreateClass():
    
    Hname = CreateClassName()
    
    
    print(f"\nok,{Hname}\n")
    input(">>>")
    os.system('cls||clear')
    print(dedent(f"""
    
    You are a lumberjack named {Hname} that lives in the woods of Haxebis,
    a small peaceful kingdom in the continent of Andorias.
    Here, the winter is harshly dreadful, but the autumn is pretty nice.
    So, as usual, you are going to fish in the pond near the city and
    decided to take a few things with you.
    """))
    input(">>>")
    os.system('cls||clear')

    backpack_list, item_list = ItemSelection_1(Hname)

    backpack_list = ItemSelection_2(backpack_list, item_list)


    print(backpack_list)
    print("working till now")


def CreateClassName():

    os.system('cls||clear')
    print("You are a lumberjack named...")
    Hname = input("""\nPlease imput your name, up to 20 characters:"
>>>""")
    
    if len(Hname) == 0:
        print("\nSince you didn't type any name, You are going to be called Rudolfos")
        
        decision_name = input(dedent("""
        Type 1, if you are ok with it or 2 if you want to input your name again
        
        >>>"""))

        while len(decision_name) == 0:

            os.system('cls||clear')
            decision_name = input(dedent("""
            Invalid answer, please, type 1 if you
            want to continue with the default name or 
            2 if you want to type your own

            >>>"""))

        while int(decision_name) != 1 and int(decision_name) != 2:

            os.system('cls||clear')
            decision_name = input(dedent("""
            Invalid answer, please, type 1 if you
            want to continue with the default name or 
            2 if you want to type your own

            >>>""")) 

        if int(decision_name) == 1:
            Hname = "Rudolfos" 
        
        else:
            os.system('cls||clear')
            Hname = input(dedent("""
            Please, Input your name
            
            >>>"""))
            
            if len(Hname) == 0:
                os.system('cls||clear')
                print("So, you are called Rudolfos!")
                Hname = "Rudolfos"

            else:
                os.system('cls||clear')


    while len(Hname) > 20:
        os.system('cls||clear')
        print("""Your name is longer than 20 characters""")
        Hname = input(dedent("""Please, input another
        
        >>>"""))
    
    return Hname


def ItemSelection_1(Hname):
    print(dedent(f"""
    You only have a small amount of space in your backpack,
    (able to chose 2 items) so, be smart.
            ------------------------------
    1. Arrows and Bow
    2. Flintch
    3. chef's knife
    4. Grilled Lambs leg
    5. Lucky Token
            ------------------------------
    """))
    
    item_list = {
                1 : {
                    'item_value'       : '1',
                    'item_name'        : 'Item_arrows and bow',
                    'item_description' : dedent(f""" A gift from your father, your old and realiable arrow. 
        Excelent for hunting, allows you to attack from afar, normaly guaranteeing you 
        with first hits """)
                    },

                2 : {
                    'item_value'       : '2',
                    'item_name'        : 'item_Flintch',
                    'item_description' : 'A stone used to start fires, always good to have one around!'
                    },

                3 : {
                    'item_value'        : '3',
                    'item_name'         : "item_chef's knife",
                    'item_description'  : dedent(f"""
                    \bA long knife normally used for kitchen purpouses. 
                    You could really chop a bone with it.""")
                    },

                4 : {
                    'item_value'        : '4',
                    'item_name'         : 'item_Grilled Lambs leg',
                    'item_description'  : "A delicious lamb leg, can feed you for 4 meals"
                    },

                5 : {
                    'item_value'        : '5',
                    'item_name'         : 'iten_Luck token',
                    'item_description'  : "A token that grants you extra luck"
                    }

    }

    chosen_item_1 = int(input("""Chose an item from the previous menu:
>>>"""))
    os.system('cls||clear')

    while (chosen_item_1 != 1 and chosen_item_1 != 2 and chosen_item_1 != 3
            and chosen_item_1 != 4 and chosen_item_1 != 5):
        os.system('cls||clear')
        chosen_item_1 = int(input("""To choose an item, type an number from 1 to 5
            ------------------------------
    1. Arrows and Bow
    2. Flintch
    3. chef's knife
    4. Grilled Lambs leg
    5. Lucky Token
            ------------------------------
>>>"""))

    print(item_list[chosen_item_1]['item_name'], "\n", 
    item_list[chosen_item_1]['item_description'])
    chosen_item_1_confirm = input(dedent(f"""
Do you really want to keep this item?
    1. yes
    2. no

>>>"""))
    os.system('cls||clear')
    if int(chosen_item_1_confirm) == 1:
        print(f"{item_list[chosen_item_1]['item_name']} added to the backpack")
        backpack_list = []
        backpack_list.append(item_list[chosen_item_1]['item_name'])
        item_list.pop(chosen_item_1)
        
        return (backpack_list, item_list)

    if int(chosen_item_1_confirm) == 2:
        ItemSelection_1(Hname)
    
    else:
        print("Invalid answer!")
        ItemSelection_1(Hname)


def ItemSelection_2(backpack_list, item_list):
    
    x = (list(item_list)[0], list(item_list)[1], list(item_list)[2], list(item_list)[3])

    chosen_item_2 = int(input(f"""
    From the remaining itens, chose another one to take with you in your adventure:
            ------------------------------
    1. {item_list[x[0]]['item_name']}
    2. {item_list[x[1]]['item_name']}
    3. {item_list[x[2]]['item_name']}
    4. {item_list[x[3]]['item_name']}
            ------------------------------
    >>>"""))
    os.system('cls||clear')
    chosen_item_2 -= 1 #so we can use the item index in X
    #similar loop from ItemSelection_1, to only allow values from the selected range...
    while (chosen_item_2 != 1 and chosen_item_2 != 2 and chosen_item_2 != 3
            and chosen_item_2 != 4):
        os.system('cls||clear')
        chosen_item_2 = int(input(f"""To choose an item, type an number from 1 to 4
           ------------------------------
    1. {item_list[x[0]]['item_name']}
    2. {item_list[x[1]]['item_name']}
    3. {item_list[x[2]]['item_name']}
    4. {item_list[x[3]]['item_name']}    
            ------------------------------
>>>"""))

    print(item_list[x[chosen_item_2]]['item_name'], "\n", 
    item_list[x[chosen_item_2]]['item_description'])
    chosen_item_2_confirm = input(dedent(f"""
Do you really want to keep this item?
    1. yes
    2. no

>>>"""))

    os.system('cls||clear')
    if int(chosen_item_2_confirm) == 1:
        print(f"{item_list[x[chosen_item_2]]['item_name']} added to the backpack")
        backpack_list.append(item_list[x[chosen_item_2]]['item_name'])
        item_list.pop(x[chosen_item_2])
        
        return (backpack_list)

    if int(chosen_item_2_confirm) == 2:
        ItemSelection_2(backpack_list, item_list)
    
    else:
        print("Invalid answer!")
        ItemSelection_2(backpack_list, item_list)







def is_dead():
    if health < 1:
        return True

    else:
        return False 

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implemente enter()")
        exit(1)


class House(Scene):

    print("House")
    pass


class Forest(Scene):

    pass


class Map(object):

   scenes_dic = {
       1 : House(),
       2 : Forest()
   }
   
   def enter_scene():
       pass


map_start = Map()

map_start.scenes_dic[1]



CreateClass()