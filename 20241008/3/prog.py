matrix = []
s = input()
n = 1
gas = 0
water = 0
while s := input():
    n += 1
    gas += s.count('.')
    water += s.count('~')
    if s[1] == '#':
        break

h = len(s)
w = n
waterlines = water // (w - 2) + 1 * (water % (w - 2))
gaslines = h - 2 - waterlines
print('#' * w)
for i in range(gaslines):
    print('#' + '.' * (w - 2) + '#')
for i in range(waterlines):
    print('#' + '~' * (w - 2) + '#')
print('#' * w)
v = (h - 2) * (w - 2)
if gas > water:
    gas_str = '.' * 20 + f' {gas}/{v}'
    gas_str_len = len(gas_str)
    wlen = round(water / gas * 20)
    print(gas_str)
    print(f"{'~' * wlen}{' ' * (gas_str_len - wlen - len(str(water)) - len(str(v)) - 1)}{water}/{v}")
else:
    water_str = '~' * 20 + f' {water}/{v}'
    water_str_len = len(water_str)
    glen = round(gas / water * 20)
    print(f"{'.' * glen}{' ' * (water_str_len - glen - len(str(gas)) - len(str(v)) - 1)}{gas}/{v}")
    print(water_str)