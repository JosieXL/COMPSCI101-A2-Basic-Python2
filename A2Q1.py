"""
Name: Xiaolin Li (Josie)
Username: xli556
ID number: 455398598
Description: This program is used to print out any sized multiplication table between 1 to 20 (inclusive).
"""
def display_heading(size, spaces):
    display_separator(size, spaces)
    title = str(size) + "x" + str(size) + " Times Table"
    print(get_word(title, (size+1) * spaces))
    print(get_row(0, size, spaces))
    display_separator(size, spaces)

def main():
    size = get_user_input()
    spaces = len(str(size * size)) + 2
    display_heading(size, spaces)
    display_table(size, spaces)
    display_separator(size, spaces)

def get_number(num, spaces):
    number = " " * (spaces - len(str(num))) + str(num)
    return number
    
def get_word(words, spaces):
    middle = (spaces - len(words)) // 2
    if (spaces - len(words)) % 2 != 0:
        words = " " * (middle +1) + words + " " * middle
    else:
        words = " " * middle  + words + " " * middle
    return words

def get_row(num, size, spaces):
    row = " "
    if num == 0: #heading part numbers
        if 1 <= size <= 3:
            row += spaces * " "
        else:
            row = spaces * " "
        row_value = 0
        while row_value != size:
            row_value = row_value + 1
            row += get_number(row_value, spaces)
        return row            
    else: #colomn part numbers in table
        if 1<= size <= 9:
            row = " " + str(num) + " " + "|"#The second " " is for the space between number and |
        elif size > 9: #when size > 9, space need to -1 behind the numbers
            if 1<= num <= 9:
                row = "  " + str(num) + " " + "|"
            else:
                row = " " + str(num) + " " + "|"
        row_value = 0
        while row_value != size:
            row_value = row_value + 1
            row += get_number(row_value * num, spaces)
        return row
    
def display_separator(size, spaces):
    seperators = "-" * ((size + 1) * spaces)
    print(seperators)

def display_table(size, spaces):
    for row in range(1, (size + 1)): #size+1 make sure the funciton print out value including size.
        print(get_row(row, size, spaces))
                     
def get_user_input():
    size = int(input("Enter the size of the multiplication table (1-20): "))
    while not 1<= size <= 20:
        print("Table size should be between 1 and 20.")
        size = int(input("Please try again: "))
    return size
    
main()
