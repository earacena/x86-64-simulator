# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: memory.py
# File Description: This file contains the functions related to the memory component

from bus import Bus
from disk import Disk
from disk import main

class Memory:

    def __init__(self, bus, memory_size, virtual_memory_size, debug):
        self.debug_info = debug;

        if self.debug_info == True:
            print("[Memory] initializing...")

        ### Initialization code ###
        self.virtual_memory         = [] 
        self.memory                 = []
        self.page_table_register    = None
        self.bus                    = bus
        self.memory_size            = [None] * memory_size
        self.number_of_pages_loaded = 0
        
        self.const_stack_address    = 8000
        self.const_heap_address     = 4000
        self.const_BSS_address      = 2000
        self.const_text_address     = 1000
        ###########################
  
        if self.debug_info == True:
            print("[Memory] finished initializing...")


    def initialize_virtual_memory(self):
        


    def load_initial_pages_of_program(self):
        self.page_table_register = bus.communicate("memory", "disk, initial page number", "")
        page_size = bus.communicate("memory", "disk, send page size", "")
        while memory_size >= page_size:
            page = bus.communicate("memory", "disk, send page", str(page_table_register))
            page_table.append(list(page))


# For unit testing
def main():
    debug = True

    memory_size = 100
    virtual_memory_size = 8000

    bus = Bus(debug) 
    memory = Memory(bus, memory_size, virtual_memory_size, debug)

    bus.link_memory(memory)

    memory.load_initial_pages_of_program()

    memory.print_memory_page_table()
    memory.print_virtual_memory_layout()

