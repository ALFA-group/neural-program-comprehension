predicted = 13
actual = 11
error = 2

if (predicted - actual < error) or (predicted - actual > -1*error):
    print(predicted - actual + error)
else:
    print(predicted - actual - error)

