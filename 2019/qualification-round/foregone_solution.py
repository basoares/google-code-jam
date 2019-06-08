# Copyright B. Soares
#
# Released under the MIT License
# https://github.com/basoares/google-code-jam/blob/master/LICENSE
#

num_tests = int(input())
for i in range(num_tests):
    number = input()
    a = number.replace('4', '3')
    b = ''.join('1' if d == '4' else '0' for d in number).lstrip('0')
    print('Case #{}: {} {}'.format(i+1, a, b))
