#!/usr/bin/python3
import os
from .bar import Bar


class Device(object):
    """ Create a Device object for a PCIe device.

    :param str pciid: PCI bus ID as string, e.g. "0000:03:00.0"

    """

    __base = "/sys/bus/pci/devices/"

    def __init__(self, pciid: str):
        self.__base = os.path.join(self.__base, str(pciid))
        if not os.access(self.__base, os.F_OK):
            raise ValueError("Device not found: %s" % (self.__base))
        self.bar = [None] * 6
        for barnum in range(0, 6):
            resfile = os.path.join(self.__base, "resource%d" % (barnum))
            if os.access(resfile, os.F_OK):
                self.bar[barnum] = Bar(resfile)

    def __get_attr__(self, attr: str, attr_type: type):
        """ Read a sysfs attribute and convert the received string to the
        given attribute type.

        :param str attr: attribute name
        :param type attr_type: data type the attribute is casted to.
        :returns: attribute value
        :rtype: attr_type

        """
        path = os.path.join(self.__base, attr)
        if not os.access(path, os.F_OK):
            raise ValueError("Cannot read attribute %s" % (attr))
        with open(path) as f:
            val = f.read()[:-1]  # strip newline
            if attr_type is int:
                return attr_type(val, 0)
            else:
                return attr_type(val)

    def vendor(self) -> int:
        """ Get the PCI vendor ID.

        :returns: PCI vendor ID
        :rtype: int
        """
        return self.__get_attr__("vendor", int)

    def device(self) -> int:
        """ Get the PCI device ID.

        :returns: PCI device ID
        :rtype: int
        """
        return self.__get_attr__("device", int)

    def revision(self) -> int:
        """ Get the PCI revision Number.

        :returns: PCI revision Number
        :rtype: int
        """
        return self.__get_attr__("revision", int)

    def subsystem_vendor(self) -> int:
        """ Get the PCI subsystem vendor ID.

        :returns: PCI subsystem vendor ID
        :rtype: int
        """
        return self.__get_attr__("subsystem_vendor", int)

    def subsystem_device(self) -> int:
        """ Get the PCI subsystem device ID.

        :returns: PCI subsystem device ID
        :rtype: int
        """
        return self.__get_attr__("subsystem_device", int)
