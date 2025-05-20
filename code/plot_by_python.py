import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
# Create colors
primary = (24/255,97/255,153/255)
df = pd.read_stata("figures/auto.dta")
plt.scatter(df["weight"], df["mpg"], color=primary)
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.savefig("figures/plot_by_python.pdf")
plt.show()
