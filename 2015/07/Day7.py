

signal_map = {}
signal_val = {}
operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']

class Gate:

    def __init__(self, in_gate1: str, in_gate2: str, in_value: int, operator):
        self.in_gate1 = in_gate1
        self.in_gate2 = in_gate2
        self.in_value = in_value
        self.func = operator
        self.value = 0

gates_to_do = []

with open('signals.txt', 'r') as signals:
    for line in signals.readlines():
        parts = line.split('->')
        out = parts[1].strip()
        signal_val[out] = -1
        input_parts = parts[0].strip().split(' ')

        if len(input_parts) == 1:
            in_val = input_parts[0]
            if in_val.isnumeric():
                signal_map[out] = Gate('', '', int(in_val), "=")
                gates_to_do.append(out)
            else:
                signal_map[out] = Gate(in_val, '', -1, "=")
        elif len(input_parts) == 2:
            signal_map[out] = Gate(input_parts[1], '', -1, input_parts[0])
        else:
            op = input_parts[1]
            if op == 'RSHIFT' or op == 'LSHIFT':
                signal_map[out] = Gate(input_parts[0], '', int(input_parts[2]), op)
            if op == 'OR':
                signal_map[out] = Gate(input_parts[0], input_parts[2], -1, op)
            if op == 'AND':
                first_and = input_parts[0]
                if first_and.isnumeric():
                    signal_map[out] = Gate('', input_parts[2], int(first_and), op)
                else:
                    signal_map[out] = Gate(first_and, input_parts[2], -1, op)


# Recursive solution
def get_gate_value(wire):
    if signal_val[wire] >= 0:
        return signal_val[wire]
    gate = signal_map[wire]
    if gate.func == '=':
        if gate.in_value >= 0:
            signal_val[wire] = gate.in_value
            return gate.in_value
        else:
            signal_val[wire] = get_gate_value(gate.in_gate1)
            return signal_val[wire]
    elif gate.func == 'AND':
        if gate.in_gate1 == '':
            signal_val[wire] = gate.in_value & get_gate_value(gate.in_gate2)
            return signal_val[wire]
        else:
            signal_val[wire] = get_gate_value(gate.in_gate1) & get_gate_value(gate.in_gate2)
            return signal_val[wire]
    elif gate.func == 'OR':
        signal_val[wire] = get_gate_value(gate.in_gate1) | get_gate_value(gate.in_gate2)
        return signal_val[wire]
    elif gate.func == 'NOT':
        signal_val[wire] = ~get_gate_value(gate.in_gate1)
        return signal_val[wire]
    elif gate.func == 'LSHIFT':
        signal_val[wire] = get_gate_value(gate.in_gate1) << gate.in_value
        return signal_val[wire]
    elif gate.func == 'RSHIFT':
        signal_val[wire] = get_gate_value(gate.in_gate1) >> gate.in_value
        return signal_val[wire]

signal = get_gate_value('a')
print(f"The signal at 'a' = {signal}")

# Recursive solution
# def get_gate_value(wire, vals_finished):
#     # print(wire)
#     gate = signal_map[wire]
#     if gate.func == '=':
#         if gate.in_value >= 0:
#             val = gate.in_value
#             vals_finished += 1
#             print(f'Vals finished: {vals_finished}')
#             return val, vals_finished
#         else:
#             val, finished = get_gate_value(gate.in_gate1, vals_finished)
#             finished += 1
#             print(f'Vals finished: {finished}')
#             return val, finished
#     elif gate.func == 'AND':
#         if gate.in_gate1 == '':
#             val, finished = get_gate_value(gate.in_gate2, vals_finished)
#             finished += 1
#             print(f'Vals finished: {finished}')
#             return gate.in_value & val, finished
#         else:
#             val, finished = get_gate_value(gate.in_gate1, vals_finished)
#             finished += 1
#             print(f'Vals finished: {finished}')
#             val2, finished2 = get_gate_value(gate.in_gate2, finished)
#             finished2 += 1
#             print(f'Vals finished: {finished2}')
#             return val & val2, finished + finished2
#     elif gate.func == 'OR':
#         val, finished = get_gate_value(gate.in_gate1, vals_finished)
#         finished += 1
#         print(f'Vals finished: {finished}')
#         val2, finished2 = get_gate_value(gate.in_gate2, finished)
#         finished2 += 1
#         print(f'Vals finished: {finished2}')
#         return val | val2, finished + finished2
#     elif gate.func == 'NOT':
#         val, finished = get_gate_value(gate.in_gate1, vals_finished)
#         finished += 1
#         print(f'Vals finished: {finished}')
#         return ~val, finished
#     elif gate.func == 'LSHIFT':
#         val, finished = get_gate_value(gate.in_gate1, vals_finished)
#         finished += 1
#         print(f'Vals finished: {finished}')
#         return val  << gate.in_value, finished
#     elif gate.func == 'RSHIFT':
#         val, finished = get_gate_value(gate.in_gate1, vals_finished)
#         finished += 1
#         print(f'Vals finished: {finished}')
#         return val >> gate.in_value, finished
    

# signal = get_gate_value('a', 0)
# print(f"The signal at 'a' = {signal}")

