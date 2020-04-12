b = []
with open(r'/home/antonyi/Загрузки/petrol2.in', 'r') as f:
	b = f.readlines()

len_pet, d, d_on_petrol = [int(x) for x in b[0].split(' ')]
petrols = [int(x) for x in b[1].split(' ')]
# len_pet, d, d_on_petrol = (10, 100, 25)
# petrols = [13, 16, 21, 35, 38, 61, 67, 70, 77, 81]
it = 0
start_pos = 0
cnt_petrols = 0

while start_pos + d_on_petrol < d:
    
    if petrols[it] < start_pos + d_on_petrol:
        if it+1 < len(petrols):
            it += 1
            continue
    
    if petrols[it] > start_pos + d_on_petrol:
        it -= 1
    
    start_pos = petrols[it]
    cnt_petrols += 1

print(cnt_petrols)
    