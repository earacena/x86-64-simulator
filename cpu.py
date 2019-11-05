# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: cpu.py
# File Description: This file contains the functions related to the CPU component

from bus import Bus
from common import phex

class CPU:
    def __init__(self, debug):
        self.debug_info = debug

        if self.debug_info == True:
            print("[CPU] initializing...")

        self.bus = Bus(debug)

        self.register_table = {
            # General purpose registers
            "rax":    0,
            "rbx":    0,
            "rcx":    0,
            "rdx":    0,
            "r8":     0,
            "r9":     0,
            # Special purposee registers
            "pc":     0,
            "rsp":    0,
            "rbp":    0,
            "rip":    0,
            "rflags": 0,
        }

        # Performance/timing variables
        self.current_instr_size   = 0
        self.current_instr_cycles = 0
        self.cpi = 0

        ###########################i

        if self.debug_info == True:
            print("[CPU] finished initializing...")
    
    def synchronize_with_memory(self, callee, callee_name):
        starting_position = self.bus.communicate("cpu", callee, callee_name, "virtual memory, starting position")
        self.register_table["pc"] = starting_position

    def fetch_next_instruction(self, callee, callee_name):
        instruction = self.bus.communicate("cpu", callee, callee_name, "cache, give block", self.register_table["pc"] + 4)
        # parse instruction
        self.execute_instruction(instruction)


    def parse_instruction(self, instruction):
        # seperate instruction into op, dest_reg, src_reg, value
        if self.debug_info == True:
            print("\n[CPU] parsing instruction '" + instruction + "'...")

        register_id = ["rax", "rbx", "rcx", "rdx", "r8", "r9", "rsp", "rbp", "rip"]

        op = ""
        dest_reg = ""
        src_reg = ""
        value = ""


        cleaned = instruction.replace(',', '')
        split = cleaned.split(" ")        

        if len(split) == 2:
            value = split[1]
        elif str(split[2]) in register_id:
            src_reg = split[2]
            dest_reg = split[1]
        else:
            dest_reg = split[1]
            value = split[2]
        
        op = split[0]

        if self.debug_info == True:
            print("[CPU] parsing done, result:")
            print("[...]   length:", len(split))
            print("[...]    split:", split)
            print("[...]       op: ", op)
            print("[...] dest_reg: ", dest_reg)
            print("[...]  src_reg: ", src_reg)
            print("[...]    value: ", value)

        return [op, dest_reg, src_reg, value]

    def ALU(self, op, dest_reg, src_reg, value, callee, callee_name):
        if self.debug_info == True:
            self.print_alu_debug(op, dest_reg, src_reg, value)

        # mov
        if op == "mov":
            # Check if moving value or register
            if value != "":
                self.register_table[dest_reg] = int(value, 0)
            else:
                self.register_table[dest_reg] = self.register_table[src_reg]
        
        # add
        if op == "add":
            # Check if adding value or register
            if value != "":
                self.register_table[dest_reg] += int(value, 0)
            else:
                self.register_table[dest_reg] += self.register_table[src_reg]

        # sub
        if op == "sub":
            # Check if adding value or register
            if value != "":
                self.register_table[dest_reg] -= int(value, 0)
            else:
                self.register_table[dest_reg] -= self.register_table[src_reg]

        # cmp
        if op == "cmp":
           self.register_table["rflags"] = (self.register_table[dest_reg] == self.register_table[src_reg])

        # jmp
        if op == "jmp":
            # self.bus.communicate("cpu", callee, callee_name, "virtual memory, find position of label", value)
            self.register_table["pc"] = int(value, 0)


    # Print the values of all the registers        
    def print_register_table(self):
        padding = "___________________"
    
        print(padding + "Register Table " + padding)   
        print("| RAX    = ",phex(self.register_table["rax"], 6))
        print("| RBX    = ",phex(self.register_table["rbx"], 6))
        print("| RCX    = ",phex(self.register_table["rcx"], 6))
        print("| RDX    = ",phex(self.register_table["rdx"], 6))
        print("| R8     = ",phex(self.register_table["r8"], 6))
        print("| R9     = ",phex(self.register_table["r9"], 6))
        print("| PC     = ",phex(self.register_table["pc"], 6))
        print("| RSP    = ",phex(self.register_table["rsp"], 6))
        print("| RBP    = ",phex(self.register_table["rbp"], 6))
        print("| RIP    = ",phex(self.register_table["rip"], 6))
        print("| RFLAGS = ",phex(self.register_table["rflags"], 6))
        print(padding + padding + padding)
  
    # Display the position of the program counter and program
    def print_program_with_position(self, callee, callee_name):
        # defualt offset 4 positions before, 4 positions after
        self.bus.communicate("cpu", callee, callee_name, "virtual memory, print position", self.register_table["pc"])

    def print_alu_debug(self, op, dest_reg, src_reg, value):    
        print("[CPU] ALU |        op: ", op)
        print("          |  dest_reg: ", dest_reg)
        print("          |   src_reg: ", src_reg)
        print("          |     value: ", value)

def main():
    debug = True

    cpu = CPU(debug)

    # Test ALU
    # placeholder callee/callee_name for simple testing
    callee = "virtual memory"
    callee_name = "placeholder'"
    
    # mov
    cpu.ALU("mov", "rax", "", "5", callee, callee_name)
    cpu.ALU("mov", "rbx", "rax", "", callee, callee_name)
    cpu.print_register_table()

    # add
    cpu.ALU("add", "rax", "", "5", callee, callee_name)
    cpu.ALU("add", "rbx", "rax", "", callee, callee_name)
    cpu.print_register_table()

    # sub
    cpu.ALU("mov", "rax", "", "5", callee, callee_name)
    cpu.ALU("mov", "rbx", "rax", "", callee, callee_name)
    cpu.print_register_table()

    # cmp
    cpu.ALU("cmp", "rax", "rbx", "", callee, callee_name)
    cpu.print_register_table()

    # jmp
    # cpu.ALU("jmp", "", "", "label")
    # cpu.print_register_table()

    # parse instruction test
    cpu.parse_instruction("mov rax, 0")  
    cpu.parse_instruction("mov rax, rbx")  
    cpu.parse_instruction("add rax, 0")  
    cpu.parse_instruction("add rax, rbx")  
    cpu.parse_instruction("sub rax, 0")  
    cpu.parse_instruction("sub rax, rbx")  
    cpu.parse_instruction("cmp rax, 0")


    #cpu.parse_instruction("jmp label")  
                                         
