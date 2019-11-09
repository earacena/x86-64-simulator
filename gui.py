"""
    Project: x86_64 Hardware Simulator
    Name: Emanuel Aracena
    Filename: gui.py
    File Description: This file contains the functions related to the GUI component
"""
# Force python to use python3 print function
from __future__ import print_function

# Component Modules
from cpu import CPU
from cache import Cache
from tlb import TLB
from memory import Memory
from disk import Disk
from disk import print_page
from bus import Bus

# Common file, for reusable function implementations
#from common import phex

class GUI:
    """ This class handles all UI activity and manages integration with other components. """
    def __init__(self, bus, cpu, cache, tlb, memory, disk, debug):
        """ Assign the references to the components in the simulator. """
        self.debug_info = debug
        self.bus = bus
        self.cpu = cpu
        self.cache = cache
        self.tlb = tlb
        self.memory = memory
        self.disk = disk
        self.phase = 1

    def menu_loop(self):
        """ Handles user input and transition between different stages of the UI. """
        choice = ""
        quit_choice = "z"
        while choice is not quit_choice:
            main_menu()
            if self.phase == 1:
                phase_1_menu()
                choice = input("\nChoice: ")
                choice_table = self.load_choice_table(self.phase)
                if choice in choice_table:
                    choice_table[choice]()
            elif self.phase == 2:
                phase_2_menu()
                choice = input("\nChoice: ")
                choice_table = self.load_choice_table(self.phase)
                if choice in choice_table:
                    choice_table[choice]()

            elif self.phase == 3:
                phase_3_menu()
                choice = input("\nChoice: ")
                choice_table = self.load_choice_table(self.phase)
                if choice in choice_table:
                    choice_table[choice]()

            elif self.phase == 4:
                phase_4_menu()
                choice = input("\nChoice: ")
                choice_table = self.load_choice_table(self.phase)
                if choice in choice_table:
                    choice_table[choice]()

            else:
                # Phase 5
                phase_5_menu()
                self.phase = 1

    def load_choice_table(self, phase):
        """ Load appropriate choice table for menu, avoids many if-statements. """
        if phase == 1:
            choice_table = {
                "a": self.load_source_code,
                "z": terminate
            }

        elif phase == 2:
            choice_table = {
                "a": self.reset_and_load_source_code,
                "b": self.view_instructions,
                "c": self.page_application,
                "z": terminate
            }

        elif phase == 3:
            choice_table = {
                "a": self.reset_and_load_source_code,
                "b": self.view_instructions,
                "d": self.load_into_memory,
                "z": terminate
            }

        elif phase == 4:
            choice_table = {
                "a": self.reset_and_load_source_code,
                "b": self.view_instructions,
                "d": self.simulate_one_instruction,
                "e": self.view_cache_table,
                "f": self.view_cache_stats,
                "g": self.view_registers,
                "h": self.view_memory_layout,
                "i": self.view_virtual_mem_layout,
                "j": self.view_page_table,
                "k": self.view_runtime_info,
                "z": terminate
            }

        return choice_table

    def load_source_code(self):
        """ Load data from file with given filename."""
        print("\nLoad source code selected!")
        filename = input("Filename?[x86_64 .asm only]: ")
        self.disk.load_file(filename)
        self.phase = 2

    def page_application(self):
        """ Page the application by calling the Disk component's method. """
        self.phase = 3
        max_instr_size = 4
        self.disk.page_application(max_instr_size)

    def reset_simulator(self):
        """ Reassign the references of the components to reset the simulation. """
        print("\nReset simulator, selected!")

        # instance new component objects
        debug = self.bus.debug_info

        self.bus = Bus(debug)
        self.cpu = CPU(debug)

        cache_size = self.cache.cache_size
        block_size = self.cache.block_size
        self.cache = Cache(cache_size, block_size, debug)

        table_size = self.tlb.table_size
        self.tlb = TLB(table_size, debug)

        memory_size = self.memory.memory_size
        virtual_memory_size = self.memory.virtual_memory_size
        self.memory = Memory(memory_size, virtual_memory_size, debug)

        page_size = self.disk.page_size
        self.disk = Disk(page_size, debug)

    def reset_and_load_source_code(self):
        """ Reset the simulator and give pronmpt to load data from new file. """
        self.phase = 2
        self.reset_simulator()
        self.load_source_code()

    def view_instructions(self):
        """ View the currently loaded program instructions. """
        print("\nView instructions selected!")

        print("\n[PRINT] Printing source code...")
        for instruction in self.disk.source_code:
            print("[...] ", instruction.strip('\n'))

        input("[~] Press any key to continue...")

    def load_into_memory(self):
        """ Load as many pages that fit in memory, starting with the starting page (main). """
        print("\nLoad into memory selected!")
        self.phase = 4
        self.memory.load_initial_pages_of_program(self.disk, "disk")
        self.memory.map_pages_to_virtual(self.disk, "disk")
        self.cpu.synchronize_with_memory(self.memory, "virtual memory")

    def simulate_one_instruction(self):
        """ Simulate the communication of executing one instruction. """
        print("\nSimulate one instruction selected!")

    def view_cache_table(self):
        """ View the contents of the cache. """
        print("\nView cache table selected!")
        self.cache.print_cache()
        input("[~] Enter any key to continue...")

    def view_cache_stats(self):
        """
            View the current statistics of the cache regarding hit, miss, replace
            ratios.
        """
        print("\nView cache statstics selected!")

        input("[~] Enter any key to continue...")

    def view_registers(self):
        """ View the current values of the CPU registers. """
        print("\nView registers selected!")
        self.cpu.print_register_table()
        input("[~] Enter any key to continue...")

    def view_memory_layout(self):
        """ View the current contents of the memory component. """
        print("\nView memory layout selected!")
        self.memory.print_memory_page_table()

        input("[~] Enter any key to continue...")

    def view_virtual_mem_layout(self):
        """ View the current mappings of the virtual memory. """
        print("\nView virtual memory layout selected!")
        self.memory.print_virtual_with_position(self.cpu.register_table["pc"])
        input("[~] Enter any key to continue...")

    def view_page_table(self):
        """ View the current contents of the Disk's page table. """
        print("\nView page table selected!")
        self.disk.print_page_table()
        input("[~] Enter any key to continue...")

    def view_runtime_info(self):
        """ View the runtime statistics of the simulated program. """
        print("\nView runtime info selected!")
        input("[~] Enter any key to continue...")

