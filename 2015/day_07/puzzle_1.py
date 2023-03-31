
from re import findall

gates = dict()
with open('2015\\day_07\\input.txt') as file:
    text = file.read()

for line in text.splitlines():
    # Assignmnet
    if matches:= findall('(\w+) -> (\w+)', line):
        in1, out = matches[0]
        in1 = int(in1) if in1.isnumeric() else gates[in1]
        gates[out] = in1
    # AND
    elif matches:= findall('(\w+) AND (\w+) -> (\w+)', line):
        in1, in2, out = matches[0]
        in1 = int(in1) if in1.isnumeric() else gates[in1]
        in2 = int(in2) if in2.isnumeric() else gates[in2]
        gates[out] = in1 & in2
    # OR
    elif matches:= findall('(\w+) OR (\w+) -> (\w+)', line):
        in1, in2, out = matches[0]
        in1 = int(in1) if in1.isnumeric() else gates[in1]
        in2 = int(in2) if in2.isnumeric() else gates[in2]
        gates[out] = in1 | in2
    # LSHIFT
    elif matches:= findall('(\w+) LSHIFT (\w+) -> (\w+)', line):
        in1, in2, out = matches[0]
        in1 = int(in1) if in1.isnumeric() else gates[in1]
        in2 = int(in2) if in2.isnumeric() else gates[in2]
        gates[out] = in1 << in2
    # RSHIFT
    elif matches:= findall('(\w+) RSHIFT (\w+) -> (\w+)', line):
        in1, in2, out = matches[0]
        in1 = int(in1) if in1.isnumeric() else gates[in1]
        in2 = int(in2) if in2.isnumeric() else gates[in2]
        gates[out] = in1 >> in2
    # NOT
    elif matches:= findall('NOT (\w+) -> (\w+)', line):
        in1, out = matches[0]
        in1 = int(in1) if in1.isnumeric() else gates[in1]
        gates[out] = ~in1

print(gates)