import sys

'''
00 - End of the program
02 - Push
03 - Pop
04 - Print
05 - Add
06 - Subtract
'''

stack = []

OP_EOP	= "00"
OP_EOI	= "01"
OP_PUSH	= "02"
OP_POP	= "03"
OP_PRINT= "04"
OP_ADD	= "05"
OP_SUB	= "06"

def load_program(argv):
   prog = open(argv)
   lines = prog.read().replace("\n", " ")
   lines = lines.split(" ")
   prog.close()
   return lines

def do_PUSH(i, lines):
   toPush = int(lines[i + 1], 16)
   stack.append(toPush)

def do_POP():
   return stack.pop()

def do_PRINT():
   print stack

def do_ADD():
   num1 = stack.pop()
   num2 = stack.pop()
   total = num1 + num2
   stack.append(total)

def do_SUB():
   num1 = stack.pop()
   num2 = stack.pop()
   total = num1 - num2
   stack.append(total)

def execute_program(lines):
   loop = 1
   i = 0
   while loop == 1:
      instruction = lines[i]
      if instruction == OP_EOP:
         loop = 0
      elif instruction == OP_PUSH:
         do_PUSH(i, lines)
      elif instruction == OP_POP:
         do_POP()
      elif instruction == OP_PRINT:
         do_PRINT()
      elif instruction == OP_ADD:
         do_ADD()
      elif instruction == OP_SUB:
         do_SUB()
      i+=1

def run_program(argv):
   progLines = load_program(argv)
   execute_program(progLines)

def main(argv):
   run_program(argv[1])
   return 0

def target(*args):
   return main, None

if __name__ == '__main__':
   main(sys.argv)
