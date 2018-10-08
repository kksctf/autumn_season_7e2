#!/usr/bin/env python3

flag = [ord(i) for i in list(input("Enter flag: "))]

if \
(len(flag) == 11 and
(-7^flag[6] - 97*flag[10] + 52^flag[4] - (-55)^flag[5] + 4^flag[6] - (-96)^flag[8] + 15^flag[0] -(-54)*flag[4] + 48*flag[10] -(-80)*flag[5] + 95^flag[4] == 21691) and
(-54^flag[10] + (-83)^flag[10] + 97^flag[0] + 6^flag[5] + (-29)^flag[8] - 63*flag[8] + (-11)^flag[6] - (-85)^flag[3] - (-20)*flag[0] + 21^flag[5] - 75*flag[5] == 3761) and
(-5*flag[1] + -99*flag[0] + 45*flag[5] + (-37)^flag[4] - 70*flag[2] + (-68)^flag[9] - (-66)*flag[9] - (-69)^flag[3] + 59*flag[5] - (-10)*flag[9] + (-76)*flag[5] == -7591) and
(81*flag[3] + (-14)^flag[4] + (-79)^flag[7] + 36*flag[0] - 24*flag[3] + 67*flag[4] -(-80)^flag[6] - 66^flag[2] + (-55)^flag[5] + (-11)*flag[4] + 39*flag[10] == 1410) and
(26^flag[2] - 6*flag[6] - 4*flag[2] - 82*flag[4] + (-76)*flag[9] - (-93)*flag[2] + (-86)^flag[10] + (-93)*flag[7] - 90*flag[2] - (-18)^flag[8] + (-80)^flag[6] == 20716) and
(61*flag[2] + 7^flag[10] - 55^flag[8] - 96^flag[10] - 97^flag[7] + (-41)*flag[2] + (-32)^flag[1] - (-33)*flag[1] - 7*flag[0] + 41*flag[1] + (-64)*flag[10] == -2063) and
(-63*flag[4] + 63^flag[4] + (-63)*flag[3] + 4*flag[6] - (-41)^flag[7] + 11*flag[9] - 88^flag[0] - 45^flag[0] - (-74)^flag[0] - (-100)^flag[10] + 47*flag[8] == 4914) and
(-93*flag[4] - 76^flag[4] + 53*flag[4] - (-72)^flag[10] + (-9)*flag[8] + (-61)^flag[8] - 42*flag[9] - (-8)^flag[8] + (-63)^flag[7] + 60^flag[9] + (-77)^flag[6] == -15594) and
(18^flag[5] - 40*flag[3] - 81^flag[3] + (-51)*flag[1] - 48^flag[8] + 5*flag[2] - (-15)^flag[5] + (-50)*flag[5] - (-39)*flag[7] - (-20)*flag[5] + 29*flag[10] == 4329) and
(98*flag[3] + (-58)^flag[0] - 26*flag[2] + (-2)*flag[3] - (-70)^flag[8] - (-19)*flag[7] - (-56)^flag[5] + (-40)^flag[0] - (-93)^flag[3] + (-98)^flag[1] + 81*flag[6] == -14092) and
(43^flag[8] + (-68)^flag[1]+ (-86)*flag[6] - 68*flag[9] - (-53)^flag[2] - (-40)*flag[9] + 74^flag[10] + (-2)^flag[6] + 40^flag[2] - 26^flag[10] + (-13)*flag[3] == 13070)):
    print("yes, this is correct flag!")
else:
    print("wtf? go learn linear algebra")
