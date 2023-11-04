import sys

if (len(sys.argv) != 3):
    print ("Only Two arguments are needed")
    exit(1)
try:
    A = int(sys.argv[1])
    B = int(sys.argv[2])
except ValueError:
    print("Error: Parsing failed")
    exit(1)
print(
    " Sum         : ", A + B, '\n',
    "Difference  : ", A - B, '\n',
    "Product     : ", A * B, '\n',
    "Quotient    : ", ((A / B) if B != 0 else "ERROR (division by zero)"), '\n',
    "Remainder   : ", ((A % B) if B != 0 else "ERROR (modulo by zero)")
)