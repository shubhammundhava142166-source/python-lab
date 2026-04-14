c=[];n=[]
for _ in range(int(input())):
 c.append(input());n.append(int(input()))
import matplotlib.pyplot as plt
plt.pie(n,labels=c);plt.show()