s = input('Please input a string: ').split()
s_unique = set(s)
dict_s = {}
for i in s_unique:
    dict_s[i] = s.count(i)
print(dict_s)