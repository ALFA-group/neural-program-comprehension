jibun, kimi, kanojyo = 5, 3, 2

if (kimi < jibun and jibun < kanojyo):
    print(jibun)

elif (kanojyo < jibun and jibun < kimi):
    print(jibun)

elif (kanojyo < kimi and kimi < jibun):
    print(kimi)

elif (jibun < kimi and kimi < kanojyo):
    print(kimi)

else:
    print(kanjyo)

