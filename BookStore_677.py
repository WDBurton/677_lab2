import os
import shutil
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
#   Catalogue server

# Makes the catalogue documents and returns the run number for further logging.
def cat_makeDocs(runNum = -1, id_1 = 2, id_2 = 2, id_3 = 3, id_4 = 2):
    # This function creates the catalogue logs; First, it checks to see if the correct folder
    # exists.  If not, it creates it.  Then, it creates a new CATALOGUE.txt, using 'w' mode
    # for python file io; it fills the file and closes it.  Finally, if the run number is defined,
    # it creates the correct document, ORDER_LOGXX.txt, in the same manner and fills the first line.
    # Otherwise, it finds the first clear run number and uses that.  Either way, it returns the run
    # number used.

    printCat("CAT_makeDocs: Start")

    # Create the folder if it doesn't exists
    if not os.path.exists(constants.CAT_FOLDER):
        printCat("CAT_makeDocs: Make directory")
        os.makedirs(constants.CAT_FOLDER)

    # Create CATALOGUE.txt, and fill it
    printCat("CAT_makeDocs: Make catalogue")
    log = open(constants.CAT_FILE_CATALOGUE, "w")

    log.write("1," + str(id_1) + ": " + constants.BOOK_1 + "\n")
    log.write("2," + str(id_2) + ": " + constants.BOOK_2 + "\n")
    log.write("3," + str(id_3) + ": " + constants.BOOK_3 + "\n")
    log.write("4," + str(id_4) + ": " + constants.BOOK_4 + "\n")

    # Close CATALOGUE.txt file
    log.close()
    printCat("CAT_makeDocs: Catalogue made")

    # Check to see if the run number is defined!
    if runNum < 0:
        printCat("CAT_makeDocs: Run number not defined")
        # If not, search for first free doc name, and use that for the run number
        curRun = 0
        while True:
            # Until we find an empty file name, simply increment the number we're looking for
            if not os.path.isfile(constants.CAT_FILE_ORDER + str(curRun).zfill(2) + ".txt"):
                break
            curRun += 1
        # If we're here, we've found a good file name, but we need to store the number we've found.
        printCat("CAT_makeDocs: Run number found")
        runNum = curRun

    # Now that run number is defined, make the file and put in the first line
    printCat("CAT_makeDocs: Make order log")
    log = open(constants.CAT_FILE_ORDER + str(runNum).zfill(2) + ".txt", "w")
    log.write("1:" + str(id_1) + " 2:" + str(id_2) + " 3:" + str(id_3) + " 4:" + str(id_4))

    # Close ORDER_LOGXX.txt and return the run number.
    log.close()
    printCat("CAT_makeDocs: END")
    return runNum

# Deletes all catalogue documents and directory
def cat_delDocs():
    printCat("CAT_delDocs: Deleting directory and files within")
    # Errors are ignored as this is basically 'get a clean slate for future runs' function -- it
    # doesn't matter if the directory existed beforehand, so long as it doesn't exist afterwards.
    shutil.rmtree(constants.CAT_FOLDER, ignore_errors = True)



######################################################################################
#   Order server
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
printMain("MAIN: Start makeing catalogue files")
cat_makeDocs()
cat_delDocs()

