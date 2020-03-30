risto1 = [12, 34, 36, 71, 3, 42]
risto2 = [53, 23, 16, 24, 5, 15]
risto3 = [1, 34, 10, 91, 43, 26]
suuji = 34

if suuji in risto1 or (suuji in risto2 and suuji in risto3):
    print(risto1[0])
elif suuji in risto2 or (suuji in risto3 and suuji in risto1):
    print(risto2[0])
elif suuji in risto3 or (suuji in risto1 and suuji in risto2):
    print(risto3[0])

