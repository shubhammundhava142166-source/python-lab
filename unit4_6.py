a=[int(input()) for _ in range(50)]
import matplotlib.pyplot as plt
plt.hist(a,bins=[0,10,20,30,40,50,60,120]);plt.show()