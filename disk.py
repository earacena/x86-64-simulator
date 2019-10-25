# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: gui.py
# File Description: This file contains the functions related to the Disk component

class Disk:
    def __init__(self, bus, debug):

        self.debug_info = debug;

        if self.debug_info == True:
            print("[Disk] initializing...")

        ### Initialization code ###
        self.source_code = []
        self.page_table = []
        self.initial_page_number = 0
        self.page_size = 0
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
    def page_application(self, max_instr_size):
        page = []
        counter = 0
        for line in self.source_code:
            if counter >= self.page_size:
                self.page_table.append(list(page))
                page.clear()
                counter = 0

            page.append(line.strip('\n'))
            counter = counter + max_instr_size
      
        # make sure to add incomplete pages
        self.page_table.append(list(page))

        # set initial page number
        self.find_initial_page()


    def load_page(self, page_number):
        if page_number+1 > len(self.page_table):
            return False

        else:
            return self.page_table[page_number]

    # Find the position of "main" in page table
    def find_initial_page(self):
        for index, page in enumerate(self.page_table):
            for instruction in page:
                if 'main:' in instruction:
                    self.initial_page_number = index
                    return 
 
    # Print table of all pages
    def print_page_table(self):
        page_number = 0
        print("\n[Disk] Printing all pages stored in disk (initial page: "+
                str(self.initial_page_number)  +"):")
        for page in self.page_table:
            print("[...] Page " + str(page_number), page)
            page_number = page_number + 1 

## Unit test
def main():
    debug = True
    bus = None          # not needed for testing
    disk = Disk(bus, debug)


    # Largest possible instruction size: 15 bytes
    max_instr_size = 4
    # page size is 100 bytes
    disk.page_size = 32
    filename = "test.asm"

    # Main interface functions
    disk.load_file(filename)
    disk.page_application(max_instr_size)
    disk.print_page_table()

    # return page 2, should have some data, return it
    print("\n[Test] Loading page " + str(2) + ": ")
    print(disk.load_page(2))
    print("")

    # return page 6, does not exist, return False
    print("\n[Test] Loading page " + str(6) + ": ")
    print(disk.load_page(6))
    print("")


