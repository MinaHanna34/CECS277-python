""" 
In this lab, I created a grid and allowed the player to move the triangle using numbers. The user must first input how big he wants his triangle then stars will appear showing his triangle. A menu will tell the player how to move then he can quit by pressing 5.
"""
import rectangle
import check_input
""" 
In display_grid it is a nested for loop that will go through each one and then print it out.


"""


def display_grid(grid):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()
    return


""" 
In the reset grid, I made a new list then it will reset it and add . to the list. I then return the grid.

"""


def reset_grid(grid):
    grid = []
    for i in range(20):
        list = []
        for j in range(20):
            list.append('.')
        grid.append(list)

    return grid


""" 
For place rect I add the width and height and I set x and y to ret . I then added a nested loop to go through all the width and height of the grid.
"""


def place_rect(grid, rect):
    width = rect.width
    height = rect.height
    x = rect.x
    y = rect.y
    for i in range(width):
        for j in range(height):
            grid[i + x][j + y] = "*"
    return


""" 
for our main, I mainly used it to display the functions and loop them. I add the menus and imported check input to check if what the user enters is invalid. I then made the controls for the grid and made the max 20to fix the out-of-bond error.
"""


def main():

    mGrid = []

    inputHeight = check_input.get_int_range("Enter rectangle height (1-5): ",
                                            1, 5)
    inputWidth = check_input.get_int_range("Enter rectangle width (1-5):", 1,
                                           5)

    r1 = rectangle.Rectangle(inputHeight, inputWidth)

    for i in range(20):
        list = []
        for j in range(20):
            list.append('.')
        mGrid.append(list)

    place_rect(mGrid, r1)
    display_grid(mGrid)

    condition = False

    while condition == False:
        print("Enter Direction:")
        print('1. Up')
        print('2. Down')
        print('3. Left')
        print('4. Right')
        print('5. Quit')

        userInput = check_input.get_int_range('', 1, 5)
        if userInput == 1:
            if r1.x == 0:
                print("Out of bounds")
                display_grid(mGrid)

            if r1.x != 0:
                r1.move_up()
                mGrid = reset_grid(mGrid)
                place_rect(mGrid, r1)
                display_grid(mGrid)

        elif userInput == 2:
            if r1.x + r1.height != 20:
                r1.move_down()
                mGrid = reset_grid(mGrid)
                place_rect(mGrid, r1)
                display_grid(mGrid)
            if r1.x + r1.height == 20:
                print("Out of bounds")
                display_grid(mGrid)

        elif userInput == 3:
            if r1.y == 0:
                print("Out of bounds")
                display_grid(mGrid)
            if r1.y != 0:
                r1.move_left()
                mGrid = reset_grid(mGrid)
                place_rect(mGrid, r1)
                display_grid(mGrid)

        elif userInput == 4:
            if r1.y + r1.width != 20:
                r1.move_right()
                mGrid = reset_grid(mGrid)
                place_rect(mGrid, r1)
                display_grid(mGrid)
            if r1.y + r1.width == 20:
                print("Out of bounds")
                display_grid(mGrid)

        elif userInput == 5:
            condition = True


main()
