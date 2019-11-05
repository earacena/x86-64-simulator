# Project: x86_64 Hardware Simulator
# Name: Emanuel Aracena
# Filename: tlb.py
# File Description: This file contains the implementation of the TLB component

from bus import Bus
from common import phex

# Unit testing only, must not be included/implemented in interface/methods
from disk import Disk
from memory import Memory

# TLB holds a long list of recently translated virtual addresses
class TLB:
    def __init__(self, table_size):
        self.debug_info = True
        self.table_size = table_size
        self.virtual_page_table = [None] * self.table_size
        self.num_of_entries = 0

    def find_physical_address(self, virtual_address):
        for entry in self.virtual_page_table:
            if entry[0] == virtual_address:
                return entry[1]

        return "TLB MISS"

    def store_translation(self, virtual_address, physical_address):
        self.virtual_page_table[num_of_entries % self.table_size] = [virtual_address, physical_address]
        self.num_of_entries = self.num_of_entries + 1

# Unit test
def main():
    debug = True

    tlb = TLB(debug)
    tlb.virtual_page_table.append(['0xAAAA', '0x0010'])

    # Test confirmed virtual address    
    test_virt_addr = '0xAAAA'
    print("\n[Test] Looking for physical address for '" + test_virt_addr  + "'...")
    physical_address = tlb.find_physical_address(test_virt_addr)
    print("[...] Result/Status: ", physical_address)

    # Test if no such address found
    test_virt_addr = '0xBBBB'
    print("\n[Test] Looking for physical address for '" + test_virt_addr  + "'...")
    physical_address = tlb.find_physical_address(test_virt_addr)
    print("[...] Result/Status: ", physical_address)
