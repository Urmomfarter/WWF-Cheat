from From_Letters import *

hand = "abcdefg"
row = "...3456..."

spaces = []
for i in range(len(row)):
    if row[i] == ".":
        spaces.append(i)
maxLen = len(spaces)

for i in range(maxLen): #row start
    for j in range(i+1, maxLen): #row end
        print(str(i) + "\t" + str(j))
        rep_len = (j+1)-i
        substr = hand[i:j+1] #works
        
        for i2 in range(rep_len, maxLen - rep_len): #hand start
            low = i2
            high = i2 + rep_len
            tst_row = list(row)
            for k in range(rep_len):
                tst_row[spaces[i2]] = hand
            #print(substr + "\t" + ''.join(map(str,tst_row)))


#for i in range(int((Len**2 + Len) / 2)):
#    print(i)
    
