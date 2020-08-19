#TEMPLATE FOR RETURNS ANALYSIS WITH STOCKS DATA PULLED FROM INVESTING.COM 
#PLEASE READ DOCUMENTATION BEFORE RUNNING SCRIPT 

#pip3 install pandas numpy matplotlib seaborn scipy.stats 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 
import seaborn as sns 
from scipy.stats import norm 
from datetime import datetime 

#BEFORE STARTING 

# ----------- GETTING USER PATH TO FILE & FOLDER LOCATION 
file_path = input('What is your file path: ')
figure_save = input('Where do you want your graphs saved to: ')

# ----------- function IMPORT AND CLEAN DATA 
df = pd.read_csv(str(file_path), index_col = 'Date', parse_dates = True, thousands = ',') #read csv file, index Date, remove , from numerics 
df = df.drop(pd.to_datetime(datetime.date(datetime.now()))) #because the file will contain today's date, drop not useful data 
df = df.drop(['Vol.', 'Change %', 'High', 'Low'], axis = 1) #drop unused columns 


# ----------- CALCULATE RETURNS AND % RETURNS 
df['Price_1'] = df['Price'].shift(-1) #shift price 
df['Daily Returns'] = df['Price_1'] - df['Price'] #calculate daily returns 
df = df.dropna() #because the first value (descending) will have NaN for return, drop to avoid error when graphing 
df['%Returns'] = df['Daily Returns']/df['Price_1'] * 100 #percentage returns 

# ----------- MOVING AVERAGE AS A BUYING STRATEGY 
df['MA5'] = df['Price'].rolling('5d').mean() #ma5 calculation
df['MA10'] = df['Price'].rolling('10d').mean() #ma10 calculation
df['MA20'] = df['Price'].rolling('20d').mean() #ma20 calculation
df['MA50'] = df['Price'].rolling('50d').mean() #ma50 calculation 
df['MA100'] = df['Price'].rolling('100d').mean() #ma100 calculation 
df['MA200'] = df['Price'].rolling('200d').mean() #ma200 calculation 

#buy signal if MA10 exceed MA50, this will index 1/0 whether to buy or not   
#df['BuySig'] = [1 if df.loc[i, 'MA10'] > df.loc[i, 'MA50'] else 0 for i in df.index] #creating an easy to read buy signal based on MA's comparison 

#graphing moving averages - saved to the location that user indicated from the beginning
sns.set() 
plt.figure(figsize = [10,10])
plt.plot(df['MA5'], color='b')
plt.plot(df['MA10'], color='g') 
plt.plot(df['MA20'], color='r') 
plt.plot(df['MA50'], color='c') 
plt.plot(df['MA100'], color='m') 
plt.plot(df['MA200'], color='y') 
plt.xlabel('Time') 
plt.ylabel('Price') 
plt.title('Moving Averages') 
p0 = mpatches.Patch(color='b', label='MA5') 
p1 = mpatches.Patch(color='g', label='MA10') 
p2 = mpatches.Patch(color='r', label='MA20') 
p3 = mpatches.Patch(color='c', label='MA50') 
p4 = mpatches.Patch(color='m', label='MA100') 
p5 = mpatches.Patch(color='y', label='MA200') 
plt.legend(handles = [p0, p1, p2, p3, p4, p5])
plt.savefig(str(figure_save)+'/MA')

# ----------- LOG RETURNS AND DISTRIBUTION OF RETURNS 
df['LogReturns'] = np.log(df['Price_1']) - np.log(df['Price']) #take the log return 

mu = df['LogReturns'].mean() #finding a log mean 
sigma = df['LogReturns'].std(ddof=1) #finding a log std (ddof=1) because it relies on one other variables 

# ----------- NORMALISATION  
pdf = pd.DataFrame() #empty dataFrame to store important variables 
pdf['x'] = np.arange(df['LogReturns'].min()-0.01, df['LogReturns'].max()+0.01, 0.001) #generating a range 'x', normal curve 
pdf['pdf'] = norm.pdf(pdf['x'], mu, sigma)  #using PDF function from norm to generate a normal curve, based on mu and sigma from data 

#graphing distribution 
sns.set()
plt.figure(figsize=[10,10]) 
df['LogReturns'].hist(bins=20) #log returns data 
plt.plot(pdf['x'],pdf['pdf'], color='red') #normal curve 
plt.savefig(str(figure_save)+'/LogReturns')

# ----------- LIKELIHOOD FOR % OF RETURNS 

loss_daily = [-1, -3, -5, -7] #percentages loss list - small because daily fluctuations = small 
gain_daily = [1, 3, 5, 7] #percentages gain list 

##DAILY CALCULATION 
def likelihoodDaily(lst): #this function returns the likelihood of losing/gaining x% 
    likelihood = pd.DataFrame()
    likelihood['Loss/Gain Daily'] = lst 
    likelihood = likelihood.set_index('Loss/Gain Daily')
    values_list = [] 
    for i in lst: 
        value = norm.cdf((i/100), mu, sigma) 
        values_list.append(value) 
    likelihood['%'] = values_list  
    print(likelihood)

likelihoodDaily(loss_daily) #call function on loss list 
likelihoodDaily(gain_daily) #call function on gain list 

##YEARLY (the multiple will change depending on entires; 1Y data has 220 entries, 272 entries) 
mu272 = mu * 272 
sigma272 = (272**0.5) * sigma 

loss_yearly = [-5, -10, -15, -20] #percentages loss list - larger because yearly fluctuations = larger 
gain_yearly = [5, 10, 15, 20] #percentages gain list

def likelihoodYearly(lst): #this function returns the likelihood of losing/gaining x% 
    likelihood = pd.DataFrame() 
    likelihood['Loss/Gain Yearly'] = lst
    likelihood = likelihood.set_index('Loss/Gain Yearly')
    values_list = [] 
    for i in lst: 
        value = norm.cdf((i/100), mu272, sigma272) 
        values_list.append(value) 
    likelihood['%'] = values_list  
    print(likelihood) 

likelihoodYearly(loss_yearly) #calling function on loss % 
likelihoodYearly(gain_yearly) #calling function on gain %

# ----------- VALUES AT RISK AND BUYING STRATEGIES - Confidence Interval that Investment will return a gain/loss 
quantiles = [1, 5, 95, 99] #the 95th and 99th are usually the most important 
#1 and 5 are for losses (left-tail) 
#95 and 99 are for gains (right-tail)

def findVaRDaily(lst): #this function returns VaR for implied quantiles 
    var = pd.DataFrame() 
    var['Confidence Interval'] = quantiles 
    var = var.set_index('Confidence Interval') 
    VaR = [] 
    for i in lst: 
        value = norm.ppf((i/100), mu, sigma)
        VaR.append(value) 
    var['Loss/Gain Daily'] = VaR 
    print(var)  

findVaRDaily(quantiles) #calling function on VaR 

def findVaRYearly(lst): #this function returns VaR for implied quantiles 
    var = pd.DataFrame() 
    var['Confidence Interval'] = quantiles 
    var = var.set_index('Confidence Interval') 
    VaR = [] 
    for i in lst: 
        value = norm.ppf((i/100), mu272, sigma272)
        VaR.append(value) 
    var['Loss/Gain Yearly'] = VaR 
    print(var)  

findVaRYearly(quantiles) #calling function on VaR 