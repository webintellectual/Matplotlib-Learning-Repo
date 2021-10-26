from matplotlib import pyplot as plt
from matplotlib import style

# style.use("seaborn-dark")
# print(style.available)
plt.xkcd()

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,"g",label ="line one", linewidth = 5)
plt.plot(x2,y2,"c",label = "line two", linewidth = 5)

plt.title("Styled Info")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()

plt.grid(True,color = "k")

plt.show()