def main_menu():
    """ Prints the main menu splash screen. """
    print("\n _________________________________________________")
    print("||              x86_64 CPU Simulator             ||")
    print("||               Emanuel Aracena                 ||")
    print(" -------------------------------------------------")

def phase_1_menu():
    """ Menu for the first stage of the UI. """
    print("")
    print("a. Load source code")
    print("")
    print("z. Quit")

def phase_2_menu():
    """ The menu for the second stage of the UI. """
    print("")
    print("a. Reset and load new source code")
    print("> b. View instructions")
    print("")
    print("c. Page source code.")
    print("")
    print("z. Quit")

def phase_3_menu():
    """ The menu for third stage of the UI. """
    print("\na. Reset and load new source code")
    print("> b. View instructions")
    print("")
    print("d. Load into memory")
    print("")
    print("z. Quit")

def phase_4_menu():
    """ The menu for the fourth stage of the UI. """
    print("\na. Reset and load new source code")
    print("> b. View instructions")
    print("\nd. Simulate one instruction")
    print("> e. View Cache table")
    print("> f. View Cache statistics")
    print("> g. View registers")
    print("> h. View memory layout")
    print("> i. View virtual memory layout")
    print("> j. View page table")
    print("> k. View current run-time info")
    print("\nz. Quit")

def phase_5_menu():
    """ The menu for the fifth stage of the UI. Used as a placeholder."""
    print("\n[ATTENTION] PROGRAM HAS FINISHED EXECUTION, RETURNING TO MENU!")

def terminate():
    """ Exit the program. """
    print("")
    print("Quit selected!")
