"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/23/2020
This is a Hangman game, the GUI is completed via tkinter
"""

import random
from tkinter import *
from tkinter import messagebox
from tkinter import font
import buttons
import lose_image
from PIL import ImageTk, Image


root = Tk()  # Creates the window
root.title("Let's Play HangMan!")  # The window title
root.geometry("1200x720")  # Sets the size of the window
root['bg'] = 'gray'  # Sets the background color for the window

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
                    " ////     ///    ////    ////     ////    ////    Author: Elijah Morishita\n"
                    "                                                          elmorishita@dmacc.edu",
                    anchor='n',
                    bg="gray",
                    fg="white"
                    ).grid(sticky=W, rowspan=27)  # Left Justified, spanning 30 rows

img_main_menu = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\main-menu.png")
lbl_menu = Label(root, image=img_main_menu).grid(row=0, column=1, sticky=N, columnspan=COLSPAN)  # The menu label

lbl_please_enter = Label(root, justify=LEFT, text="#1\nPlease enter a word or phrase below...", bg="gray", fg="white")
lbl_please_cont = Label(root, justify=LEFT, text="#2\nPress ENTER to register it"
                                                 "\n#3\nPress START NEW GAME to begin :)"
                                                 "\n(#4)\nPress CLEAR to try again if required :\\",
                        bg="gray", fg="white")

lbl_please_enter.grid(row=3, column=1, columnspan=COLSPAN, sticky=W, pady=1)
lbl_please_cont.grid(row=5, column=1, columnspan=COLSPAN, sticky=W, pady=1)

# The entry box for user input of what the user would like to use for the upcoming game
text_box = Entry(root, relief=FLAT, width=38)
text_box.grid(row=4, column=1, columnspan=COLSPAN, pady=1)

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
    global original_user_entry
    original_user_entry = text_box.get()
    convert = []
    length_of_entry = len(text_box.get())
    # Checks to make sure the user entered something in the entry box before pressing the ENTER button
    if length_of_entry == 0:
        messagebox.showwarning(title="Whoops!", message="Looks like you forgot to enter a word/phrase\n"
                                                        "in the entry field, please enter 5 - 30 characters\n"
                                                        "and then press ENTER :\\")
    else:
        # first convert the string into ' _ ' and newlines in place of spaces
        for x in range(length_of_entry):
            if answer[x] == ' ':
                convert.append('\n')
            else:
                convert.append(' _ ')
        # then for the sake of removing the {}, convert it all back into a string
        global return_to_string
        return_to_string = ""
        for x in convert:
            return_to_string += x

        # prints out the "blank" spaces based on the length of user input
        global blank_labels  # Made this global so it can be destroyed via the clear_box function
        blank_labels = Label(root, text=return_to_string, bg="gray", fg="white")
        blank_labels.grid(row=22, column=9, rowspan=20, columnspan=10, sticky='NESW')
        enter_button['state'] = DISABLED  # disables the ENTER button to stop multiple labels
        text_box.delete(0, 'end')  # clears the entry box so the other player can't see it
        text_box.config(state='disabled')  # disables the entry box (grays out the text)


enter_button = Button(root, text="ENTER", command=get_input)
enter_button.grid(row=6, column=5, sticky=E, columnspan=2, pady=4)


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
clear_button.grid(row=6, column=7, sticky=W, columnspan=2, pady=4)

# This label is created and destroyed to check in alphabet_pressed() if start_game() has commenced
lets_begin = Label(root)
lets_begin.destroy()

# The start button
def start_game():
    """
    This function checks for user input in the entry box and give the user info on the rules of
    the game as well as notifies them that the game has commenced
    :return:
    """
    # Checks to see if the user entered a word/phrase and pressed ENTER first
    if blank_labels.winfo_exists() != 1 or blank_labels.cget("text") == "":
        messagebox.showwarning(title="Whoops!", message="Looks like you forgot to enter a word or phrase\n"
                                                        "first, or you entered one and forgot to press the\n"
                                                        "ENTER button first. :\\")
    else:
        # Displays the rules
        global lets_begin
        lets_begin = Label(root, justify=LEFT, text="#5\n"
                                                    "Click on the letters below to try\n"
                                                    "and guess the hidden word or phrase.\n"
                                                    "********** BE WARNED! **********\n"
                                                    "You only have SIX chances\n"
                                                    "before it's GAME OVER :(",
                           bg="gray", fg="white")
        lets_begin.grid(row=7, column=1, columnspan=COLSPAN, rowspan=13, pady=1, sticky=W)


game_over = 0  # Used in alphabet_press() to determine the game_over count
correct_guess_count = 0  # Used in alphabet_press() to determine the correct_guess_count


def alphabet_press(user_letter_pick):

    # Checks to see if the START NEW GAME button was successfully pressed w/o error
    if lets_begin.winfo_exists() != 1:
        messagebox.showwarning(title="Pump the brakes!", message="It appears you've gotten a bit ahead of\n"
                                                                 "yourself, though your eagerness is appreciated\n"
                                                                 "please follow procedure :\\")
    else:
        b_label = []
        for n in return_to_string:
            b_label += n
        global original_user_entry
        original_entry_length = len(original_user_entry)
        global game_over
        global correct_guess_count
        good_guess = FALSE
        for letters in original_user_entry:
            j = 0
            if letters[j] == alphabet[user_letter_pick]:
                b_label[j+1] = alphabet[user_letter_pick]
                print("User_answer:", original_user_entry)
                print("alphabet[user_letter_pick]", alphabet[user_letter_pick])
                print("Letters:", letters[j])
                good_guess = TRUE  # The player guessed the right letter
                correct_guess_count += 1
                print("correct_guess_count:", correct_guess_count)
                print("original_entry_length:", original_entry_length)
                if correct_guess_count == original_entry_length:  # The User wins the game!!
                    messagebox.showinfo(title="**** WINNER! ****", message="CONGRATS!!\n"
                                                                           "You figured out the word/phrase\n"
                                                                           "before it was too late, clearly your\n"
                                                                           "guessing skills are unfathomable")
                    blank_labels.destroy()  # Removes the blanks
                    lets_begin.destroy()  # Removes the let's begin label & rules
                    enter_button['state'] = NORMAL  # re-enables the ENTER button
                    text_box.config(state='normal')  # re-enables the entry box
            j += 1
        if good_guess == FALSE:  # The player guessed the wrong letter
            game_over += 1
            print("game_over:", game_over)
            if game_over >= 1:
                lll_img = Image.open(
                    r"C:\Users\Owner\PycharmProjects\Module14\lose_image/left_leg_lose.png")  # open the image
                resized_lll_img = lll_img.resize((300, 225),
                                                 Image.ANTIALIAS)  # resize the image + makes sure borders are ok
                lose_leg_left_img = ImageTk.PhotoImage(resized_lll_img)  # assign the newly resized image
                losing_lbl_one = Label(root, image=lose_leg_left_img, bg="gray", fg="white")  # Create the label
                losing_lbl_one.photo = lose_leg_left_img  # Assign the img to the label (pic is blank w/o this)
                losing_lbl_one.grid(row=0, column=12, columnspan=5, rowspan=5)  # place it on the grid
            if game_over >= 2:
                rll_img = Image.open(
                    r"C:\Users\Owner\PycharmProjects\Module14\lose_image/right_leg_lose.png")  # open the image
                resized_rll_img = rll_img.resize((300, 225),
                                                 Image.ANTIALIAS)  # resize the image + makes sure borders are ok
                lose_leg_right_img = ImageTk.PhotoImage(resized_rll_img)  # assign the newly resized image
                losing_lbl_two = Label(root, image=lose_leg_right_img, bg="gray", fg="white")  # Create the label
                losing_lbl_two.photo = lose_leg_right_img  # Assign the img to the label (pic is blank w/o this)
                losing_lbl_two.grid(row=0, column=16, columnspan=5, rowspan=5)  # place it on the grid
            if game_over >= 3:
                cl_img = Image.open(
                    r"C:\Users\Owner\PycharmProjects\Module14\lose_image/chest_lose.png")  # open the image
                resized_cl_img = cl_img.resize((300, 225),
                                               Image.ANTIALIAS)  # resize the image + makes sure borders are ok
                lose_chest_img = ImageTk.PhotoImage(resized_cl_img)  # assign the newly resized image
                losing_lbl_three = Label(root, image=lose_chest_img, bg="gray", fg="white")  # Create the label
                losing_lbl_three.photo = lose_chest_img  # Assign the img to the label (pic is blank w/o this)
                losing_lbl_three.grid(row=4, column=14, columnspan=5, rowspan=5)  # place it on the grid
            if game_over >= 4:
                lal_img = Image.open(
                    r"C:\Users\Owner\PycharmProjects\Module14\lose_image/left_arm_lose.png")  # open the image
                resized_lal_img = lal_img.resize((300, 225),
                                                 Image.ANTIALIAS)  # resize the image + makes sure borders are ok
                left_arm_img = ImageTk.PhotoImage(resized_lal_img)  # assign the newly resized image
                losing_lbl_four = Label(root, image=left_arm_img, bg="gray", fg="white")  # Create the label
                losing_lbl_four.photo = left_arm_img  # Assign the img to the label (pic is blank w/o this)
                losing_lbl_four.grid(row=5, column=12, columnspan=5, rowspan=5)  # place it on the grid
            if game_over >= 5:
                ral_img = Image.open(
                    r"C:\Users\Owner\PycharmProjects\Module14\lose_image/right_arm_lose.png")  # open the image
                resized_ral_img = ral_img.resize((300, 225),
                                                 Image.ANTIALIAS)  # resize the image + makes sure borders are ok
                right_arm_img = ImageTk.PhotoImage(resized_ral_img)  # assign the newly resized image
                losing_lbl_five = Label(root, image=right_arm_img, bg="gray", fg="white")  # Create the label
                losing_lbl_five.photo = right_arm_img  # Assign the img to the label (pic is blank w/o this)
                losing_lbl_five.grid(row=5, column=15, columnspan=5, rowspan=5)  # place it on the grid
        if game_over >= 6:  # GAME OVER
            hl_img = Image.open(
                r"C:\Users\Owner\PycharmProjects\Module14\lose_image/head_lose.png")  # open the image
            resized_hl_img = hl_img.resize((300, 225),
                                             Image.ANTIALIAS)  # resize the image + makes sure borders are ok
            head_img = ImageTk.PhotoImage(resized_hl_img)  # assign the newly resized image
            losing_lbl_six = Label(root, image=head_img, bg="gray", fg="white")  # Create the label
            losing_lbl_six.photo = head_img  # Assign the img to the label (pic is blank w/o this)
            losing_lbl_six.grid(row=7, column=13, columnspan=5, rowspan=5)  # place it on the grid
            messagebox.showerror(title="GAME OVER", message="GAME OVER\n"
                                                            "Aw shucks, maybe next time :(")
            blank_labels.destroy()  # Removes the blanks
            lets_begin.destroy()  # Removes the let's begin label & rules
            enter_button['state'] = NORMAL  # re-enables the ENTER button
            text_box.config(state='normal')  # re-enables the entry box


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
    lbl_start_game.grid(row=1, column=1, columnspan=COLSPAN, pady=6)


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
    lbl_start_game.grid(row=1, column=1, columnspan=COLSPAN, pady=6)


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
    lbl_start_game.grid(row=1, column=1, columnspan=COLSPAN, pady=8)  # Uses more padding b/c the image is smaller
    start_game()  # The game officially begins here! :)


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
    lbl_start_game.grid(row=1, column=1, columnspan=COLSPAN, pady=6)


img_start_button = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\start_new_game_raised_normal.png")
lbl_start_game = Label(root, image=img_start_button, bg="gray", fg="white")
lbl_start_game.grid(row=1, column=1, sticky=S, columnspan=COLSPAN, pady=6)

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
    lbl_options.grid(row=2, column=1, columnspan=COLSPAN, pady=6)


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
    lbl_options.grid(row=2, column=1, columnspan=COLSPAN, pady=6)


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
    lbl_options.grid(row=2, column=1, columnspan=COLSPAN, pady=8)  # Uses more padding b/c the image is smaller

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
    lbl_options.grid(row=2, column=1, columnspan=COLSPAN, pady=6)


img_option_button = PhotoImage(file=r"C:\Users\Owner\PycharmProjects\Module14\buttons\options_raised_normal.png")
lbl_options = Label(root, image=img_option_button, bg="gray", fg="white")
lbl_options.grid(row=2, column=1, sticky=N, columnspan=COLSPAN, pady=6)

lbl_options.bind("<Enter>", change_options_button)  # Mouse Rollover ("entering" the image area), uses the change method
lbl_options.bind("<Leave>", change_back_options_button)  # Mouse Rollover ("leaving" the image area), uses the change_back method
lbl_options.bind("<Button-1>", on_click_options_button)  # On-click the button appears to depress
lbl_options.bind("<ButtonRelease>", release_click_options_button)  # Once released the On-click is disregarded

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
ALPHA_ROW = 22
ALPHA_COL = 1

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
abc_s(0, 22, 1)
abc_s(1, 22, 2)
abc_s(2, 22, 3)
abc_s(3, 22, 4)
abc_s(4, 22, 5)
abc_s(5, 22, 6)
abc_s(6, 22, 7)
abc_s(7, 22, 8)
abc_s(8, 23, 1)
abc_s(9, 23, 2)
abc_s(10, 23, 3)
abc_s(11, 23, 4)
abc_s(12, 23, 5)
abc_s(13, 23, 6)
abc_s(14, 23, 7)
abc_s(15, 23, 8)
abc_s(16, 24, 1)
abc_s(17, 24, 2)
abc_s(18, 24, 3)
abc_s(19, 24, 4)
abc_s(20, 24, 5)
abc_s(21, 24, 6)
abc_s(22, 24, 7)
abc_s(23, 24, 8)
abc_s(24, 25, 1)
abc_s(25, 25, 2)

mainloop()

root.mainloop()
