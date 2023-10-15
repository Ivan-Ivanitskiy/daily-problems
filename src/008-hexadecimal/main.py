hex_map = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def to_hex(n):
    if n == 0:
        return '0'
    hex_number = ''
    while n > 0:
        hex_number = hex_map[n % 16] + hex_number
        n = n // 16
    return hex_number
  
print(to_hex(123))
# 7B