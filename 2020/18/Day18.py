


with open('math.txt', 'r') as math:
    equations = [line.replace(' ','').strip() for line in math.readlines()]

def find_parens(expression):
    # print('find_parens', expression)
    parens = [0]
    idx = 1
    while len(parens) > 0 and idx < len(expression):
        s = expression[idx]
        if s == '(': parens.append(0)
        elif s == ')': parens.pop()
        idx += 1
    return expression[1:idx-1], idx

def eval_expression(expression):
    if '(' not in expression:
        result = int(expression[0])
        for idx in range(1,len(expression),2):
            if expression[idx] == '+':
                result += int(expression[idx+1])
            else: result *= int(expression[idx+1])
        return result
    else:
        idx = 0
        if expression[idx] == '(':
            paren, inc = find_parens(expression[idx:])
            result = eval_expression(paren)
            idx += inc
        else:
            result = int(expression[idx])
            idx += 1

        while idx < len(expression):
            op = expression[idx]
            next_sym = expression[idx+1]

            if next_sym == '(':
                paren, inc = find_parens(expression[idx+1:])
                val = eval_expression(paren)
                if op == '+': result += val
                else: result *= val
                idx += inc + 1
            else:
                if op == '+': result += int(expression[idx+1])
                else: result *= int(expression[idx+1])
                idx += 2

    return result


total = sum([eval_expression(eq) for eq in equations])
print('Part one:')
print(f'Sum of results = {total}\n')


import re

def modify_equation(eq):
    print(f'eq: {eq}')
    products = [exp for exp in eq.split('*')]
    print(f'products: {products}')
    # if '(' not in eq:
    #     products = [f'{exp}' if len(exp)>1 else exp for exp in eq.split('*')]
    #     # print(f'products: {products}')
    #     result = ''
    #     for product in products:
    #         additions = [exp for exp in product.split('+')]
    #         r_nest = additions[0]
    #         for addition in additions[1:]:
    #             r_nest = f'({r_nest}+{addition})'
    #         if result == '': result = r_nest
    #         else: result = f'{result}*{r_nest}'
    #     return result
    # else:
    #     expressions = []
    #     curr = 0
    #     start = 0
    #     while curr < len(eq)-1:
    #         if eq[curr] != '(':
    #             curr += 1
    #             continue
    #         else:
    #             expressions.append(modify_equation(eq[start:curr]))
    #             paren, inc = find_parens(eq[curr:])
    #             expressions.append(f'({modify_equation(paren)})')
    #             start = curr + inc
    #             curr = start
    #         curr += 1
    #     expressions.append(eq[start:curr+1])
    #     expressions = [exp for exp in expressions if len(exp)>0]

    #     return ''.join(expressions)





        
# def modify_equation(eq):
#     print(f'eq: {eq}')
#     if '(' not in eq:
#         products = [f'{exp}' if len(exp)>1 else exp for exp in eq.split('*')]
#         # print(f'products: {products}')
#         result = ''
#         for product in products:
#             additions = [exp for exp in product.split('+')]
#             r_nest = additions[0]
#             for addition in additions[1:]:
#                 r_nest = f'({r_nest}+{addition})'
#             if result == '': result = r_nest
#             else: result = f'{result}*{r_nest}'
#         return result
#     else:
#         expressions = []
#         curr = 0
#         start = 0
#         while curr < len(eq)-1:
#             if eq[curr] != '(':
#                 curr += 1
#                 continue
#             else:
#                 expressions.append(modify_equation(eq[start:curr]))
#                 paren, inc = find_parens(eq[curr:])
#                 expressions.append(f'({modify_equation(paren)})')
#                 start = curr + inc
#                 curr = start
#             curr += 1
#         expressions.append(eq[start:curr+1])
#         expressions = [exp for exp in expressions if len(exp)>0]

#         return ''.join(expressions)


# mod_equations = [ modify_equation(eq) for eq in equations ]

# total = sum([eval_expression(eq) for eq in mod_equations])
# print('Part two:')
# print(f'Sum of results = {total}\n')

eq = equations[2]
eq = '(9*7*5*9*9*8)+6+2*(7*7)*(9+7*9+4)'
# eq = '(9+2+7*(3+1))*2'

print(f'eq:  {eq}')
print(f'mod: {modify_equation(eq)}')