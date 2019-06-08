# Copyright B. Soares
#
# Released under the MIT License
# https://github.com/basoares/google-code-jam/blob/master/LICENSE
#

for tc in range(int(input())):
    N = input()
    P = input()
    path = ''.join('E' if p == 'S' else 'S' for p in P)
    print('Case #{}: {}'.format(tc+1, path))


