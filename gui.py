# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: gui.py
# File Description: This file contains the functions related to the GUI component

# Class GUI



# menu_loop
def menu_loop():
    input = ""
    phase = 1
    prompt("Choice: ")
    while input is not "z":
      if phase == 1:
          phase_1_menu()
          if input == "a":
              phase = 2
          elif input == "z":
              # Quit
              quit() 
      elif phase == 2:
          phase_2_menu()
          if input == "a":
              phase = 2
              reset_simulator()
              load_source_code()
          elif input == "b":
              view_instructions()
          elif input == "c":
              phase = 3
              convert_to_binary()
          elif input == "z":
              # Quit
              quit() 
      elif phase == 3:
          phase_3_menu()
          if input == "a":
              phase = 2
          elif input == "b":
              view_instructions()
          elif input == "c":
              view_binary()
          elif input == "d":
              load_into_memory()
          elif input == "z":
              # Quit
              quit() 
      elif phase == 4:
          phase_4_menu()
          if input == "a":
              phase = 2
              reset_simulator()
              load_source_code()
          elif input == "b":
              view_instructions()
          elif input == "c":
              view_binary()
          elif input == "d":
              simulate_one_instruction()
          elif input == "e":
              view_cache_table()
          elif input == "f":
              view_cache_stats()
          elif input == "g":
              view_registers()
          elif input == "h":
              view_memory_layout()
          elif input == "i":
              view_virtual_mem_layout()
          elif input == "j":
              view_page_table()
          elif input == "k":
              view_runtime_info()
          elif input == "z":
              # Quit
              quit() 
      else:
          # Phase 5
          phase = 1


# phase_1_menu
def phase_1_menu():
    print("A. Load source code")
    print("")
    print("Z. Quit")

## phase_1_choice_A
def load_source_code():
    print("Load source code selected!")

## quit
def quit():
    print("Quit selected!")


# phase_2_menu
def phase_2_menu():
    print("A. Reset and load new source code")
    print("B. View instructions")
    print("C. Convert to binary")
    print("")
    print("Z. Quit")

def reset_simulator():
    print("Reset simulator, selected!")

## phase_2_choice_A
def reset_and_load_source_code():
    reset_simulator()
    load_source_code()

## phase_2_choice_B
def view_instructions():
    print("View instructions selected!")

## phase_2_choice_C
def convert_to_binary():
    print("Convert to binary selected!")

# phase_3_menu
def phase_3_menu():
    print("A. Reset and load new source code")
    print("B. View instructions")
    print("C. View binary")
    print("D. Load into memory")
    print("")
    print("Z. Quit")

## phase_2_choice_A
## phase_2_choice_B

## phase_3_choice_C
def view_binary():
    print("View binary selected!")

## phase_3-choice_D
def load_into_memory():
    print("Load into memory selected!")

## quit


# phase_4_menu
def phase_4_menu():
    print("A. Reset and load new source code")
    print("B. View instructions")
    print("C. View binary")
    print("D. Simulate one instruction")
    print("E. View Cache table")
    print("F. View Cache statistics")
    print("G. View registers")
    print("H. View memory layout")
    print("I. View virtual memory layout")
    print("J. View page table")
    print("K. View current run-time info")
    print("")
    print("Z. Quit")

## phase_2_choice_A
## phase_2_choice_B
## phase_2_choice_C

## phase_4_choice_D
def simulate_one_instruction():
    print("Simulate one instruction selected!")

## phase_4_choice_E
def view_cache_table():
    print("View cache table selected!")

## phase_4_choice_F
def view_cache_stats():
    print("View cache statstics selected!")
    

## phase_4_choice_G
def view_registers(): 
    print("View registers selected!")


## phase_4_choice_H
def view_memory_layout():
    print("View memory layout selected!")
    

## phase_4_choice_I
def view_virtual_mem_layout():
    print("View virtual memory layout selected!")

## phase_4_choice_J
def view_page_table(): 
    print("View page table selected!")


## phase_4_choice_K
def view_runtime_info():
    print("View runtime info selected!")

## quit



# phase_5_menu

def phase_5_menu():
    print("[ATTENTION] PROGRAM HAS FINISHED EXECUTION, RETURNING TO MENU!")
    
### same as phase 4 with message stating that execution has completed.
