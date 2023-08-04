import os
import time
positions = {
        "a":"a",
        "b":"b",
        "c":"c",
        "d":"d",
        "e":"e",
        "f":"f",
        "g":"g",
        "h":"h",
        "i":"i"
            }
def player_1():
    position = input("Player 1 (X)please enter the letter of the position$ ")
    position = str(position)
    if position == "a" or position == "b" or position == "c" or position == "d" or position == "e" or position == "f" or position == "g" or position == "h" or position == "i":
        if positions[position] != "X" and positions[position] !="O":
            positions[position] = "X"
            br = calculate(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
            #print(positions)
            return br
        elif positions[position] == "X" or positions[position] == "O":
            print("Position already taken try again ")
            player_1()
    else:
        print("Enter a correct position ")
        player_1()

def player_2():
    position = input("Player 2 (O)please enter the letter of the position$ ")
    position = str(position)
    if position == "a" or position == "b" or position == "c" or position == "d" or position == "e" or position == "f" or position == "g" or position == "h" or position == "i":
        if positions[position] != "X" and positions[position] !="O":
           positions[position] = "O"
           br = calculate(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
           #print(positions)
           return br
        elif positions[position] == "X" or positions[position] == "O":
            print("Position already taken try again ")
            player_2()
    else:
        print("Enter a correct position ")
        player_2()
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def print_box(a,b,c,d,e,f,g,h,i):
    print("          |          |          ")
    print(f"    {a}     |    {b}     |    {c}")
    print("__________|__________|__________")
    print("          |          |          ")
    print(f"    {d}     |    {e}     |    {f}")
    print("__________|__________|__________")
    print("          |          |          ")
    print(f"    {g}     |    {h}     |    {i}")
    print("          |          |          ")
    
def calculate(a,b,c,d,e,f,g,h,i):
    if (a == "X" and b =="X" and c == "X") or (d == "X" and e =="X" and f == "X")or (g == "X" and h =="X" and i == "X"):
        clear_screen()
        print("Player 1 Wins")
        return "break"
    elif (a == "O" and b =="O" and c == "O") or(d == "O" and e =="O" and f == "O")or(g == "O" and h =="O" and i == "O"):
        clear_screen()
        print("Player 2 Wins")
        return "break"
    elif (a == "X" and d == "X" and g=="X")or(b == "X" and e == "X"and h=="X")or (c=="X" and f =="X" and i=="X"):
        clear_screen()
        print("Player 1 Wins")
        return "break"
    elif (a == "O" and d == "O" and g=="O")or(b == "O" and e == "O"and h=="O")or (c=="O" and f =="O" and i=="O"):
        clear_screen()
        print("Player 2 Wins")
        return "break"
    elif (a=="X" and e=="X" and i =="X")or (c =="X"and e == "X"and g=="X"):
        clear_screen()
        print("Player 1 Wins")
        return "break"
    elif (a=="O" and e=="O" and i =="O")or (c =="O"and e == "O"and g=="O"):
        clear_screen()
        print("Player 2 Wins")
        return "break"
    elif a =="a"or b=="b" or c=="c" or d=="d"or e=="e" or f=="f" or g=="g" or h=="h" or i=="i":
        return "continue"
    else:
        clear_screen()
        return "no break"

if __name__ == "__main__":
    for i in range(1,10):
        clear_screen()
        print_box(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
        if i%2 == 0:
            br = player_2()
            if br == "break":
                print_box(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
                break
            elif br == "continue":
                continue
            else:
                print("Oh ho it looks like no one of you have won")
                print_box(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
        else:
            br = player_1()
            if br  == "break":
                print_box(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
                break
            elif br == "continue":
                continue
            else:
                print("Oh ho it looks like no one of you have won")
                print_box(positions["a"],positions["b"],positions["c"],positions["d"],positions["e"],positions["f"],positions["g"],positions["h"],positions["i"])
    input("Press anything to exit...")
                
