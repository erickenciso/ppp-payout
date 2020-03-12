#!/usr/bin/env python
# coding: utf-8

# In[14]:


winners = ([['Santi', 40]])
losers = ([['Bink',40],['TChan',20]])

l = []
for i in range(len(losers)):
    l.append(losers[i][1])
a = max(l)

for i in range(len(losers)):
    if losers[i][1] == a:
        bl = losers[i][0]

count = 0
done = False
# go through list of losers, change count to reflect index of curren winner being paid out
for i in range(len(losers)):
    #for each loser pay out debt until it reaches zero
    while losers[i][1]!=0 and done == False:
        #if last winner already paid break out of loop
        if count > (len(winners) - 1):
            done = True
        #if last winner paid out remaining balance will be rake, send to biggest loser    
        elif count == (len(winners) - 1) and losers[i][1]> winners[count][1]:
            print (losers[i][0] + ' pays ' + winners[count][0] + ' ' + str(round(winners[count][1],2)))
            losers[i][1] = losers[i][1] - winners[count][1]
            print (losers[i][0] + ' pays ' + str(round(losers[i][1],2)) + ' in rake to ' + bl)
            losers[i][1] = 0
            done = True
             
        #if losers remaining debt greater or equal to winners balance update loser debt and count
        elif losers[i][1] >= winners[count][1]:
            print (losers[i][0] + ' pays ' + winners[count][0] + ' ' + str(round(winners[count][1],2)))
            losers[i][1] = losers[i][1] - winners[count][1]
            
            winners[count][1] = 0
            count = count + 1
        #if loser debt smaller than winning players balance set debt to 0 and update winning players balance
        else:
            print (losers[i][0] + ' pays ' + winners[count][0] + ' ' + str(round(losers[i][1],2)))
            winners[count][1] = winners[count][1] - losers[i][1]
            losers[i][1] = 0
            
for i in range(len(losers)):
    if losers[i][1] != 0:
        print (losers[i][0] + ' pays ' + str(round(losers[i][1],2)) + ' in rake to ' + bl)


# In[ ]:




