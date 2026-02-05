# Program Name: Assignment1.py
# Course: IT3883/Section 12893
# Student Name: Motunrayo Iruedo
# Assignment Number: Assignment 1
# Due Date: 02/04/2026
# Purpose:
#   This program uses a simple menu to manage a text buffer.
#   The user can add (append) text, clear the saved text, display it,
#   or exit the program.
# Resources Used:
#   - My notes and practice/youtube videos

# ----------------------------
# SETUP / STARTING VARIABLES
# ----------------------------
# This variable holds whatever text the user has saved so far.
saved_text = ""


# ----------------------------
# MENU DISPLAY FUNCTION
# ----------------------------
# This function prints the menu each time the loop repeats.
def show_menu():
    print("\n==============================")
    print("   TEXT BUFFER MENU")
    print("==============================")
    print("1) Add text to the buffer")
    print("2) Clear the buffer")
    print("3) Show the buffer")
    print("4) Exit")
    print("==============================")


# ----------------------------
# MAIN PROGRAM LOOP
# ----------------------------
# This loop keeps the program running until the user chooses option 4.
keep_running = True

while keep_running:
    show_menu()

    # Get the user's choice (as a string so we can compare to "1", "2", etc.)
    user_choice = input("Choose an option (1-4): ").strip()

    # ----------------------------
    # OPTION 1: APPEND TEXT
    # ----------------------------
    if user_choice == "1":
        extra_text = input("Type something to add: ")

        # Append new text onto the end of the saved buffer.
        # (We add a space first if the buffer already has content.)
        if saved_text != "":
            saved_text += " "  # adds spacing so words don't smash together

        saved_text += extra_text
        print("✅ Added to buffer.")

    # ----------------------------
    # OPTION 2: CLEAR BUFFER
    # ----------------------------
    elif user_choice == "2":
        saved_text = ""  # reset back to empty
        print("🧹 Buffer cleared.")

    # ----------------------------
    # OPTION 3: DISPLAY BUFFER
    # ----------------------------
    elif user_choice == "3":
        print("\n--- CURRENT BUFFER ---")
        if saved_text == "":
            print("(Nothing saved yet.)")
        else:
            print(saved_text)
        print("----------------------")

    # ----------------------------
    # OPTION 4: EXIT PROGRAM
    # ----------------------------
    elif user_choice == "4":
        print("Exiting now... bye! 👋")
        keep_running = False

    # ----------------------------
    # INVALID OPTION HANDLING
    # ----------------------------
    else:
        print("⚠️ Not a valid option. Please type 1, 2, 3, or 4.")
