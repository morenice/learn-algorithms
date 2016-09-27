# -*- coding: utf-8 -*-


def validation(max_input_num, check_sequence):
    stack = list()
    stack_oper = list()

    for i in range(1, max_input_num+1):
        stack.append(i)
        stack_oper.append('+')

        while True:
            if len(stack) == 0 or len(check_sequence) == 0:
                break

            if check_sequence[0] == stack[len(stack)-1]:
                del(check_sequence[0])
                stack.pop()
                stack_oper.append('-')
            else:
                break

    if len(check_sequence) != 0:
        print("NO")

    for oper in stack_oper:
        print(oper)


if __name__ == '__main__':
    max_input_num = input()

    check_sequence = list()
    for i in range(int(max_input_num)):
        seq = input()
        check_sequence.append(int(seq))

    validation(int(max_input_num), check_sequence)
