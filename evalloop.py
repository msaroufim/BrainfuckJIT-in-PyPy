from tape import Tape
import sys

def mainloop(program,bracket_map):
    tape = Tape()
    pc   = 0
    while pc < len(program):
        code = program[pc]

        if code == ">":
            tape.advance()

        elif code == "<":
            tape.devance()

        elif code == "+":
            tape.inc()

        elif code == "-":
            tape.dec()

        elif code == ".":
            sys.stdout.write(chr(tape.get()))

        elif code == ",":
            tape.set(ord(sys.stdin.read(1)))

        elif code == "[" and tape.get() == 0:
            pc = bracket_map[pc]

        elif code == "]" and tape.get() != 0:
            pc = bracket_map[pc]

        pc += 1

def parse(program):
    parsed = []
    bracket_map = {}
    leftstack = []

    pc = 0
    for char in program:
        if char in ('[',']','<','>','+','-',',','.'):
            parsed.append(char)

            if char == '[':
                leftstack.append(pc)
            elif char == ']':
                left = leftstack.pop()
                right = pc
                bracket_map[left]  = right
                bracket_map[right] = left
            pc += 1

    return "".join(parsed), bracket_map

def run(input):
    program, map = parse(input.read())
    mainloop(program,map)

if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    run(open(sys.argv[1],'r'))

