import winsound

c = 261
d = 293
e = 329
f = 349
g = 392
a = 440
b = 493

note = [261, 293, 329, 349, 392, 440, 493]


t = 300
for i in note:
	winsound.Beep(i,t)