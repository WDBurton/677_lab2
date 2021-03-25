import os
import constants

# Okay, this is the main file for the funcationality of the bookstore.

# I miss C++.  T___T  Low level stuff rocks, don't you dare claim otherwise.


######################################################################################
#   Global declarations

# This section is used for global declarations -- things that will be used later, and should
# easily be changed if needed.


######################################################################################
#   Test
# This is basic testing code, here first because Python doesn't have forward declaration.  Which
# bugs me.  D<

# Basic functions for print statements, for development purposes

def printMain(toPrint):
    if(constants.PRINT_MAIN): print(toPrint)

def printCat(toPrint):
    if(constants.PRINT_CATALOGUE): print(toPrint)




######################################################################################
#   Catalogue
def cat_makeDocs(runNum = -1, id_1 = 2, id_2 = 2, id_3 = 3, id_4 = 2):
    pass
    # This function creates the catalogue logs; First, it checks to see if the correct folder
    # exists.  If not, it creates it.  Then, it creates a new CATALOGUE.txt, using 'w' mode
    # for python file io; it fills the file and closes it.  Finally, if the run number is defined,
    # it creates the correct document, ORDER_LOGXX.txt, in the same manner and fills the first line.
    # Otherwise, it finds the first clear run number and uses that.  Either way, it returns the run
    # number used.

    # Create the folder if it doesn't exists

    # Create CATALOGUE.txt, and fill it

    # Close CATALOGUE.txt file

    # Variable for the true run number

    # Check to see if the run number is defined!

        # If defined, store in true run number

        # Otherwise, search for first free doc name, and use that for the run number

    # Now that run number is defined, make the file and put in the first line

    # Close ORDER_LOGXX.txt and return the run number.





######################################################################################
#   Order
######################################################################################
#   Front-end
######################################################################################
#   Client


######################################################################################
#   Main
# This is where the actual 'run the goddamn code' section is, because Python doesn't seem to have
# any convenient forward declaration.  D<  At least not for functional programming, which I prefer.


# Basic print statements for debugging purposes.
printMain("MAIN: Start")
print(constants.CAT_FOLDER)

