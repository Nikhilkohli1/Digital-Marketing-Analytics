# AdStock Marketing Mix Modeling 


CLAAT document link - https://docs.google.com/document/d/1BoSlam9Pp4LPUwb88HmeilAvCu6RH2-b8ECv4c8M0NM/edit#

CLAAT Preview Link - https://codelabs-preview.appspot.com/?file_id=1BoSlam9Pp4LPUwb88HmeilAvCu6RH2-b8ECv4c8M0NM#3


## Description - 

In this assignment, we are provided with a Generated Dataset to  analyse the Effects of Ad Spending on TV & Radio. And whether
or not these mediums have any AdStock Effects or not. 

We Explain few Concepts related to AdStock and Marketing Mix Modeling in the Assignment Notebook. 

Dataset consists of features like Sales, TVSales, TVRadio Sales, Adstock Values for 2 models and Period is in Weeks. 
We also have TV and Radio Spending o Advertisements for each week. 
We are also given a Temperature information which can be used to model seasonality. 

![MMM](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3/Images/Mark_mix.PNG)

## AdStock Effect

AdStock effect is the prolonged or lagged effect of advertising on consumer purchase behavior

Ad-stock quantifies build-up of awareness in the minds of the consumers. It accounts for exposure to advertising and the influence it has on purchase behavior. Each new exposure to an advertisement builds awareness and it will be higher if there have been recent exposures and lower if not. In the absence of further exposures adstock eventually deteriorates to negligible levels.
The key assumption made by the adstock model is that each given sales period retains a fraction of the previous stock of advertising.

## Adstock Components -

- Exposure to advertising today has effects on consumers’ purchasing decisions in the future (Carryover Effect)
- The effect of ad exposure on purchasing decisions decays with time (Carryover Effect)
- The effect of ad exposure on sales is subject to the law of diminishing returns (Shape Effect)
- Changing the level of ad exposure brings about a relative change in sales volumes (Shape Effect)
- We will discuss about two main components -

### Diminishing Returns -
This states that after the saturation level is reached, the impact of exposure to ads start diminishing over time.

### Carry Over Effect -
This is the impact of past advertisement on present sales. It is also called Decay effect as the impact of previous months advertisement decays over time.
	
let us denote the intensity of the channel activity measured in dollars spent or the number of messages in time period t as Xt, the business metric of interest, often the sales volume or revenue, as yt, and the current effect induced by the activity on the business metric as at. The effect variable at is called the adstock. The adstock model assumption can then be expressed as - 

		AdStock(time=t) = Xt + λ * (AdStock(time=t-1)

![Formula](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3/Images/Capture.PNG)


You can Run the Steps described below to View/Replicate the outcome of the tasks. 


1. This is the original Dataset file provided - 'Adstock_TV_Radio_Sales.csv'

2. Run the Jupyter notebook - 'Marketing_Mix_Model_AdStock_Analysis.ipynb' 

3. This notebook includes the Univariate Analysis and Multivariate Analysis. Then we model the Adstock effects using Marketing Mix Modeling 
 in 2 ways 
 	- Linear Regression using Ordinary Least Squares method
 	- Numerical Approximation Method
 
 
4. Use the output generated - 'MMM_Adstock_TV_Radio_Modeling.csv'
We uploaded this to salesforce Einstein Analytics and Created An App > Dataset > DataFlow > Dashboard 

![Dashboard](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3/DashBoard/Adstock.png)


You can generate your own insights as well based on your understanding of the data. 






