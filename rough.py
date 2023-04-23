import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Read the CSV file into a Pandas dataframe

df = pd.read_csv('cpt_trial6.csv')
#df1 = pd.read_csv('cpt_data_ss.csv')




# DATAFRAMES -----------------------------------------------------------------------------------------------------------------------------------------------
#df1 = pd.read_csv('cpt_data_corr_(L=1000, tf=2000000 , ts=1200000, R=1).csv')
#df2 = pd.read_csv('cpt_data_corr_(L=800, tf=1000000 , ts=700000, R=1).csv')
#df3 = pd.read_csv('cpt_data_corr_(L=600, tf=800000 , ts=400000, R=1).csv')
#df4 = pd.read_csv('cpt_data_corr_(L=400, tf=600000 , ts=200000, R=1).csv')
#df5 = pd.read_csv('cpt_data_corr_(L=200, tf=60000 , ts=40000, R=1).csv')
#df6 = pd.read_csv('cpt_data_corr_(L=100, tf=500000 , ts=100000, R=1).csv')
#df7 = pd.read_csv('cpt_data_corr_(L=50, tf=50000 , ts=10000, R=1).csv')


# MAKING DATA TYPE TO FLOAT  -------------------------------------------------------------------------------------------------------------------------------------

#df['m'] = df['m'].astype(float)
#df['P(m)'] = df['P(m)'].astype(float)
#df['exp_m'] = df['exp_m'].astype(float)

#df['ρ'] = df['ρ'].astype(float)
#df['σ²-Model'] = df['σ²-Model'].astype(float)

#df1['r'] = df1['r'].astype(float)
#df1['Cij'] = df1['Cij'].astype(float)

#df2['r'] = df2['r'].astype(float)
#df2['Cij'] = df2['Cij'].astype(float)

#df3['r'] = df3['r'].astype(float)
#df3['Cij'] = df3['Cij'].astype(float)

#df4['r'] = df4['r'].astype(float)
#df4['Cij'] = df4['Cij'].astype(float)

#df5['r'] = df5['r'].astype(float)
#df5['Cij'] = df5['Cij'].astype(float)

#df6['r'] = df6['r'].astype(float)
#df6['Cij'] = df6['Cij'].astype(float)

#df7['r'] = df7['r'].astype(float)
#df7['Cij'] = df7['Cij'].astype(float)

# DEFINING NEW DATAFRAME FOR ONLY POSITIVE POINTS   ------------------------------------------------------------------------------------------------------------

#df = df[0:28]

#d1 = df1[0:int(len(df1) * 0.5)]
#d2 = df2[0:int(len(df2) * 0.5)]
#d3 = df3[0:int(len(df3) * 0.5)]
#d4 = df4[0:int(len(df4) * 0.5)]
#d5 = df5[0:int(len(df5) * 0.5)]
#d6 = df6[0:int(len(df6) * 0.5)]
#d7 = df7[0:int(len(df7) * 0.5)]

# PLOTTING STRAIGHT LINE -------------------------------------------------------------------------------------------------------------------------------


#plt.loglog(0.732-df_filtered['ρ'], df_filtered['σ²-Model'], label = 'L=1024, tf = 12000000, ts = 6000000', linewidth = 0.75)
plt.loglog(0.732-df['ρ'], df['σ²-Model'], label = 'σ²-Model', linewidth = 0.75)
#plt.loglog(0.732-df['ρ'], df['σ²-Analytical'], label = 'σ²-Analytical', linewidth = 0.75)



#plt.plot(0.732-d['ρ'], (d['exp_rhoc']**8)*2.2, label = 'exp(ρc - ρ)', linewidth = 0.75 )
#plt.plot(0.732-d['ρ'], d['σ²-Analytical'], label = 'σ²-Model vs ρ, L = 100', linewidth = 0.75 )


# PLOTTING MASS DISTRIBUTION
#plt.loglog(df['m'], df['P(m)'], label = 'Probability Mass Distribution, Rho = 0.2', linewidth = 0.75)
#plt.loglog(df['m'], (df['m']**(-5/2))*df['exp_m1']*0.2, label = 'm**(-5/2), a = -.1742', linewidth = 0.75)
#plt.loglog(df['m'], (df['m']**(-5/2))*df['exp_m2']*0.2, label = 'a = -.19', linewidth = 0.75)


# PLOTTING SCATTER PLOT -----------------------------------------------------------------------------------------------------------------------------------------------
#plt.scatter(0.732-df_filtered['ρ'], df_filtered['σ²-Model'], s=8)
plt.scatter(0.732-df['ρ'], df['σ²-Model'], s=8)
#plt.scatter(0.732-df['ρ'], df['σ²-Analytical'], s=8)


#plt.plot(0.732-df['ρ'], (0.732-df['ρ'])**(-0.4)*5, label = '|ρc - ρ|ᵃ', linewidth = 0.75, color = 'r' )


#plt.scatter(0.732-d['ρ'], (d['exp_rhoc']**8)*2.2, s=10)
#plt.scatter(d['ρ'], d['σ²-Analytical'], s=8)

# PLOTTING MASS DISTRIBUTION SCATTER PLOT
#plt.scatter(df['m'], df['P(m)'], s=10)

# PLOTTING CORRELATION POINTS  -----------------------------------------------------------------------------------------------------------------------------

#plt.plot(d1['r']/1000, d1['Cij']*1000, label = 'Cij, L = 1000', linewidth = 0.75 )
#plt.plot(d2['r']/800, d2['Cij']*800, label = 'Cij, L = 800', linewidth = 0.75 )
#plt.plot(d3['r']/600, d3['Cij']*600, label = 'Cij, L = 600', linewidth = 0.75 )
#plt.plot(d4['r']/400, d4['Cij']*400, label = 'Cij, L = 400', linewidth = 0.75 )
#plt.plot(d5['r']/200, d5['Cij']*200, label = 'Cij, L = 200', linewidth = 0.75 )
#plt.plot(d6['r']/100, d6['Cij']*100, label = 'Cij, L = 100', linewidth = 0.75 )
#plt.plot(d7['r']/50, d7['Cij']*50, label = 'Cij, L = 50', linewidth = 0.75 )



# FITTING A LINE ----------------------------------------------------------------------------
#x = 0.732-df['ρ']
#y = df['σ²-Model']

#m, b = np.polyfit(x, np.log10(y), 1)
#plt.loglog(x, 10**(m*x + b), label='linear fit')



#-------------------------------------------------------------------------------------------
#plt.scatter(d1['r']/1000, d1['Cij']*1000, s=8)
#plt.scatter(d2['r']/800, d2['Cij']*800, s=8)
#plt.scatter(d3['r']/600, d3['Cij']*600, s=8)
#plt.scatter(d4['r']/400, d4['Cij']*400, s=8)
#plt.scatter(d5['r']/200, d5['Cij']*200, s=8)
#plt.scatter(d6['r']/100, d6['Cij']*100, s=8)
#plt.scatter(d7['r']/50, d7['Cij']*50, s=8)


#plt.xlabel('m', fontsize = 10)
#plt.ylabel('P(m)')
#plt.title('P(m) vs m, Rho = 0.2')

plt.xlabel('ρ', fontsize = 20)
plt.ylabel('σ²', fontsize = 20)
plt.title('σ² vs ρ (LogLog Scale),  L = 100, tf = 600000, ts = 300000, R = 100', fontsize = 15)

#plt.xlim(left=1)
plt.legend()
plt.show() 


#cpt_trial2 had slop  = -0.4



