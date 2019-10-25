# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: memory.py
# File Description: This file contains the functions related to the memory component

class Memory:

    def __init__(self, bus, memory_size, debug):
        self.debug_info = debug;

        if self.debug_info == True:
            print("[Memory] initializing...")

        ### Initialization code ###
        self.page_table             = []
        self.page_table_register    = None
        self.bus                    = bus
        self.memory_size            =
        self.number_of_pages_loaded = 0
        ###########################
  
        if self.debug_info == True:
            print("[Memory] finished initializing...")


    def load_initial_pages_of_program(self):
        self.page_table_register = bus.communicate("memory", "disk, initial page number", "")
        page_size = bus.communicate("memory", "disk, send page size", "")
        while memory_size >= page_size:
            page = bus.communicate("memory", "disk, send page", str(page_table_register))
            page_table.append(list(page))

