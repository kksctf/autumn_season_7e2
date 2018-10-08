#!/usr/bin/env python3

flag = [ord(i) for i in list(input("Enter flag: "))]

if \
(len(flag) == 5 and
flag[0] * 34 + flag[1] * 4 - flag[2] * 7 + flag[3] * 89 + flag[4] * 30 == 16327 and
flag[0] * 4 - flag[1] + flag[2] * 70 + flag[3] * 32 - flag[4] * 10 == 9936 and
flag[0] * 7 - flag[1] * 8 + flag[2] * 2 + flag[3] * 12 - flag[4] * 3 == 1191 and
flag[0] * 8 + flag[1] * 17 - flag[2] * 3 + flag[3] * 2 - flag[4] * 14 == 1066 and
flag[0] * 43 - flag[1] * 22 + flag[2] * 7 - flag[3] * 13 + flag[4] * 10 == 2546):
    print("yes, this is correct flag!")
else:
    print("wtf? go learn linear algebra")
