#
# filename = 'tekst.txt'
#
# with open(filename, 'r') as fopen:
#     lines = fopen.readlines()
#
# # for nr in range(len(lines)):
# #   print(f'Linia {nr} -> {lines[nr]}')
#
#
# for nr, value in enumerate(lines):
#   print(f'linia {nr} --> {value}')
#
#
# with open('save.txt', 'w') as f:
#     f.write('Line 1')
#     f.write('Line 2')
#     f.write('Line 3')
#     f.write('Line 4')
#
with open('save.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')
    f.write('Line 4\n')
    f.write('The end!')


sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']

with open('save.txt', 'w') as f:
    f.write('----'.join(sweets_list))
# ważne  encoding="utf-8"
with open("tekst.txt", 'r',encoding="utf-8") as fopen:
    lines = fopen.readlines()
    print(lines)
