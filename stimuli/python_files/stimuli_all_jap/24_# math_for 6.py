kazu = [3, 7, 0, 1, 2, 2]
shin_kazu = 1

for ex in range(1, len(kazu), 2):
    shin_kazu *= kazu[ex]

print(shin_kazu)

