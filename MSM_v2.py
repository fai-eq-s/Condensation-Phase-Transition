import pandas as pd
import matplotlib.pyplot as plt

# Load the data sets from CSV files
df5 = pd.read_csv('rho.csv')
df1 = pd.read_csv('rhosq.csv')
#df2 = pd.read_csv('MSM_v5.1.csv')
#df3 = pd.read_csv('MSM_v5.2.csv')
df4 = pd.read_csv('MSM_v5.3.csv')
#df6 = pd.read_csv('MSM_v1.3.csv')



# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the data sets on the same axis
ax.plot(df5['Rho'], df1['Rho'], label='ρ', linewidth = 0.5, marker='o', markersize=3, markerfacecolor='red')
ax.plot(df1['Rho'], df1['Rho Sq'], label='ρ²', linewidth = 0.5, marker='o', markersize=3, markerfacecolor='red')
#ax.plot(df2['RHO'], df2['SIGMA SQUARED'], label='R = 1',  linewidth = 0.5, marker='o', markersize=3, markerfacecolor='red')
#ax.plot(df3['RHO'], df3['SIGMA SQUARED'], label='R = 10',  linewidth = 0.5, marker='o', markersize=3, markerfacecolor='red')
ax.plot(df4['RHO'], df4['SIGMA SQUARED'], label='R = 100', linewidth = 0.5, marker='o', markersize=3, markerfacecolor='red')


# Add a title and axis labels
ax.set_title('Subsystem Site: Rho, Rho Sq, Sigma Sq v/s Rho', fontsize = 10, fontname = 'times new roman')
ax.set_xlabel('ρ  $\longrightarrow$', fontsize = 10, fontname = 'times new roman')
ax.set_ylabel('σ² and ρ² $\longrightarrow$', fontsize = 10, fontname = 'times new roman')

# Set the x-axis and y-axis scales to log
#ax.set_xscale('log')
#ax.set_yscale('log')

# Set font size of tick labels on x and y axis
font_size = 7
plt.xticks(fontsize=font_size)
plt.yticks(fontsize=font_size)

# Add a legend with font size and font family
font_size = 7
font_family = 'serif'
plt.legend(prop={'size': font_size, 'family': font_family})
#plt.plot(df1['Rho'], df1['Sigma Square'], marker='o', markersize=0.1, markerfacecolor='red')


# Show the plot
plt.show()
