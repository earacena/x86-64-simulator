# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: gui.py
# File Description: This file contains the functions related to the Disk component

from common import phex
from bus import Bus

class Page:
    def __init__(self, page_number, start_address, page_size):
        self.page_number   = page_number
        self.start_address = phex(start_address, 10)
        self.page_size     = page_size
        self.end_address   = phex(int(self.start_address, 0) + page_size, 10)
        self.instructions  = []
        self.num_of_instr  = 0

    def add_instruction(self, instruction):
        address = int(self.start_address, 0) + (self.num_of_instr * 4)
        self.instructions.append([phex(address, 10), instruction])
        self.num_of_instr = self.num_of_instr + 1
        

class Disk:
    def __init__(self, debug):

        self.debug_info = debug;

        if self.debug_info == True:
            print("[Disk] initializing...")

        ### Initialization code ###
        self.source_code = []
        self.storage = []
        self.initial_page_number = 0
        self.page_size = 32
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
    # is 4 bytes (max x86_64 instruction size) for simplicity
    def page_application(self, max_instr_size):
        page_counter = 0
        counter = 0
        address = 0
        page = Page(page_counter, address, self.page_size)
        for instruction in self.source_code:
            if counter >= self.page_size:
                self.storage.append(page)
                page_counter = page_counter + 1
                page = Page(page_counter, address, self.page_size)
                counter = 0

            page.add_instruction(instruction.strip('\n'))
            counter = counter + max_instr_size
            address = address + max_instr_size
             
        # make sure to add incomplete pages
        self.storage.append(page)

        # set initial page number
        self.find_initial_page()


    def load_page(self, page_number):
        if page_number+1 > len(self.storage):
            return False
        else:
            return self.storage[page_number]

    # Find the position of "main" in page table
    def find_initial_page(self):
        for index, page in enumerate(self.storage):
            for instruction in page.instructions:
                if 'main:' in instruction[1]:
                    self.initial_page_number = index
                    return 
 
    # Print table of all pages
    def print_page_table(self):
        print("\n[Disk] Printing all pages stored in disk (initial page: "+
                str(self.initial_page_number)  +"):")
        for page in self.storage:
            print("[...] Page " + 
                  str(page.page_number) +
                  "\n[...] start address: " + str(page.start_address) +
                  "\n[...] end address:   " + str(page.end_address) +
                  "\n[...] Instructions:")
            for instruction in page.instructions:
                  print("[...]", instruction)
            print("")

    def print_page(self, page):
        if page != False:
            print("[...] Page " + 
                  str(page.page_number) +
                  "\n[...] start address: " + str(page.start_address) +
                  "\n[...] end address:   " + str(page.end_address) +
                  "\n[...] Instructions:")
            for instruction in page.instructions:
                  print("[...]", instruction)
            print("")
        else:
            print("[Disk] Page does not exist.")

## Unit test
def main():
    debug = True
    bus = None          # not needed for testing
    disk = Disk(debug)


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
    page = disk.load_page(2)
    disk.print_page(page)

    # return page 6, does not exist, return False
    print("\n[Test] Loading page " + str(100) + " (must return False): ")
    page = disk.load_page(100)
    disk.print_page(page)
