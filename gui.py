# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: gui.py
# File Description: This file contains the functions related to the GUI component

# Used to reset the simulator
from cpu import CPU
from cache import Cache
from tlb import TLB
from memory import Memory
from disk import Disk
from bus import Bus
from common import phex
# Class GUI
class GUI:

    def __init__(self, bus, cpu, cache, tlb, memory, disk, debug):
        self.debug_info = True
        self.bus = bus
        self.cpu = cpu
        self.cache = cache
        self.tlb = tlb
        self.memory = memory
        self.disk = disk

    def main_menu(self):
        print("")
        print("╔═══════════════════════════════════════════════╗")
        print("║              x86_64 CPU Simulator             ║")
        print("║                Emanuel Aracena                ║")
        print("╚═══════════════════════════════════════════════╝")

    # menu_loop
    def menu_loop(self):
        choice = ""
        phase = 1
        while choice is not "z":
            self.main_menu()
            if phase == 1:
                self.phase_1_menu()
                choice = input("\nChoice: ")
                if choice == "a":
                    phase = 2
                    self.load_source_code()
                elif choice == "z":
                    # Quit
                    self.quit() 
            elif phase == 2:
                self.phase_2_menu()
                choice = input("\nChoice: ")
                if choice == "a":
                    phase = 2
                    self.reset_simulator()
                    self.load_source_code()
                elif choice == "b":
                    self.view_instructions()
                elif choice == "c":
                    phase = 3
                    self.page_application()
                elif choice == "z":
                    # Quit
                    self.quit() 
            elif phase == 3:
                self.phase_3_menu()
                choice = input("\nChoice: ")
                if choice == "a":
                    phase = 2
                    self.reset_simulator()
                    self.load_source_code()
                elif choice == "b":
                    self.view_instructions()
                elif choice == "d":
                    self.load_into_memory()
                    phase = 4
                elif choice == "z":
                    # Quit
                    self.quit()
            elif phase == 4:
                self.phase_4_menu()
                choice = input("\nChoice: ")
                if choice == "a":
                    phase = 2
                    self.reset_simulator()
                    self.load_source_code()
                elif choice == "b":
                    self.view_instructions()
                elif choice == "d":
                    self.simulate_one_instruction()
                elif choice == "e":
                    self.view_cache_table()
                elif choice == "f":
                    self.view_cache_stats()
                elif choice == "g":
                    self.view_registers()
                elif choice == "h":
                    self.view_memory_layout()
                elif choice == "i":
                    self.view_virtual_mem_layout()
                elif choice == "j":
                    self.view_page_table()
                elif choice == "k":
                    self.view_runtime_info()
                elif choice == "z":
                    # Quit
                    self.quit() 
            else:
                # Phase 5
                phase = 1
    
    
    # phase_1_menu
    def phase_1_menu(self):
        print("")
        print("a. Load source code")
        print("")
        print("z. Quit")
    
    ## phase_1_choice_A
    def load_source_code(self):
        print("")
        print("Load source code selected!")
        filename = input("Filename?[x86_64 .asm only]: ")
        self.disk.load_file(filename)
    
    ## quit
    def quit(self):
        print("")
        print("Quit selected!")
    
    
    # phase_2_menu
    def phase_2_menu(self):
        print("")
        print("a. Reset and load new source code")
        print("┕ b. View instructions")
        print("")
        print("c. Page source code.")
        print("")
        print("z. Quit")
   

    def page_application(self):
        max_instr_size = 4
        self.disk.page_application(max_instr_size) 

    def reset_simulator(self):
        print("")
        print("Reset simulator, selected!")

        # instance new component objects
        debug = self.bus.debug_info

        self.bus = Bus(debug)
        self.cpu = CPU(debug)
        
        cache_size = self.cache.cache_size
        block_size = self.cache.block_size
        self.cache = Cache()

        table_size = self.tlb.table_size
        self.tlb = TLB(table_size, debug)

        memory_size = self.memory.memory_size
        virtual_memory_size = self.virtual_memory_size
        self.memory = Memory(memory_size, virtual_memory_size, debug)

        self.disk = Disk(debug)
    
    ## phase_2_choice_A
    def reset_and_load_source_code(self):
        reset_simulator()
        load_source_code()
    
    ## phase_2_choice_B
    def view_instructions(self):
        print("")
        print("View instructions selected!")

        print("\n[PRINT] Printing source code...")
        for instruction in self.disk.source_code:
            print("[...] ", instruction.strip('\n'))

        input("[~] Press any key to continue...")

    ## phase_2_choice_C
    
    # phase_3_menu
    def phase_3_menu(self):
        print("")
        print("a. Reset and load new source code")
        print("┕ b. View instructions")
        print("")
        print("d. Load into memory")
        print("")
        print("z. Quit")
    
    ## phase_2_choice_A
    ## phase_2_choice_B
    
    
    ## phase_3-choice_D
    def load_into_memory(self):
        print("")
        print("Load into memory selected!")
        self.memory.load_initial_pages_of_program(self.disk, "disk")
        self.memory.map_pages_to_virtual(self.disk, "disk")
        self.cpu.synchronize_with_memory(self.memory, "virtual memory") 
    ## quit
    
    
    # phase_4_menu
    def phase_4_menu(self):
        print("")
        print("a. Reset and load new source code")
        print("┕ b. View instructions")
        print("")
        print("d. Simulate one instruction")
        print("┝ e. View Cache table")
        print("┝ f. View Cache statistics")
        print("┝ g. View registers")
        print("┝ h. View memory layout")
        print("┝ i. View virtual memory layout")
        print("┝ j. View page table")
        print("┕ k. View current run-time info")
        print("")
        print("z. Quit")
    
    ## phase_2_choice_A
    ## phase_2_choice_B
    ## phase_2_choice_C
    
    ## phase_4_choice_D
    def simulate_one_instruction(self):
        print("")
        print("Simulate one instruction selected!")
    
    ## phase_4_choice_E
    def view_cache_table(self):
        print("")
        print("View cache table selected!")
        self.cache.print_cache()
        input("[~] Enter any key to continue...")
    
    ## phase_4_choice_F
    def view_cache_stats(self):
        print("")
        print("View cache statstics selected!")
        
        input("[~] Enter any key to continue...")
    
    ## phase_4_choice_G
    def view_registers(self): 
        print("")
        print("View registers selected!")
        self.cpu.print_register_table()
        input("[~] Enter any key to continue...")
    
    
    ## phase_4_choice_H
    def view_memory_layout(self):
        print("")
        print("View memory layout selected!")
        self.memory.print_memory_page_table() 

        input("[~] Enter any key to continue...")
    ## phase_4_choice_I
    def view_virtual_mem_layout(self):
        print("")
        print("View virtual memory layout selected!")
        self.memory.print_virtual_with_position(self.cpu.register_table["pc"]) 
        input("[~] Enter any key to continue...")

    ## phase_4_choice_J
    def view_page_table(self): 
        print("")
        print("View page table selected!")
        self.disk.print_page_table()
        input("[~] Enter any key to continue...")
    
    ## phase_4_choice_K
    def view_runtime_info(self):
        print("")
        print("View runtime info selected!")
        input("[~] Enter any key to continue...")
    
    ## quit
    
    
    
    # phase_5_menu
    
    def phase_5_menu(self):
        print("")
        print("[ATTENTION] PROGRAM HAS FINISHED EXECUTION, RETURNING TO MENU!")
        
    ### same as phase 4 with message stating that execution has completed.
