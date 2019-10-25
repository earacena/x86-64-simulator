# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: gui.py
# File Description: This file contains the functions related to the Disk component

class Disk:
    def __init__(self, debug):

        self.debug_info = debug;

        if self.debug_info == True:
            print("[Disk] initializing...")

        ### Initialization code ###
        self.source_code = []
        self.page_table = []
        ###########################
  
        if self.debug_info == True:
            print("[Disk] finished initializing...")
    

    def load_file(self, filename):
        if self.debug_info == True:
            print("[Disk] loading file '" + filename + "'..." )

        with open(filename) as file:
            for line in file:
                self.source_code.append(line)
        
        if self.debug_info == True:
            print("[Disk] Contents of file '" + filename + "' loaded: ")

            for line in self.source_code:
                print("[...] " + line.strip('\n'))

    # This function sorts the code sequentially into pages, making the assumption that every instruction
    # is 15 bytes (max x86_64 instruction size) for simplicity
    def page_application(self, max_instr_size, max_page_size):
        page = []
        counter = 0
        for line in self.source_code:
            if counter >= max_page_size:
                self.page_table.append(list(page))
                page.clear()
                counter = 0

            page.append(line.strip('\n'))
            counter = counter + max_instr_size
      
        # make sure to add incomplete pages
        self.page_table.append(list(page))

    def load_page(self, page_number):
        if page_number+1 > len(self.page_table):
            return False

        else:
            return self.page_table[page_number]
 
    # Print table of all pages
    def print_page_table(self):
        page_number = 0
        print("\n[Disk] Printing all pages stored in disk:")
        for page in self.page_table:
            print("[...] Page " + str(page_number), page)
            page_number = page_number + 1 

## Unit test
def main():
    debug = True
    disk = Disk(debug)

    # Largest possible instruction size: 15 bytes
    max_instr_size = 15
    # page size is 100 bytes
    max_page_size = 100
    filename = "test.asm"

    # Main interface functions
    disk.load_file(filename)
    disk.page_application(max_instr_size, max_page_size)
    disk.print_page_table()

    # return page 2, should have some data, return it
    print("\n[Test] Loading page " + str(2) + ": ")
    print(disk.load_page(2))
    print("")

    # return page 6, does not exist, return False
    print("\n[Test] Loading page " + str(6) + ": ")
    print(disk.load_page(6))
    print("")
