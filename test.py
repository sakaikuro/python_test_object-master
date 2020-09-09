"""
このファイルに解答コードを書いてください
"""
with open('input.txt') as f:
    text = f.readlines()
    
m = int(text[-1].strip())
pair_ = text[:-1]    

i_, s_ = [], []
for i in range(len(pair_)):
    split = pair_[i].strip().split(':')
    i_.append(int(split[0]))
    s_.append(split[1])
    
dict_pair = dict(zip(i_, s_))
pair = sorted(dict_pair.items(), key=lambda x:x[0])

output = []
for i in range(len(pair)):
    if m % pair[i][0]==0:
        output.append(pair[i][1])

print(''.join(output)) if output else print(m)
