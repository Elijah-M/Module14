"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/23/2020
This is a Hangman game, the GUI is completed via tkinter
"""

from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image


root = Tk()  # Creates the window
root.title("Let's Play HangMan!")  # The window title
root.geometry("1200x720")  # Sets the size of the window
root['bg'] = 'gray'  # Sets the background color for the window


def window_close():
    """
    If the user closes the window a message box appears to make sure they wanted to or not
    :return:
    """
    response = messagebox.askokcancel(title="Exit?",
                                      message="Are you sure you want to close the program?")
    if response == True:
        root.destroy()  # Closes the window
        #  Else: The program continues as normal


# If the uses closes out the window a message occurs
root.protocol("WM_DELETE_WINDOW", window_close)


COLSPAN = 8  # The column span

# Changes the font to something that'll work for the title wording below
default_font = font.nametofont("TkFixedFont")
default_font.configure(size=8)
root.option_add("*Font", default_font)

# The title of the game
lbl_title = Message(root,
                    text=
                    "                                                #####\n"
                    "                                               /#  #\n"
                    "  ####           ############    ############  /# #   #####\n"
                    " /#  #          /#          #   /#          #  /##  /#      #\n"
                    " /#  #          /#  #########   /####    ####  /## /#   ##   #\n"
                    " /#  #          /#  #///////    ////#    #//   //  /#  #//#  #\n"
                    " /#  #          /#  #####          /#    #         /#    # ###\n"
                    " /#  #          /#      #          /#    #         ///#   #//\n"
                    " /#  #          /#  #####          /#    #           //#    #\n"
                    " /#  #          /#  #///           /#    #         ####//#   #\n"
                    " /#  ########   /#  #########      /#    #        /#   ##    #\n"
                    " /#         #   /#          #      /#    #        /#        #\n"
                    " /###########   /############      /######        //########\n"
                    " ///////////    ////////////       //////          ////////\n"
                    "  #########      ####                  #        #####   #####\n"
                    " /#        #    /#  #                 # #      /#   #  /#   #\n"
                    " /#   ###   #   /#  #                #   #     /#   #  /#   #\n"
                    " /#   #/#   #   /#  #               #     #     /#  #####  #\n"
                    " /#   ##   #    /#  #              #  ##   #     /#       #\n"
                    " /#       #     /#  #             #  # /#   #      /#   #\n"
                    " /#   ####      /#  #            #  ######  #      /#   #\n"
                    " /#   #//       /#  #           /#          #      /#   #\n"
                    " /#   #         /#  #########   /#  ######  #      /#   #\n"
                    " /#   #         /#          #   /#  #////#  #      /#   #\n"
                    " /#####         /############   /####   /####      /#####\n"
                    " /////          ////////////    ////    ////       /////\n"
                    "  ####    ####          #          ####    ####      ##########\n"
                    " /#  #   /#  #         # #        /#   #  /#  #    /#          #\n"
                    " /#  #   /#  #        #   #       /#    # /#  #    /#  #####   #\n"
                    " /#  #   /#  #       #     #      /#     #/#  #    /#  #///#####\n"
                    " /#  ######  #      #  ##   #     /#      ##  #    /#  #  /////\n"
                    " /#          #     #  # /#   #    /#  #    #  #    /#  #   #####\n"
                    " /#  ######  #    #  ######  #    /#  ##      #    /#  #  /##  #\n"
                    " /#  #////#  #   /#          #    /#  #/#     #    /#  #  ///# #\n"
                    " /#  #   /#  #   /#  ######  #    /#  # /#    #    /#  ####### #\n"
                    " /#  #   /#  #   /#  #////#  #    /#  #  /#   #    /#          #\n"
                    " /####   /####   /####   /####    /####   /####    //##########\n"
                    " ////    ////    ////    ////     ////    ////      //////////\n"
                    "  ###      ###          #          ####    ####\n"
                    " /#  #    #  #         # #        /#   #  /#  #\n"
                    " /#   #  #   #        #   #       /#    # /#  #\n"
                    " /#    ##    #       #     #      /#     #/#  #\n"
                    " /#     #    #      #  ##   #     /#      ##  #\n"
                    " /#  #     # #     #  # /#   #    /#  #    #  #\n"
                    " /#  ##   ## #    #  ######  #    /#  ##      #\n"
                    " /#  #/# #/# #   /#          #    /#  #/#     #\n"
                    " /#  # /# /# #   /#  ######  #    /#  # /#    #\n"
                    " /#  # // /# #   /#  #////#  #    /#  #  /#   #\n"
                    " /####    /###   /####   /####    /####   /####\n"
                    " ////     ///    ////    ////     ////    ////   Author: Elijah Morishita\n"
                    "                                                         elmorishita@dmacc.edu",
                    anchor='n',
                    bg="gray",
                    fg="white"
                    ).grid(sticky=NW, rowspan=84)  # Left Justified, spanning 30 rows

img_main_menu = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\main-menu.png")
lbl_menu = Label(root, image=img_main_menu).grid(row=0, column=1, sticky=N, columnspan=COLSPAN)  # The menu label

lbl_please_enter = Label(root, justify=LEFT, text="#1\nClick on START NEW GAME to begin.", bg="gray", fg="white")
lbl_please_cont = Label(root, justify=LEFT, text="#2\nEnter a word or phrase in the above entry field."
                                                 "\n#3\nPress ENTER to begin :)"
                                                 "\n(#4)\nPress CLEAR to try again if required :\\",
                        bg="gray", fg="white")

lbl_please_enter.grid(row=24, column=1, columnspan=COLSPAN, sticky=W, pady=1)
lbl_please_cont.grid(row=40, column=1, columnspan=COLSPAN, sticky=W, pady=1)

# This forces all entry to become upper-case, and gives a maximum character amount
a_variable = StringVar()
MAX_CHARACTERS = 25


def capitolize():
    """
    Automatically capitalizes the user input
    :return:
    """
    a_variable.set(a_variable.get().upper())


def maximum():
    """
    Checks for the max entry of characters from the user
    :return:
    """
    if len(a_variable.get()) > MAX_CHARACTERS:
        messagebox.showwarning(title="Max Characters Exceeded!",
                               message="Please enter no more than 25\n"
                                       "characters, thanks.")
        clear_box()  # Clears the entry field


bad_input = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '1', '2',
             '3', '4', '5', '6', '7', '8', '9', '0', ';', ':', '\'', '"', '\\', ',' '<', '>', '/', '?',
             '[', '{', '}', ']']
length_of_bad_input = len(bad_input)


def check_input(the_user_entry):
    """
    Checks the user's input, throws an error if they enter the wrong character
    :param the_user_entry:
    :return:
    """
    try:
        for z in range(length_of_bad_input):
            if bad_input[z] == the_user_entry:
                messagebox.showwarning(title="Invalid input!",
                                       message="The following characters are forbidden:\n"
                                               "~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/1234567890")
                clear_box()
                raise ValueError
    except ValueError:
        print("The user entered an invalid character in the entry box\n"
              "potentially one of the following:\n"
              "~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/1234567890")


# The entry box for user input of what the user would like to use for the upcoming game
text_box = Entry(root, relief=FLAT, width=38, textvariable=a_variable)
text_box.grid(row=32, column=1, columnspan=COLSPAN, pady=1)

# This label is created and destroyed to check in start_game() if the ENTER button was pressed before START NEW GAME
blank_labels = Label(root)
blank_labels.destroy()


def get_input():
    """
    This function gathers user input and converts the chars to blanks (underscores)
    and blank spaces to newlines.  It also grays out the ENTER button and entry field
    :return:
    """
    answer = text_box.get()  # for converting the string into chars
    check_input(answer)  # Makes sure the user entered good input
    capitolize()  # Makes all chars in uppercase
    global original_user_entry
    original_user_entry = text_box.get()
    convert = []
    length_of_entry = len(text_box.get())
    #  length_of_chars_only is used to determine the winner of the game
    global length_of_chars_only
    length_of_chars_only = length_of_entry
    for v in answer:
        if v == ' ':
            length_of_chars_only -= 1
    # Checks to make sure the user entered something in the entry box before pressing the ENTER button
    if length_of_entry == 0:
        messagebox.showwarning(title="Whoops!", message="Looks like you forgot to enter a word/phrase\n"
                                                        "in the entry field, please enter 1 - " + str(MAX_CHARACTERS) +
                                                        " characters\n"
                                                        "and then press ENTER :\\")
    else:
        # first convert the string into ' _ ' and newlines in place of spaces
        for x in range(length_of_entry):
            if answer[x] == ' ':
                convert.append('\n')
            else:
                convert.append(' _')
        # then for the sake of removing the {}, convert it all back into a string
        global return_to_string
        return_to_string = ""
        for x in convert:
            return_to_string += x

        # prints out the "blank" spaces based on the length of user input
        global blank_labels  # Made this global so it can be destroyed via the clear_box function
        blank_labels = Label(root, text=return_to_string, bg="gray", fg="white")
        blank_labels.grid(row=65, column=9, rowspan=19, columnspan=2, sticky='NESW', pady=6)
        enter_button['state'] = DISABLED  # disables the ENTER button to stop multiple labels
        convert.clear()  # Clears the content of convert
        if len(a_variable.get()) > MAX_CHARACTERS:  # If the Max characters is exceeded it clears their entry
            maximum()
        else:
            text_box.delete(0, 'end')  # clears the entry box so the other player can't see it
            text_box.config(state='disabled')  # disables the entry box (grays out the text)


enter_button = Button(root, text="ENTER", command=get_input)  # The ENTER Button
enter_button.grid(row=48, column=1, sticky=NE, columnspan=6, rowspan=8, pady=4)


def clear_box():
    """
    This just deletes the blank_label Label (the ___'s), it also clears the entry field
    and enables the ENTER button
    :return:
    """
    blank_labels.destroy()
    enter_button['state'] = NORMAL  # enables the ENTER button
    text_box.config(state='normal')  # enables the entry box
    text_box.delete(0, 'end')  # clears the entry box


clear_button = Button(root, text="CLEAR", command=clear_box)
clear_button.grid(row=48, column=7, sticky=NW, columnspan=2, rowspan=8, pady=4)

lets_begin = Label(root, justify=LEFT, text="#5\n"
                                            "Click on the letters below to try\n"
                                            "and guess the hidden word or phrase.\n"
                                            "********** BE WARNED! **********\n"
                                            "You only have SIX chances\n"
                                            "before it's GAME OVER :(",
                                            bg="gray", fg="white")
lets_begin.grid(row=56, column=1, columnspan=COLSPAN, rowspan=24, pady=1, sticky=W)


game_over = 0  # Used in alphabet_press() to determine the game_over count
correct_guess_count = 0  # Used in alphabet_press() to determine the correct_guess_count
LEFT_COL = 9
RIGHT_COL = 10

# Placing the main LOSER image, the following Labels just cover up the main image
ws_img = Image.open(
    r"C:\Users\Owner\PycharmProjects\Module14\lose_image/Lose.png")  # open the image
resized_wsl_img = ws_img.resize((300, 500),
                                 Image.ANTIALIAS)  # resize the image + makes sure borders are ok
lose_whole_self_img = ImageTk.PhotoImage(resized_wsl_img)  # assign the newly resized image
losing_lbl_zero = Label(root, image=lose_whole_self_img, bg="gray", fg="white", anchor="e")  # Create the label
losing_lbl_zero.photo = lose_whole_self_img  # Assign the img to the label (pic is blank w/o this)
losing_lbl_zero.grid(row=0, column=LEFT_COL, rowspan=80, columnspan=2, sticky=N)

losing_lbl_one = Label(root, bg="gray", fg="white")  # Create the label
losing_lbl_two = Label(root, bg="gray", fg="white")  # Create the label
losing_lbl_three = Label(root, bg="gray", fg="white")  # Create the label
losing_lbl_four = Label(root, bg="gray", fg="white")  # Create the label
losing_lbl_five = Label(root, bg="gray", fg="white")  # Create the label
losing_lbl_six = Label(root, bg="gray", fg="white")  # Create the label

# Uncovers the left Leg
losing_lbl_one.grid(row=0, column=LEFT_COL, rowspan=15, sticky='NESW')
# Uncovers the Right Leg
losing_lbl_two.grid(row=0, column=RIGHT_COL, rowspan=15, sticky='NESW')
# Uncovers the Chest
losing_lbl_three.grid(row=15, column=LEFT_COL, columnspan=2, rowspan=13, sticky='NESW')
# Uncovers the Left Arm
losing_lbl_four.grid(row=28, column=LEFT_COL, rowspan=14, sticky='NESW')
# Uncovers the Right Arm
losing_lbl_five.grid(row=28, column=RIGHT_COL, rowspan=14, sticky='NESW')
# Uncover the Head image
losing_lbl_six.grid(row=42, column=LEFT_COL, columnspan=2, rowspan=23, sticky='NESW')


def recovery():
    # Uncovers the left Leg
    losing_lbl_one.grid(row=0, column=LEFT_COL, rowspan=15, sticky='NESW')
    # Uncovers the Right Leg
    losing_lbl_two.grid(row=0, column=RIGHT_COL, rowspan=15, sticky='NESW')
    # Uncovers the Chest
    losing_lbl_three.grid(row=15, column=LEFT_COL, columnspan=2, rowspan=13, sticky='NESW')
    # Uncovers the Left Arm
    losing_lbl_four.grid(row=28, column=LEFT_COL, rowspan=14, sticky='NESW')
    # Uncovers the Right Arm
    losing_lbl_five.grid(row=28, column=RIGHT_COL, rowspan=14, sticky='NESW')
    # Uncover the Head image
    losing_lbl_six.grid(row=42, column=LEFT_COL, columnspan=2, rowspan=23, sticky='NESW')

def game_over_remove_labels(game_over):
    """
    This handles the losing scenario
    :param game_over:
    :return:
    """
    if game_over >= 1:
        losing_lbl_one.grid_forget()  # place left leg on the grid
    if game_over >= 2:
        losing_lbl_two.grid_forget()  # place right leg on the grid
    if game_over >= 3:
        losing_lbl_three.grid_forget()  # place chest on the grid
    if game_over >= 4:
        losing_lbl_four.grid_forget()  # place left arm on the grid
    if game_over >= 5:
        losing_lbl_five.grid_forget()  # place right arm on the grid
    if game_over >= 6:  # GAME OVER
        losing_lbl_six.grid_forget()  # place head on the grid
        messagebox.showerror(title="GAME OVER", message="GAME OVER\n"
                                                        "Aw shucks, maybe next time :(")
        play_again()  # Asks if they'd like to play again
        enter_button['state'] = NORMAL  # re-enables the ENTER button
        text_box.config(state='normal')  # re-enables the entry box


#  Creating the winning image
winning_img = Image.open(
    r"C:\Users\Owner\PycharmProjects\Module14\win_image\win.png")  # open the WINNER image
resized_winning_img = winning_img.resize((300, 500),
                                         Image.ANTIALIAS)  # resize the image + makes sure borders are ok
winning_img_main_img = ImageTk.PhotoImage(resized_winning_img)  # assign the newly resized image
winning_lbl_zero = Label(root, image=winning_img_main_img, bg="gray", fg="white", anchor="e")  # Create the label
winning_lbl_zero.photo = winning_img_main_img  # Assign the img to the label (pic is blank w/o this)


def play_again():
    their_answer = messagebox.askyesno(title="Play Again?",
                                       message="Would you like to play again?")
    if their_answer == True:  # Yes
        losing_lbl_zero.grid(row=0, column=LEFT_COL, rowspan=80, columnspan=2, sticky='NESW')
        cover_up = Label(root, bg="gray", fg="gray")  # creates a label to cover up the answer area
        cover_up.grid(row=65, column=9, rowspan=19, columnspan=2, sticky='NESW')
        enter_button['state'] = NORMAL  # re-enables the ENTER button
        text_box.config(state='normal')  # re-enables the entry box
        recovery()
        winning_lbl_zero.grid_forget()
    else:
        root.destroy()  # Closes the window

def winner():
    messagebox.showinfo(title="**** WINNER! ****", message="CONGRATS!!\n"
                                                           "You figured out the word/phrase\n"
                                                           "before it was too late, clearly your\n"
                                                           "guessing skills are unfathomable")
    winning_lbl_zero.grid(row=0, column=LEFT_COL, rowspan=80, columnspan=2, sticky=N)  # Placing the winning image
    play_again()  # Finds out if they'd like to play again


new_blank_labels = Label(root, bg="gray", fg="white")  # Update the Blanks label

make_to_string = ""  # Used for creating a global string in alphabet_press()
past_first_iteration = True
strike_one = []  # Used to determine if the user clicks on the same letter more than once
first_strike_through = False


def multiple_letters_check(user_letter_pick):
    """
    This checks if the user clicked on the same letter multuple times
    :param user_letter_pick:
    :return:
    """
    if first_strike_through == True:  # Makes sure this isn't done on the first iteration
        # Checks to see if the user clicked on the same letter twice
        try:
            for q in strike_one:
                print("q: ", q, "user_letter_pick: ", user_letter_pick)
            if q == user_letter_pick:
                messagebox.showwarning(title="Duplicate Letter Choice!",
                                       message="You already tried that one, please\n"
                                               "choose another letter.")
                raise ValueError  # returns False, the user entered the same letter
            else:
                return True  # They picked a different letter
        except ValueError:
            print("The user entered the same letter twice")
            return False
    return True  # They picked a different letter


def alphabet_press(user_letter_pick):
    """
    This function implements most of the game logic via pressing the A - Z buttons
    :param user_letter_pick:
    :return:
    """
    # Checks to see if the START NEW GAME button was successfully pressed w/o error
    if lets_begin.winfo_exists() != 1:
        messagebox.showwarning(title="Pump the brakes!", message="It appears you've gotten a bit ahead of\n"
                                                                 "yourself, though your eagerness is appreciated\n"
                                                                 "please follow procedure :\\")
    else:
        attempt = multiple_letters_check(user_letter_pick)
        if attempt == True:  # Checks if the user entered the same letter
            global first_strike_through
            first_strike_through = True
            global past_first_iteration
            global make_to_string
            if past_first_iteration == True:
                b_label = []
                blanks = return_to_string  # Just giving it a name with better context
            else:
                b_label = []
                blanks = make_to_string
            for n in blanks:  # Creating a list of chars from the string of blanks
                b_label += n
            conversion = []  # used to combine the original entry into a string with " " in between the chars
            global original_user_entry
            original_entry_length = len(original_user_entry)
            # create a string of the original entry + " _"
            for h in range(original_entry_length):  # create a string of the original entry + " " to gain the length
                conversion.append(" ")
                conversion.append(original_user_entry[h])
            # Removes any additional spaces from the end
            ending = False
            while ending == False:
                if conversion[-1] == ' ':
                    del conversion[-1]
                if conversion[-1] != ' ':
                    ending = True
            # '\n' chars get converted to double blanks ' ' + ' ' ==========================
            # So the below for loop removes one of those ' '
            then_a_space = 0
            length_of_conversion = len(conversion)
            deletion_list = []
            for o in range(length_of_conversion):
                if conversion[o] == ' ':
                    then_a_space += 1
                if conversion[o] != ' ':
                    then_a_space = 0
                if then_a_space == 2:
                    # takes out the needed index for removal since I can't del an index in a for loop
                    deletion_list.append(o)
            length_of_deletion_list = len(deletion_list)
            del_iteration = 1
            for u in range(length_of_deletion_list):
                del conversion[deletion_list[u]]
                if u+1 == length_of_deletion_list:  # to avoid an index error as u would become too high in the last portion
                    continue
                deletion_list[u+1] -= del_iteration
                del_iteration += 1
            # ===========================================================================
            global game_over
            global correct_guess_count
            global blank_labels
            global new_blank_labels
            good_guess = FALSE
            j = 0
            for letters in conversion:  # This loop checks if the user's pick matches any of the letters from the original entry
                if letters == ' ':
                    j += 1
                    continue  # skips an iteration
                if letters == alphabet[user_letter_pick]:  # If the user guesses the correct letter
                    b_label[j] = alphabet[user_letter_pick]  # Assign the letter corresponding spot in the string
                    make_to_string = ""  # resets the variable
                    for c in b_label:  # this conversion back to a string is to make the labels look better
                        make_to_string += c
                    new_blank_labels = Label(root, text=make_to_string, bg="gray", fg="white")  # Update the Blanks label
                    new_blank_labels.grid(row=65, column=9, rowspan=19, columnspan=2, sticky='NESW')
                    past_first_iteration = False  # Causes make_to_string to hold its value
                    good_guess = TRUE  # The player guessed the right letter
                    correct_guess_count += 1
                    if correct_guess_count == length_of_chars_only:  # The User wins the game!!
                        # Clears this info
                        make_to_string = ""
                        correct_guess_count = 0
                        b_label.clear()
                        blanks = ""
                        conversion.clear()
                        j = 0
                        past_first_iteration = True
                        first_strike_through = False
                        strike_one.clear()
                        winner()  # Let's the player know they won and displays the winner graphic
                j += 1
            if good_guess == FALSE:  # The player guessed the wrong letter
                game_over += 1
                if game_over >= 6:
                    # Clears this info
                    make_to_string = ""
                    b_label.clear()
                    blanks = ""
                    conversion.clear()
                    j = 0
                    past_first_iteration = True
                    first_strike_through = False
                    strike_one.clear()
                game_over_remove_labels(game_over)  # Removes the labels based on the parameters
                if game_over >= 6:
                    game_over = 0
                    correct_guess_count = 0
        strike_one.append(user_letter_pick)


def change_start_button(event):
    """
    This function performs the first portion of a mouse rollover, changing the image
    :param event:
    :return:
    """
    img_start_button_mouse_over = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\start_new_game_raised_active.png")
    lbl_start_game.config(image=img_start_button_mouse_over)
    lbl_start_game.image = img_start_button_mouse_over
    lbl_start_game.grid(row=8, column=1, columnspan=COLSPAN, pady=6)


def change_back_start_button(event):
    """
    This function performs the 2nd portion of a mouse rollover, changing the image back to its
    original state
    :param event:
    :return:
    """
    img_start_button_mouse_over = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\start_new_game_raised_normal.png")
    lbl_start_game.config(image=img_start_button_mouse_over)
    lbl_start_game.image = img_start_button_mouse_over
    lbl_start_game.grid(row=8, column=1, columnspan=COLSPAN, pady=6)


def on_click_start_button(event):
    """
    This function performs the on-click portion, changing the image to look "pressed"
    :param event:
    :return:
    """
    img_start_button_on_click = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\start_new_game_pressed_normal.png")
    lbl_start_game.config(image=img_start_button_on_click)
    lbl_start_game.image = img_start_button_on_click
    lbl_start_game.grid(row=8, column=1, columnspan=COLSPAN, pady=8)  # Uses more padding b/c the image is smaller
    place_holder.destroy()  # Removes the place holder


def release_click_start_button(event):
    """
    This function performs reverses the on-click portion
    :param event:
    :return:
    """
    img_start_button_release_click = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\start_new_game_raised_active.png")
    lbl_start_game.config(image=img_start_button_release_click)
    lbl_start_game.image = img_start_button_release_click
    lbl_start_game.grid(row=8, column=1, columnspan=COLSPAN, pady=6)


img_start_button = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\start_new_game_raised_normal.png")
lbl_start_game = Label(root, image=img_start_button, bg="gray", fg="white")
lbl_start_game.grid(row=8, column=1, sticky=S, columnspan=COLSPAN, pady=6)

lbl_start_game.bind("<Enter>", change_start_button)  # Mouse Rollover ("entering" the image area), uses the change method
lbl_start_game.bind("<Leave>", change_back_start_button)  # Mouse Rollover ("leaving" the image area), uses the change_back method
lbl_start_game.bind("<Button-1>", on_click_start_button)  # On-click the button appears to depress
lbl_start_game.bind("<ButtonRelease>", release_click_start_button)  # Once released the On-click is disregarded


# The options button
def change_options_button(event):
    """
    This function performs the first portion of a mouse rollover, changing the image
    :param event:
    :return:
    """
    img_option_button_mouse_over = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\options_raised_active.png")
    lbl_options.config(image=img_option_button_mouse_over)
    lbl_options.image = img_option_button_mouse_over
    lbl_options.grid(row=16, column=1, columnspan=COLSPAN, pady=6)


def change_back_options_button(event):
    """
    This function performs the 2nd portion of a mouse rollover, changing the image back to its
    original state
    :param event:
    :return:
    """
    img_option_button_mouse_return = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\options_raised_normal.png")
    lbl_options.config(image=img_option_button_mouse_return)
    lbl_options.image = img_option_button_mouse_return
    lbl_options.grid(row=16, column=1, columnspan=COLSPAN, pady=6)


def on_click_options_button(event):
    """
    This function performs the on-click portion, changing the image to look "pressed"
    :param event:
    :return:
    """
    img_options_button_on_click = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\options_pressed_normal.png")
    lbl_options.config(image=img_options_button_on_click)
    lbl_options.image = img_options_button_on_click
    lbl_options.grid(row=16, column=1, columnspan=COLSPAN, pady=8)  # Uses more padding b/c the image is smaller

def release_click_options_button(event):
    """
    This function performs reverses the on-click portion
    :param event:
    :return:
    """
    img_options_button_release_click = PhotoImage(
        file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\options_raised_active.png")
    lbl_options.config(image=img_options_button_release_click)
    lbl_options.image = img_options_button_release_click
    lbl_options.grid(row=16, column=1, columnspan=COLSPAN, pady=6)


img_option_button = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\options_raised_normal.png")
lbl_options = Label(root, image=img_option_button, bg="gray", fg="white")
lbl_options.grid(row=16, column=1, sticky=N, columnspan=COLSPAN, pady=6)

lbl_options.bind("<Enter>", change_options_button)  # Mouse Rollover ("entering" the image area), uses the change method
lbl_options.bind("<Leave>", change_back_options_button)  # Mouse Rollover ("leaving" the image area), uses the change_back method
lbl_options.bind("<Button-1>", on_click_options_button)  # On-click the button appears to depress
lbl_options.bind("<ButtonRelease>", release_click_options_button)  # Once released the On-click is disregarded

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_length = len(alphabet)
buttons_abc = []  # A - Z normal button labels
image_abc = []  # A - Z button images (normal, raised)

# Creates labels and assigns images to them (normal raised)
for x in range(alpha_length):
    image_abc.append(PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\button_" + alphabet[x] + ".png"))
    buttons_abc.append(Label(root, image=image_abc[x], bg="gray", fg="white"))

buttons_abc_active = []  # A - Z active button labels
image_abc_active = []  # A - Z button images (active, raised)

# Creates labels and assigns images to them (active, raised)
for x in range(alpha_length):
    image_abc_active.append(PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\button_" + alphabet[x] + "3.png"))
    buttons_abc_active.append(Label(root, image=image_abc_active[x], bg="gray", fg="white"))

buttons_abc_pressed = []  # A - Z active button labels
image_abc_pressed = []  # A - Z button images (active, pressed)

# Creates labels and assigns images to them (active, pressed)
for x in range(alpha_length):
    image_abc_pressed.append(PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\button_" + alphabet[x] + "(1).png"))
    buttons_abc_pressed.append(Label(root, image=image_abc_pressed[x], bg="gray", fg="white"))

# The for loops place the A-Z buttons (Labels, Normal/Raised) onto a grid
ALPHA_ROW = 80
ALPHA_COL = 1


# Placing the letters in a grid, 3x rows of 8 + 1x row of 2
this_index = 0
for x in range(alpha_length):
    if this_index > 25:
        break
    for y in range(alpha_length):
        if this_index > 25:
            break
        buttons_abc[this_index].grid(row=ALPHA_ROW+x, column=ALPHA_COL+y, sticky=S, pady=2)
        this_index = this_index + 1
        if y >= 7:
            break


# Hides the letters until the START NEW GAME button has been pressed
place_holder = Label(root, bg="gray")
place_holder.grid(row=80, column=1, rowspan=4, columnspan=8, sticky="NESW")


def abc_s(abc_index, ALPHA_ROW, ALPHA_COL):
    def change_alphabet_buttons(event):
        """
        This function performs the first portion of a mouse rollover, changing the image
        :param event:
        :return:
        """
        another_image = image_abc_active[abc_index]
        a_label = buttons_abc[abc_index]
        a_label.config(image=another_image)
        a_label.image = another_image
        a_label.grid(row=ALPHA_ROW, column=ALPHA_COL, pady=2)

    def change_back_alphabet_button(event):
        """
        This function performs the 2nd portion of a mouse rollover, changing the image back to its
        original state
        :param event:
        :return:
        """
        img_alphabet_button_mouse_return = image_abc[abc_index]
        a_label = buttons_abc[abc_index]
        a_label.config(image=img_alphabet_button_mouse_return)
        a_label.image = img_alphabet_button_mouse_return
        a_label.grid(row=ALPHA_ROW, column=ALPHA_COL, pady=2)

    def on_click_alphabet_button(event):
        """
        This function performs the on-click portion, changing the image to look "pressed"
        :param event:
        :return:
        """
        img_alphabet_button_on_click = image_abc_pressed[abc_index]
        a_label = buttons_abc[abc_index]
        a_label.config(image=img_alphabet_button_on_click)
        a_label.image = img_alphabet_button_on_click
        a_label.grid(row=ALPHA_ROW, column=ALPHA_COL, pady=4)  # Uses more padding b/c the image is smaller
        alphabet_press(abc_index)  # Adds a letter if past the START NEW GAME button has been pressed


    def release_click_alphabet_button(event):
        """
        This function performs reverses the on-click portion
        :param event:
        :return:
        """
        another_image = image_abc_active[abc_index]
        a_label = buttons_abc[abc_index]
        a_label.config(image=another_image)
        a_label.image = another_image
        a_label.grid(row=ALPHA_ROW, column=ALPHA_COL, pady=2)


    buttons_abc[abc_index].bind("<Enter>", change_alphabet_buttons) # Mouse Rollover ("entering" the image area), uses the change method
    buttons_abc[abc_index].bind("<Leave>", change_back_alphabet_button)  # Mouse Rollover ("leaving" the image area), uses the change_back method
    buttons_abc[abc_index].bind("<Button-1>", on_click_alphabet_button)  # On-click the button appears to depress
    buttons_abc[abc_index].bind("<ButtonRelease>", release_click_alphabet_button)  # Once released the On-click is disregarded


#  For loops do NOT work with binding multiple Labels, even with lambda :(
#  So the result is 26x functions :\
abc_s(0, 80, 1)
abc_s(1, 80, 2)
abc_s(2, 80, 3)
abc_s(3, 80, 4)
abc_s(4, 80, 5)
abc_s(5, 80, 6)
abc_s(6, 80, 7)
abc_s(7, 80, 8)
abc_s(8, 81, 1)
abc_s(9, 81, 2)
abc_s(10, 81, 3)
abc_s(11, 81, 4)
abc_s(12, 81, 5)
abc_s(13, 81, 6)
abc_s(14, 81, 7)
abc_s(15, 81, 8)
abc_s(16, 82, 1)
abc_s(17, 82, 2)
abc_s(18, 82, 3)
abc_s(19, 82, 4)
abc_s(20, 82, 5)
abc_s(21, 82, 6)
abc_s(22, 82, 7)
abc_s(23, 82, 8)
abc_s(24, 83, 1)
abc_s(25, 83, 2)


mainloop()

root.mainloop()
