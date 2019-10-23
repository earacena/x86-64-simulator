# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: cpu.py
# File Description: This file contains the functions related to the CPU component

class CPU:
    def __init__(self, bus, debug):
        if debug == True:
            print("[CPU] initializing...")

        ### Initialization code ###
        
        self.debug_info = debug
        # Number of lines before and after program counter printed when
        # the CPU prints program with position   
        self.size_of_print = 5
 
        # General purpose registers
        self.rax = 0
        self.rbx = 0 
        self.rcx = 0 
        self.rdx = 0
        self.r8  = 0
        self.r9  = 0

        # Special purpose registers
        self.program_counter = 0
        self.stack_ptr  = 0
        self.base_ptr   = 0
        self.instr_ptr  = 0
        self.rflags     = 0

        # Performance/timing variables
        self.current_instr_size = 0
        self.cpi = 0

        ###########################
        if debug == True:
            print("[CPU] finished initializing...")

    def ALU(self, op, dest_reg, src_reg, value):
       
        if self.debug_info == True:
            print("[CPU] ALU called with parameters: ")
            print("[CPU]\tOP:", op)
            print("[CPU]\tDest. reg:", dest_reg)
            print("[CPU]\tSrc. reg:", src_reg)
            print("[CPU]\tValue:", value)

        # mov
        # add
        # sub
        # cmp
        # jmp
        
    def print_register_table():
        padding = "___________________"
    
        print(padding + "Register Table " + padding)   
        print("| RAX    = ", rax)
        print("| RBX    = ", rbx)
        print("| RCX    = ", rcx)
        print("| RDX    = ", rdx)
        print("| R8     = ", r8)
        print("| R9     = ", r9)
        print("| PC     = ", pc)
        print("| RSP    = ", rsp)
        print("| RBP    = ", rbp)
        print("| RIP    = ", rip)
        print("| RFLAGS = ", rflags)
        print(padding + padding + padding)
  
    # display the position of the program counter and
    # program
    def print_program_with_position():
        # copy =  bus.communicate("cpu", "request page, print",
        #                         [self.size_of_pos, program_counter])

        # offset = (self.size_of_print + 1) * -1
        # for line in copy:
        #     print(program_counter + offset, |, line)
        #     program_counter = program_counter + 1

    
