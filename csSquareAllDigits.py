# Create a function that given an integer, returns an integer where every 
# digit in the input integer is squared.

# Examples:
# csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
# csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9

# Notes
# [execution time limit] 4 seconds (py3)
# [input] integer n
# [output] integer

def csSquareAllDigits(n):
    x = ''.join(str(int(i)**2) for i in str(n))
    return int(x)
    
        
print(csSquareAllDigits(9119))
print(csSquareAllDigits(2483))
