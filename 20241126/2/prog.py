import sys

data = sys.stdin.buffer.read()
txt = data.decode('utf-8', errors="replace").encode('latin1', errors="replace").decode('CP1251', errors="replace")
sys.stdout.write(txt)
