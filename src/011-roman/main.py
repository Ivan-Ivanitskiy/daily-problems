rom_map = [
    ['','I','II','III','IV','V','VI','VII','VIII','IX'],
    ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
    ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
    ['','M','MM','MMM']
    ]

def integer_to_roman(num):
    roman = ""
    i = 0
    while num > 0:
        remainder = num % 10
        roman = rom_map[i][remainder] + roman
        num = num // 10
        i += 1
    return roman

print(integer_to_roman(1000))
# M
print(integer_to_roman(48))
# XLVIII
print(integer_to_roman(444))
# CDXLIV