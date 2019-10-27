# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: memory.py
# File Description: This file contains the functions related to the memory component

from bus import Bus
from common import phex

# For unit testing only, must not be used inside methods/class interface.
from disk import Disk
from disk import main

class Memory:

    def __init__(self, memory_size, virtual_memory_size, debug):
        self.debug_info = debug;

        if self.debug_info == True:
            print("[Memory] initializing...")

        ### Initialization code ###
        self.virtual_memory         = [None] * virtual_memory_size 
        self.memory                 = [None] * memory_size
        self.page_table_register    = None
        self.bus                    = Bus(debug)
        self.memory_size            = memory_size
        self.number_of_pages_loaded = 0
        self.memory_used            = 0
        ### Virtual Memory ###        
      
        # Assuming size of memory is   
        self.stack_address_used     = 8000 # decrease as memory is used, stack
                                           # grows up
        self.CONST_stack_start      = 8000

        self.heap_address_used      = 0 # increase as memory is used
        self.CONST_heap_start       = 4000

        self.BSS_address_used       = 0 # increase as memory is used
        self.CONST_BSS_start        = 2000

        self.text_address_used      = 0 # increase as memory is used
        self.CONST_text_start       = 1000
        ###########################
  
        if self.debug_info == True:
            print("[Memory] finished initializing...")

    def load_initial_pages_of_program(self, callee, callee_name):
        self.page_table_register = self.bus.communicate("memory", callee, callee_name,
                                                        "disk, initial page number", "")
        page_size = self.bus.communicate("memory", callee, callee_name, 
                                         "disk, send page size", "")
        while (self.memory_size - self.memory_used) >= page_size:
            page = self.bus.communicate("memory", callee, callee_name, "disk, send page",
                                        str(self.page_table_register))

            self.store_page(page)
            self.page_table_register = self.page_table_register + 1

    # Place page in open spot in memory
    def store_page(self, page):
        if self.debug_info == True:
            print("[Memory] Attempting to store disk page ", page.page_number, "...")

        if (self.memory_size - self.memory_used) < page.page_size:
            if self.debug_info == True:
                print("[Memory] Memory (Text) full, replacing pages...")
            replace_page(page)
        else:
            # store page, instruction by instruction
            counter = self.memory_used
            for instruction in page.instructions:
                self.memory[counter] = instruction
                self.memory[counter+1] = "."    # These are placeholders used to simulate      
                self.memory[counter+2] = "."    # byte addressing, ...
                self.memory[counter+3] = "."    # ...
                counter = counter + 4
                self.text_address_used = self.text_address_used + 4
                self.memory_used = self.memory_used + 4 

    def replace_page(self, page):
        pass

    # print what working memory looks like
    def print_memory_page_table(self):
        unallocated = "...unallocated..."
        for index, instruction in enumerate(self.memory):
            if instruction == None:
                output = unallocated
            else:
                output = instruction
            print(phex(index, 10), " | ", output)

    def print_virtual_memory_layout(self):
#        for index, data in self.virtual_memory:
#            if index == self.stack_address_available:
#                print("[...] STACK(up): ")
#            if index == self.heap_address_available:
#                print("[...] HEAP(down):")
#            if index == self.BSS_address_available:
#                print("[...] BSS:")
#            if index == self.text_address_available:
#                print("[...] TEXT (instructions):")
#            print("[...]\t",data)
        pass

# For unit testing
def main():
    debug = True
    filename = "test.asm"

    memory_size = 100
    virtual_memory_size = 8000
    disk = Disk(debug)
    disk.load_file(filename)
    disk.page_size = 32
    disk.page_application(4) # instruction size 4 bytes
    memory = Memory(memory_size, virtual_memory_size, debug)

    memory.load_initial_pages_of_program(disk, "disk")

    memory.print_memory_page_table()
    memory.print_virtual_memory_layout()

