import sys

data = sys.stdin.buffer.read()
N = int(data[0])
tail = data[1:]
L = len(tail)
parts = []
for i in range(N):
    part = tail[i * L // N: (i + 1) * L // N]
    parts.append(part)
parts.sort()
sys.stdout.buffer.write(data[:1])
for part in parts:
    sys.stdout.buffer.write(part)
