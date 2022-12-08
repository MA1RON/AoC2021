import numpy as np

with open('input_data.txt','r') as f:
    lines = f.readlines()
f.close()

def find_occ(lenline,lines,targetdigit):
    listocc0 = []
    listocc1 = []
    occ0 = np.zeros(lenline)
    occ1 = np.zeros(lenline)
    jj = 0
    for line in lines:
        flag0 = False
        flag1 = False
        for digit in range(lenline):
            if int(line[digit]) == 0:
                occ0[digit] += 1
                if targetdigit == digit:
                    flag0 = True
            else:
                occ1[digit] += 1
                if targetdigit == digit:
                    flag1 = True
        if flag0:
            listocc0.append(jj)
        if flag1:
            listocc1.append(jj)
        jj += 1
    return [occ0,occ1,listocc0,listocc1]

lenline = len(lines[:][0])-1 # take care of \n
# part 1
[occ0,occ1,_,_] = find_occ(lenline,lines,0)
gamma = 0
epsilon = 0
for digit in range(lenline):
    if occ0[digit] < occ1[digit]:
        gamma += 2**(lenline-1-digit)
    else:
        epsilon += 2**(lenline-1-digit)
        
print(f'PART 1:\nGamma={gamma}, Epsilon={epsilon}. Result={gamma*epsilon}.\n')

# part 2
print('PART 2:')
oxy = list(lines)
co2 = list(lines)
digit = 0
flag_oxy = False
flag_co2 = False
while digit in range(lenline):
    [occ0oxy,occ1oxy,listocc0oxy,listocc1oxy] = find_occ(lenline,oxy,digit)
    [occ0co2,occ1co2,listocc0co2,listocc1co2] = find_occ(lenline,co2,digit)
    if len(listocc0oxy) > len(listocc1oxy): # for this digit there are more 0
        oxy = list([oxy[i] for i in listocc0oxy])
    else: # for this digit there are more 1 or the same number of 0 and 1
        oxy = list([oxy[i] for i in listocc1oxy])
    if len(listocc0co2) > len(listocc1co2): # for this digit there are more 0
        co2 = list([co2[i] for i in listocc1co2])
    else: # for this digit there are more 1 or the same number of 0 and 1
        co2 = list([co2[i] for i in listocc0co2])
    digit += 1
    if not flag_oxy:
        print(f'Length of Oxy list={len(oxy)}.',end='\n')
    if not flag_co2:
        print(f'Length of CO2 list={len(co2)}.',end='\n')
    if len(oxy) == 1:
        print(f'Final result of Oxy = {oxy[0][:-1]}.')
        oxy_result = int(oxy[0],base=2)
        flag_oxy = True
    if len(co2) == 1:
        print(f'Final result of CO2 = {co2[0]}.')
        co2_result = int(co2[0],base=2)
        flag_co2 = True
        
print(f'Oxygen={oxy_result}, CO2={co2_result}. Result={oxy_result*co2_result}.\n')
