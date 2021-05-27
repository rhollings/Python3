#guess the output before printing

w1 = "step"
w2 = "on"
w3 = w1 + " " + w2
w4 = w3 + " " + w3[len(w3)::-1]
w5 = "." * 3
w6 = w4 + w5
w7 = ''.join(list(i for i in w6[:-2]))

print(w7)
