import sys 
original_stdout = sys.stdout
input_file = open("input.txt", 'r')
output_file = open('output.txt', 'w')
sys.stdin, sys.stdout = input_file, output_file
####     CODE BELOW     ####



print(input())
print(type(input()))

print(input())








