# STOCKS RETURNS AND MOVING AVERAGES FROM INVESTING.COM DATA 
PLEASE READ BEFORE BEGINNING. 
This script provides a quick tool to aid with analysing and visualising stocks returns. Functionalities: 
- Graphing moving averages 
- Graphing log returns data and normally distributed values 
- Calculate probability of % loss and gain 
- Calculate Values at Risk (VaR) at set confidence intervals 

## Install Packages 
Install all packages used in the script before running by pasting either one of the following into the command line: 
- ```pip3 install pandas numpy matplotlib seaborn scipy.stats datetime``` 
- ```pip install pandas numpy matplotlib seaborn scipy.stats datetime``` 

Why each lib: 
1. **pandas**: data manipulation tools 
2. **numpy**: convenient maths and randomisation 
3. **matplotlib**: plotting and visualisation 
4. **seaborn**: makes visualisation looks better 
5. **scipy.stats**: statistics (esp. distributions statistics) 
6. **datetime**: added functionality 

## Notes on Data 
The data was written specifically to parse and analyse data taken from [Investing.com](https://www.investing.com/). Note, **English** version only. It might not worth with other CSV files which has a different format. 

To download historical data from Investing.com: 
1. Look up ticker 
2. Click on 'historical data' 
3. Select desired period (recommended more than 9 months) 
4. Click download 

## Running CSV Files through Script 
When ran, the terminal will ask for the path of the file with the following input:<br> 
```What is your file path:``` <br> 
Insert the path for the CSV file. 
<br> 
<br> 
Next, the terminal will ask for a location to save charts/figures with the following input:<br> 
```Where do you want your graphs saved to:``` <br> 
Insert your desired location's path. 

## Results 
All results from the probability calculations and VaR calculations will be printed on the terminal.  
Working on Excel export. 

##Intepreting Results 
####Gain and Losses Figures 
Because we are working with **cummulative density function**, these percentages should be read as "at least x% gain/loss". 
* Sample intepretation: There is a 35% probability that there will be at least a 1% loss in stock XYZ day by day. 
* Sample intepretation: There is a 11% proability that there will be at least a 3% gain in stock XYZ QoQ. 

1. Daily 
I set the percentages of daily gain/loss at 1, 3, 5 and 7%. These numbers were chosen because they provide realistic insights into **daily** % change; trials and runs proved than any percentages larger than 10 will result unmeaningful results. 

2. Quarter and Yearly 
I set the percentages of daily gain/loss at 5, 10, 15 and 20%. These numbers were chosen because they provide realistic insights into **quarterly and yearly** % change. 

####Confidence Interval 
The confidence interval shows how likely the returns will be within a certain range of % loss and gain. 
The intervals chosen are the 90thth and 95th confidence interval. 
* Sample interpretation: We are 99% confident that stock XYZ won't make a loss more than 0.4% and a gain of more than 0.1% daily. 
* Sample interpretation: We are 95% confident that stock XYZ won't make a loss more than 13% and a gain of more than 25% daily. 




