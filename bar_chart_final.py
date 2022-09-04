import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [32,28,33,29,27]
z = [34,26,34,31,28]
plt.bar(x,y,color='b',width=0.3)
x = [1.3,2.3,3.3,4.3,5.3]
plt.bar(x,z,color='b',width=0.3)
plt.xlabel("City")
plt.ylabel("Tempreature")
plt.show()