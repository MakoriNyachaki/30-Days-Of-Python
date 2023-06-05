countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

fin, sw, nor, *rest = countries

print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']

colors = ['Red', 'Brown', 'Purple', 'Yellow', 'Lilac', 'Silver', 'Blue', 'Green']

R, Br, P, Y, *rest = colors

print (R, Br, rest, Y, P)

colors = colors
Q,K, *rest = colors

print(K, rest, Q)
