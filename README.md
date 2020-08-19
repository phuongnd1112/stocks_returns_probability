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
