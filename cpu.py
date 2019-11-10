"""
    Project: x86_64 Hardware Simulator
    Name: Emanuel Aracena
    Filename: cpu.py
    File Description: This file contains the functions related to the CPU component
"""
# Force python to use Python3 print function
from __future__ import print_function

# Components
from bus import Bus
from common import phex

class CPU:
    """ This class represents the CPU component. """
    def __init__(self, debug):
        """ Initialize the data members of the component. """
        self.debug_info = debug

        if self.debug_info is True:
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
        self.current_instr_size = 0
        self.current_instr_cycles = 0
        self.cpi = 0

        ###########################

        if self.debug_info is True:
            print("[CPU] finished initializing...")

    def synchronize_with_memory(self, callee, callee_name):
        """
            Point the program counter to the first instruction to execute in virtual
            memory.
        """
        starting_position = self.bus.communicate("cpu", callee, callee_name,
                                                 "virtual memory, starting position", "")
        self.register_table["pc"] = int(starting_position, 0)

    def fetch_next_instruction(self, callee, callee_name):
        """
            Retrieve the instruction that is (size of instruction) positions from the current
            position pointed to by the program counter, then increment the counter that many
            positions.
        """
        instruction = self.bus.communicate("cpu", callee, callee_name, "cache, give block",
                                           self.register_table["pc"] + 4)
        self.register_table["pc"] = self.register_table["pc"] + 4

        # Cache missed
        if instruction == "MISS":
            return "CACHE MISSED"

        # parse instruction
        parsed = self.parse_instruction(instruction)

        return parsed

    def parse_instruction(self, instruction):
        """
            Seperate given instruction string into op, dest_reg, src_reg and value variables.
            Then package them together into a list and return it.
        """
        if self.debug_info is True:
            print("\n[CPU] parsing instruction '" + instruction + "'...")

        register_id = ["rax", "rbx", "rcx", "rdx", "r8", "r9", "rsp", "rbp", "rip"]
        op = ""
        dest_reg = ""
        src_reg = ""
        value = ""

        # just a label, ignore
        if ':' in instruction:
            return "label"

        split_instr = instruction.split(',')
        if len(split_instr) == 1:
            print(split_instr)
            split_instr = split_instr[0].split(' ')
        else:
            split_instr[0] = split_instr[0].split(' ', 1)
            split_instr = [split_instr[0][0], split_instr[0][1], split_instr[1].lstrip(' ')]

        if len(split_instr) == 2:
            value = split_instr[1]
        elif str(split_instr[2]) in register_id:
            src_reg = split_instr[2]
            dest_reg = split_instr[1]
        else:
            dest_reg = split_instr[1]
            value = split_instr[2]

        op = split_instr[0]

        if self.debug_info is True:
            print("[CPU] parsing done, result:")
            print("[...]   length:", len(split_instr))
            print("[...]    split:", split_instr)
            print("[...]       op: ", op)
            print("[...] dest_reg: ", dest_reg)
            print("[...]  src_reg: ", src_reg)
            print("[...]    value: ", value)

        parsed = {
            "op": op,
            "dest_reg": dest_reg,
            "src_reg": src_reg,
            "value": value
        }

        return parsed

    def ALU(self, op, dest_reg, src_reg, value, callee, callee_name):
        """
            ALU will apply the given operation 'op', to the registers given or perform
            special behaviors. Requires virtual memory communication to point to the
            appropriate place when a jump is executed.
        """
        if self.debug_info is True:
            print_alu_debug(op, dest_reg, src_reg, value)

        # Mov operation
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
            self.register_table["rflags"] = (self.register_table[dest_reg] ==
                                             self.register_table[src_reg])

        # jmp
        if op == "jmp":
            # self.bus.communicate("cpu", callee, callee_name,
            #                      "virtual memory, find position of label", value)
            self.register_table["pc"] = int(value, 0)

    def print_register_table(self):
        """ Print the value of all the registers. """
        print("[CPU] Printing register table...")
        print("[...] RAX    = ", phex(self.register_table["rax"], 32))
        print("[...] RBX    = ", phex(self.register_table["rbx"], 32))
        print("[...] RCX    = ", phex(self.register_table["rcx"], 32))
        print("[...] RDX    = ", phex(self.register_table["rdx"], 32))
        print("[...] R8     = ", phex(self.register_table["r8"], 32))
        print("[...] R9     = ", phex(self.register_table["r9"], 32))
        print("[...] PC     = ", phex(self.register_table["pc"], 32))
        print("[...] RSP    = ", phex(self.register_table["rsp"], 32))
        print("[...] RBP    = ", phex(self.register_table["rbp"], 32))
        print("[...] RIP    = ", phex(self.register_table["rip"], 32))
        print("[...] RFLAGS = ", phex(self.register_table["rflags"], 6))

    def print_program_with_position(self, callee, callee_name):
        """ Display the position of the program counter and program. """
        # defualt offset 4 positions before, 4 positions after
        self.bus.communicate("cpu", callee, callee_name, "virtual memory, print position",
                             self.register_table["pc"])

def print_alu_debug(op, dest_reg, src_reg, value):
    """ Print debug information for ALU calls in this format. """
    print("[CPU] ALU |        op: ", op)
    print("          |  dest_reg: ", dest_reg)
    print("          |   src_reg: ", src_reg)
    print("          |     value: ", value)

def main():
    """ Unit test. """
    debug = True

    cpu = CPU(debug)

    # Test ALU
    # placeholder callee/callee_name for simple testing
    callee = "virtual memory"
    callee_name = "placeholder"

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
    cpu.parse_instruction("mov DWORD PTR[rbp+8], 10")
    cpu.parse_instruction("jmp label")
