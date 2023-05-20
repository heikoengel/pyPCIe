#!/usr/bin/python3
import os
from mmap import mmap, PROT_READ, PROT_WRITE, PAGESIZE
from struct import pack, unpack


class Bar(object):
    """ Create a Bar instance that ``mmap()`` s a PCIe device BAR.

    :param str filename: sysfs filename for the corresponding resourceX file.

    """

    def __init__(self, filename: str):
        self.__map = None
        self.__stat = os.stat(filename)
        fd = os.open(filename, os.O_RDWR)
        self.__map = mmap(fd, 0, prot=PROT_READ | PROT_WRITE)
        os.close(fd)

    def __del__(self):
        if self.__map is not None:
            self.__map.close()

    def __check_offset(self, offset: int):
        """ Check if the given offset is properly DW-aligned and the access
            falls within the BAR size.

        """
        if offset & 0x3:
            raise ValueError("unaligned access to offset 0x%x" % (offset))
        if offset + 3 > self.size:
            raise ValueError("offset (0x%x) exceeds BAR size (0x%x)" %
                             (offset, self.size))

    def read(self, offset: int):
        """ Read a 32 bit / double word value from offset.

        :param int offset: BAR byte offset to read from.
        :returns: Double word read from the given BAR offset.
        :rtype: double word / 32 bit unsigned long / int

        """
        self.__check_offset(offset)
        reg = self.__map[offset:offset+4]
        return unpack("<L", reg)[0]

    def write(self, offset: int, data: int):
        """ Write a 32 bit / double word value to offset.

        :param int offset: BAR byte offset to write to.
        :param int data: double word to write to the given BAR offset.
        """
        self.__check_offset(offset)
        self.__map.seek(offset)
        reg = pack("<L", data)
        # write to map. no ret. check: ValueError/TypeError is raised on error
        self.__map.write(reg)
        # Flush current page for immediate update.
        page_offset = offset & (~(PAGESIZE - 1) & 0xffffffff)
        self.__map.flush(page_offset, PAGESIZE)
        # TODO: check return value, only for >=Python3.8

    @property
    def size(self):
        """
        Get the size of the BAR.

        :returns: BAR size in bytes.
        :rtype: int
        """
        return self.__stat.st_size
