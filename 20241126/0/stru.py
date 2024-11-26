import struct
import random

with open('output', 'wb') as f:
    for i in range(10):
        stru = struct.pack('f3si', random.random(),
                           bytes((random.randint(1, 256),
                                  random.randint(1, 256),
                                  random.randint(1, 256))),
                           random.randint(-100, 100))

        f.write(stru)
