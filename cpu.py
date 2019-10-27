# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: cpu.py
# File Description: This file contains the functions related to the CPU component

class CPU:
    def __init__(self, bus, debug):
        if debug == True:
            print("[CPU] initializing...")

        ### Initialization code ###

        # debug info flag        
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

        # Virtual Memory Address variables
        self.virtual_memory_used = 0
        # {"A[1]": "020"}
        # left value is data being requested, right side is virtual address
        self.virtual_memory = {}

        # Performance/timing variables
        self.current_instr_size   = 0
        self.current_instr_cycles = 0
        self.cpi = 0

        ###########################
        if debug == True:
            print("[CPU] finished initializing...")

    def ALU(self, op, dest_reg, src_reg, value):
       
        if self.debug_info == True:
            self.print_alu_debug(op, dest_reg, src_reg, value)

        # mov
        if op == "mov":
            return;

        # add
        if op == "add":
            return;

        # sub
        if op == "sub":
            return;

        # cmp
        if op == "cmp":
            return;

        # jmp
        if op == "jmp":
            return;


    # Print the values of all the registers        
    def print_register_table(self):
        padding = "___________________"
    
        print(padding + "Register Table " + padding)   
        print("| RAX    = ", self.rax)
        print("| RBX    = ", self.rbx)
        print("| RCX    = ", self.rcx)
        print("| RDX    = ", self.rdx)
        print("| R8     = ", self.r8)
        print("| R9     = ", self.r9)
        print("| PC     = ", self.pc)
        print("| RSP    = ", self.rsp)
        print("| RBP    = ", self.rbp)
        print("| RIP    = ", self.rip)
        print("| RFLAGS = ", self.rflags)
        print(padding + padding + padding)
  
    # Display the position of the program counter and program
    def print_program_with_position(self):
        # copy =  bus.communicate("cpu", "request page, print",
        #                         [self.size_of_pos, program_counter])

        # offset = (self.size_of_print + 1) * -1
        # for line in copy:
        #     print(program_counter + offset, |, line)
        #     program_counter = program_counter + 1
        pass

    def print_alu_debug(self, op, dest_reg, src_reg, value):    
        print("[CPU] ALU |        op: ", op)
        print("          |  dest_reg: ", dest_reg)
        print("          |   src_reg: ", src_reg)
        print("          |     value: ", value)

