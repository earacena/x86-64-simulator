# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: gui.py
# File Description: This file contains the functions related to the GUI component

# Class GUI
class GUI:

    def __init__(self, debug):
        self.debug_info = True

    def main_menu(self):
        print("")
        print("╔═══════════════════════════════════════════════╗")
        print("║                x86_64 Simulator               ║")
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
                    self.convert_to_binary()
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
                elif choice == "c":
                    self.view_binary()
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
                elif choice == "c":
                    self.view_binary()
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
        print("c. Convert to binary")
        print("")
        print("z. Quit")
    
    def reset_simulator(self):
        print("")
        print("Reset simulator, selected!")
    
    ## phase_2_choice_A
    def reset_and_load_source_code(self):
        reset_simulator()
        load_source_code()
    
    ## phase_2_choice_B
    def view_instructions(self):
        print("")
        print("View instructions selected!")
    
    ## phase_2_choice_C
    def convert_to_binary(self):
        print("")
        print("Convert to binary selected!")
    
    # phase_3_menu
    def phase_3_menu(self):
        print("")
        print("a. Reset and load new source code")
        print("┝ b. View instructions")
        print("┕ c. View binary")
        print("")
        print("d. Load into memory")
        print("")
        print("z. Quit")
    
    ## phase_2_choice_A
    ## phase_2_choice_B
    
    ## phase_3_choice_C
    def view_binary(self):
        print("")
        print("View binary selected!")
    
    ## phase_3-choice_D
    def load_into_memory(self):
        print("")
        print("Load into memory selected!")
    
    ## quit
    
    
    # phase_4_menu
    def phase_4_menu(self):
        print("")
        print("a. Reset and load new source code")
        print("┝ b. View instructions")
        print("┕ c. View binary")
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
    
    ## phase_4_choice_F
    def view_cache_stats(self):
        print("")
        print("View cache statstics selected!")
        
    
    ## phase_4_choice_G
    def view_registers(self): 
        print("")
        print("View registers selected!")
    
    
    ## phase_4_choice_H
    def view_memory_layout(self):
        print("")
        print("View memory layout selected!")
        
    
    ## phase_4_choice_I
    def view_virtual_mem_layout(self):
        print("")
        print("View virtual memory layout selected!")
    
    ## phase_4_choice_J
    def view_page_table(self): 
        print("")
        print("View page table selected!")
    
    
    ## phase_4_choice_K
    def view_runtime_info(self):
        print("")
        print("View runtime info selected!")
    
    ## quit
    
    
    
    # phase_5_menu
    
    def phase_5_menu(self):
        print("")
        print("[ATTENTION] PROGRAM HAS FINISHED EXECUTION, RETURNING TO MENU!")
        
    ### same as phase 4 with message stating that execution has completed.
