import re
subst = []
for i in range(3):
    subst.append(input().split())
Steps, Init, Final = input().split()
Steps = int(Steps)


#                            [step, index, newstring]
def find_steps(oldstring:str, step):
    # print(f'{len(step)*"    "}[{oldstring}]Current steps:', step)
    if oldstring == Final:
        # print(f'{(len(step)-1)*"    "}[{oldstring}]Found!')
        return step
    for i_s, (old, new) in enumerate(subst):
        if len(step) == Steps:
            # print(f'{len(step) * "    "}[{oldstring}]Step={len(step)}, path dead')
            return False
        # print(f'{len(step)*"    "}[{oldstring}]Trying', old, '=>', new)
        all_index = [s.start() for s in re.finditer(f'(?={old})', oldstring)]
        for index in all_index:
            # print(f'{len(step) * "    "}[{oldstring}]Replaced index', index)
            newstring = oldstring[:index] + new + oldstring[index+len(old):]
            step.append([i_s, index + 1, newstring])

            if newstring == Final:
                # print(f'{(len(step)-1)*"    "}[{oldstring}]Found!')
                return step
            else:
                gotcha = find_steps(newstring, step[:])
                if gotcha:
                    # print(f'{(len(step)-1)*"    "}[{oldstring}]Found!')
                    return gotcha
                else:
                    step = step[:-1]
                    # print(f'{len(step)*"    "}[{oldstring}]Rolledback Steps: {step}')
        if not all_index:
            # print(f'{len(step)*"    "}[{oldstring}]{old} Not in string.')
            pass
    return False


result = find_steps(Init, [])
if result: print('\n'.join([' '.join([str(a) for a in l]) for l in result]))
