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

lbl_start = Label(root, justify=LEFT, text="Please enter a word or phrase below...", bg="gray", fg="white")
lbl_start_cont = Label(root, justify=LEFT, text="Then press the ENTER button to begin :)", bg="gray", fg="white")

lbl_start.grid(row=3, column=1, columnspan=COLSPAN)
lbl_start_cont.grid(row=5, column=1, columnspan=COLSPAN)

# The entry box for user input of what the user would like to use for the upcoming game
text_box = Entry(root, relief=FLAT, width=38)
text_box.grid(row=4, column=1, columnspan=10)


def get_input():
    """
    This function gathers user input and converts the chars to blanks (underscores)
    and blank spaces to newlines.  It also grays out the ENTER button and entry field
    :return:
    """
    answer = text_box.get()  # convert the string into chars
    convert = []
    length_of_entry = len(text_box.get())

    # first convert the string into ' _ ' and newlines in place of spaces
    for x in range(length_of_entry):
        if answer[x] == ' ':
            convert.append('\n')
        else:
            convert.append(' _ ')
    # then for the sake of removing the {}, convert it all back into a string
    return_to_string = ""
    for x in convert:
        return_to_string += x

    # prints out the "blank" spaces based on the length of user input
    global blank_labels  # Made this global so it can be destroyed via the clear_box function
    blank_labels = Label(root, text=return_to_string, bg="gray", fg="white")
    blank_labels.grid(row=7, column=1, columnspan=10)
    enter_button['state'] = DISABLED  # disables the ENTER button to stop multiple labels
    text_box.config(state='disabled')  # disables the entry box (grays out the text)

enter_button = Button(root, text="ENTER", command=get_input)
enter_button.grid(row=6, column=5, sticky=E, columnspan=2)


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
clear_button.grid(row=6, column=7, sticky=W, columnspan=2)

# The start button
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

# These for loops place the A-Z buttons onto a grid
index = 0
for x in range(alpha_length):
    if index > 25:
        break
    for y in range(alpha_length):
        if index > 25:
            break
        buttons_abc[index].grid(row=10+x, column=1+y, sticky=S, pady=2)
        index = index + 1
        if y >= 7:
            break

index = 0

def change_alphabet_buttons(event):
    """
    This function performs the first portion of a mouse rollover, changing the image
    :param event:
    :return:
    """
    another_image = image_abc_active[index]
    a_label = buttons_abc[index]
    a_label.config(image=another_image)
    a_label.image = another_image
    a_label.grid(row=10, column=1, pady=2)

def change_back_alphabet_button(event):
    """
    This function performs the 2nd portion of a mouse rollover, changing the image back to its
    original state
    :param event:
    :return:
    """
    img_alphabet_button_mouse_return = image_abc[index]
    a_label = buttons_abc[index]
    a_label.config(image=img_alphabet_button_mouse_return)
    a_label.image = img_alphabet_button_mouse_return
    a_label.grid(row=10, column=1, pady=2)

def on_click_alphabet_button(event):
    """
    This function performs the on-click portion, changing the image to look "pressed"
    :param event:
    :return:
    """
    img_alphabet_button_on_click = image_abc_pressed[index]
    a_label = buttons_abc[index]
    a_label.config(image=img_alphabet_button_on_click)
    a_label.image = img_alphabet_button_on_click
    a_label.grid(row=10, column=1, pady=4)  # Uses more padding b/c the image is smaller

def release_click_alphabet_button(event):
    """
    This function performs reverses the on-click portion
    :param event:
    :return:
    """
    another_image = image_abc_active[index]
    a_label = buttons_abc[index]
    a_label.config(image=another_image)
    a_label.image = another_image
    a_label.grid(row=10, column=1, pady=2)


buttons_abc[index].bind("<Enter>", change_alphabet_buttons) # Mouse Rollover ("entering" the image area), uses the change method
buttons_abc[index].bind("<Leave>", change_back_alphabet_button)  # Mouse Rollover ("leaving" the image area), uses the change_back method
buttons_abc[index].bind("<Button-1>", on_click_alphabet_button)  # On-click the button appears to depress
buttons_abc[index].bind("<ButtonRelease>", release_click_alphabet_button)  # Once released the On-click is disregarded


mainloop()

root.mainloop()
