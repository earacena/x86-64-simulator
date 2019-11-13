"""
    Project: x86_64 Hardware Simulator
    Author: Emanuel Aracena
    Filename: tlb.py
    File Description: This file contains the implementation of the TLB component
"""

# Force python to use Python3 print function
from __future__ import print_function

# TLB holds a long list of recently translated virtual addresses
class TLB:
    """
        This class represents the TLB component, the TLB holds a long list of
        recently translated virtual addresses mapped to physical addresses.
    """
    def __init__(self, table_size, debug):
        """ Initialize the component's data members. """
        self.debug_info = debug
        self.table_size = table_size
        self.virtual_page_table = [None] * self.table_size
        self.num_of_entries = 0

    def find_physical_address(self, virtual_address):
        """ Find physical address of given virtual address, if stored in TLB. """
        if self.debug_info is True:
            print("[TLB] Looking for translation for address '" + str(virtual_address) + "'...")

        for entry in self.virtual_page_table:
            if entry != None and entry[0] == virtual_address:
                return entry[1]

        return "TLB MISSED"

    def store_translation(self, virtual_address, physical_address):
        """ Store a translation entry. """
        if self.debug_info is True:
            print("[TLB] Storing translation entry [" + str(virtual_address) + ", " +
                  str(physical_address) + "]...")
        self.virtual_page_table[self.num_of_entries % self.table_size] = [virtual_address,
                                                                          physical_address]
        self.num_of_entries = self.num_of_entries + 1

def main():
    """ Unit test. """
    debug = True
    table_size = 20
    tlb = TLB(table_size, debug)
    tlb.store_translation('0xAAAA', '0x0010')

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
