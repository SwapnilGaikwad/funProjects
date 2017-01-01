import sys

def main(argv):
   print "Hello World"
   return 0

def target(*args):
   return main, None

if __name__ == '__main__':
   main(sys.argv)
