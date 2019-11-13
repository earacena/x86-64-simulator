"""
    Project: x86_64 Hardware Simulator
    Name: Emanuel Aracena
    Filename: memory.py
    File Description: This file contains the functions related to the memory component
"""

# Force python to use Python3 print function
from __future__ import print_function

# Modules
from random import randint

# Components
from bus import Bus
from common import phex

# For unit testing only, must not be used inside methods/class interface.
from disk import Disk

class Memory:
    """ This class handles the activity of the memory and virtual memory component. """
    def __init__(self, memory_size, virtual_memory_size, debug):
        self.debug_info = debug

        if self.debug_info is True:
            print("[Memory] initializing...")

        ### Initialization code ###
        self.virtual_memory = [None] * virtual_memory_size
        self.memory = [None] * memory_size
        self.page_table_register = None
        self.bus = Bus(debug)
        self.memory_size = memory_size
        self.number_of_pages_loaded = 0
        self.memory_used = 0

        ### Virtual Memory ###
        # Assuming size of memory is
        self.stack_address_used = 0x8000 # decrease as memory is used, stack
                                         # grows up
        self.const_stack_start = 0x8000
        self.heap_address_used = 0       # increase as memory is used
        self.const_heap_start = 0x4000
        self.bss_address_used = 0        # increase as memory is used
        self.const_bss_start = 0x2000
        self.text_address_used = 0       # increase as memory is used
        self.const_text_start = 0x1000
        ###########################

        if self.debug_info is True:
            print("[Memory] finished initializing...")

    def load_initial_pages_of_program(self, callee, callee_name):
        """ Start from 'main:' label and load all subsequent pages into memory. """
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
        """ Store given page in memory. """
        if self.debug_info is True:
            print("[Memory] Attempting to store disk page ", page.page_number, "...")

        if (self.memory_size - self.memory_used) < page.page_size:
            if self.debug_info is True:
                print("[Memory] Memory (Text) full, replacing pages...")
                print("[ERROR] Not implemented yet.")
            #replace_page(page)
        else:
            # store page, instruction by instruction
            counter = self.memory_used
            for instruction in page.instructions:
                self.memory[counter] = instruction
                self.memory[counter+1] = "."    # These are placeholders used to simulate
                self.memory[counter+2] = "."    # byte addressing, ...
                self.memory[counter+3] = "."    # ...
                counter = counter + 4
                self.memory_used = self.memory_used + 4

    def replace_page(self, page):
        """ Replace random page in memory with given page. """
        if self.debug_info is True:
            print("[Memory] Replacing memory page randomly with page", page.page_number, "...")

        # memory_size/ page_size = number of page positions
        possible_page_positions = self.memory_size / page.page_size - 1
        picked_position = randint(0, possible_page_positions)

        counter = 0 + (page.page_size * picked_position)

        for instruction in page.instructions:
            self.memory[counter] = instruction
            counter = counter + 4

        # update_virtual_memory(page.page_number)

    def print_memory_page_table(self):
        """ Print the contents of memory. """
        if self.debug_info is True:
            print("\n[Memory] Printing contents of memory...")
        unallocated = "...unallocated..."
        for index, instruction in enumerate(self.memory):
            if instruction is None:
                output = unallocated
            else:
                output = instruction

            if instruction == ".":
                continue
            else:
                print("[...] ", phex(index, 10), " | ", output)

    def map_pages_to_virtual(self, callee, callee_name):
        """
            Synchronize virtual memory with the contents of memory, map memory addresses
            to virtual addresses.
        """
        if self.debug_info is True:
            print("[V. Memory / Memory] Mapping memory pages to virtual memory...")
        counter = self.const_text_start

        all_pages = self.bus.communicate("virtual memory", callee, callee_name,
                                         "disk, all pages for mapping", "")

        for page in all_pages:
            for instruction in page.instructions:
                self.virtual_memory[counter] = instruction
                counter = counter + 4

    def update_virtual_memory(self, page_number, position):
        """ Update the virtual memory addresses, with currently loaded memory pages. """
        pass

    def print_virtual_with_position(self, address):
        """ Print the position of the simulator in virtual memory with given PC address. """
        if self.debug_info is True:
            print("\n[V. Memory] Prining v. memory with position '" + phex(address, 5) + "':")
        position = int(phex(address, 8), 0) - (4*3)

        for pos in range(position, position+(4*7), 4):
            if pos == position + (4*3):
                print("=====>\t", "[", phex(pos, 8), "] ~ ", self.virtual_memory[pos])
            else:
                print("\t", "[", phex(pos, 8), "] ~ ", self.virtual_memory[pos])

    def find_starting_address(self):
        """ Find the starting position of 'main:' label in virtual memory. """
        if self.debug_info is True:
            print("\n[V. Memory] Looking for starting address...")

        start_address = ""

        for index, instruction in enumerate(self.virtual_memory):
            if instruction is None:
                continue
            elif instruction[1] == "main:":
                start_address = phex(index, 8)
                break

        if self.debug_info is True:
            print("[V. Memory] Starting address found '" + start_address + "'...")

        return start_address

    def print_virtual_memory_layout(self):
        """ Print the contents of virtual memory.  """
        if self.debug_info is True:
            print("\n[V. Memory] Printing contents of virtual memory table...:")
        for index, data in enumerate(self.virtual_memory):
            if index == self.const_stack_start:
                print("[...] STACK(up): ")
            if index == self.const_heap_start:
                print("[...] HEAP(down):")
            if index == self.const_bss_start:
                print("[...] BSS:")
            if index == self.const_text_start:
                print("[...] TEXT (instructions):")

            if data != None:
                print("[...]", phex(index, 10), " ~ ", data)

def main():
    """ Unit test. """
    debug = True
    filename = "test.asm"

    memory_size = 100
    virtual_memory_size = 8000
    page_size = 32
    disk = Disk(page_size, debug)
    disk.load_file(filename)
    disk.page_size = 32
    disk.page_application(4) # instruction size 4 bytes
    memory = Memory(memory_size, virtual_memory_size, debug)

    memory.load_initial_pages_of_program(disk, "disk")
    memory.map_pages_to_virtual(disk, "disk")
    memory.print_memory_page_table()
    memory.print_virtual_memory_layout()
    memory.print_virtual_with_position(int("0x1000", 0))
    memory.find_starting_address()
