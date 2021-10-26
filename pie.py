from matplotlib import pyplot as plt

plt.style.use("seaborn")


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
colors = ["#D5BFBF","#316B83","#6D8299","#8CA1A5","#161E54"]
explodes = [0,0,0,0.1,0]
plt.pie(slices,labels = labels, autopct= '%1.1f%%', explode = explodes, startangle=90, shadow = True, colors = colors, wedgeprops={"edgecolor" : "black"})


plt.title("Pie Chart")
plt.tight_layout()
plt.show()