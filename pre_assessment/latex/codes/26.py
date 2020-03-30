h, m = 100, 200
h_deg, m_deg = h//2, m//3
# In Python3, // rounds down to the nearest whole number
angle = abs(h_deg - m_deg)

if angle > 180:
    angle = 360 - angle

print(int(angle))
