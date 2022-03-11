# pyPCIe: Simple Python Module to access PCIe Endpoint BARs

pyPCIe provides a quick way to read/write registers in PCIe Base
Address Register (BAR) regions.

pyPCIe `mmap`s PCIe device BARs via the `resourceX` files in
`/sys/bus/pci/devices/[bus_id]` for read/write and provides functions
for 32 bit read/write requests.

*Note: the `resourceX` files in sysfs are typically only accessible as
root. The python scripts using pyPCIe might need to be run as root.*

## Example

```python
from pypcie import Device

# Bind to PCI device at "0000:03:00.0"
d = Device("0000:03:00.0")
# Access BAR 0
bar = d.bar[0]

# write 0xdeadbeef to BAR 0, offset 0x1000
bar.write(0x1000, 0xdeadbeef)

# read BAR 0, offset 0x1004
ret = bar.read(0x1004)
```
