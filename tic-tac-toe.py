# box that contains the game
box = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# displaying matrix
def displayBox():
    for i in range(len(box)):
        for j in range(len(box[i])):
            if j != len(box[i]) - 1:
                print(box[i][j], end=" | ")
            else:
                print(box[i][j])
        if i != len(box) - 1:
            print("----------")
        else:
            print()

print("*** TIC TAC TOE ***\n")
displayBox()

# winner variables
o_wins = 0
x_wins = 0
draw = 0

# list for storing positions of x and o in the box
o_arr = []
x_arr = []

# input o
def inputO():
    valid = True
    while valid==True:
        print("*** o player turn ***")
        o_row = int(input("Enter row: ")) - 1
        o_col = int(input("Enter column: ")) - 1
        
        # if space not taken
        if [o_row, o_col] not in o_arr and [o_row, o_col] not in x_arr:
            box[o_row][o_col] = "O"
            o_arr.append([o_row, o_col])
            o_arr.sort()
            print()
            displayBox()
            valid = False
        else:
            print("Space Taken")
            continue

# input x
def inputX():
    valid = True
    while valid:
        print("*** x player turn ***")
        x_row = int(input("Enter row: ")) - 1
        x_col = int(input("Enter column: ")) - 1
        
        # if space not taken
        if [x_row, x_col] not in o_arr and [x_row, x_col] not in x_arr:
            box[x_row][x_col] = "X"
            x_arr.append([x_row, x_col])
            x_arr.sort()
            print()
            displayBox()
            valid = False
        else:
            print("Space Taken")
            continue

# checking
def check():
    # for o
    for i in range(len(o_arr) - 2):
        for j in range(i+1, len(o_arr) - 1):
            for k in range(j+1, len(o_arr)):
                if o_arr[i][1]+o_arr[j][1]+o_arr[k][1]==3 and o_arr[i][0]==o_arr[j][0] and o_arr[j][0]==o_arr[k][0] or o_arr[i][0]+o_arr[j][0]+o_arr[k][0]==3 and o_arr[i][1]==o_arr[j][1] and o_arr[j][1]==o_arr[k][1] or o_arr[i][0]==o_arr[i][1] and o_arr[j][0]==o_arr[j][1] and o_arr[k][0]==o_arr[k][1] or o_arr[i][0]+o_arr[i][1]==2 and o_arr[j][0]+o_arr[j][1]==2 and o_arr[k][0]+o_arr[k][1]==2:
                    return 1, 0
    
    # for x
    for i in range(len(x_arr) - 2):
        for j in range(i+1, len(x_arr) - 1):
            for k in range(j+1, len(x_arr)):
                if x_arr[i][1]+x_arr[j][1]+x_arr[k][1]==3 and x_arr[i][0]==x_arr[j][0] and x_arr[j][0]==x_arr[k][0] or x_arr[i][0]+x_arr[j][0]+x_arr[k][0]==3 and x_arr[i][1]==x_arr[j][1] and x_arr[j][1]==x_arr[k][1] or x_arr[i][0]==x_arr[i][1] and x_arr[j][0]==x_arr[j][1] and x_arr[k][0]==x_arr[k][1] or x_arr[i][0]+x_arr[i][1]==2 and x_arr[j][0]+x_arr[j][1]==2 and x_arr[k][0]+x_arr[k][1]==2:
                    print(x_arr[i],x_arr[j],x_arr[k])
                    return 0, 1
    
    # draw case
    return 0, 0

# loop till any of the case is true
while o_wins==0 and x_wins==0 and draw==0:
    inputO()

    # checking draw case
    if len(o_arr) > 4:
        draw = 1

    # checking for win
    if len(o_arr) > 2:
        o_wins, x_wins = check()
    
    # if no one is wining then continue to take inputs for x
    if o_wins==0 and x_wins==0:
        inputX()

        # checking draw case
        if len(x_arr) == 4:
            draw=1
        
        # checking for win
        if len(x_arr) > 2:
            o_wins, x_wins = check()

# printing the result
if o_wins == 1:
    print("*** o wins ***")
elif x_wins == 1:
    print("*** x wins ***")
else:
    print("*** match draw ***")