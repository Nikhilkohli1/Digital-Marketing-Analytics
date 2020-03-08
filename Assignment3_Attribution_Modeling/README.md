# Attribution Modeling & Budget Optimization



CLAAT document link - https://docs.google.com/document/d/1BoSlam9Pp4LPUwb88HmeilAvCu6RH2-b8ECv4c8M0NM/edit#

CLAAT Preview Link - https://codelabs-preview.appspot.com/?file_id=1BoSlam9Pp4LPUwb88HmeilAvCu6RH2-b8ECv4c8M0NM#0


Description - 

We have to use the Criteo Attribution Bidding Dataset and build Attribution models to optimize the Budget 
Allocation for various Marketing campaigns. 

This dataset represents a sample of 30 days of Criteo live traffic data. Each line corresponds to one impression (a banner) that was displayed to a user. For each banner we have detailed information about the context, if it was clicked, if it led to a conversion and if it led to a conversion that was attributed to Criteo or not.

Timestamp: timestamp of the impression
UID: unique user identifier
Campaign: unique campaign identifier
Conversion: 1 if there was a conversion in the 30 days after the impression; 0 otherwise
Conversion ID: a unique identifier for each conversion
Click: 1 if the impression was clicked; 0 otherwise
Cost: the price paid for this ad
Cat1-Cat9: categorical features associated with the ad. These features' semantic meaning is not disclosed.

## Attribution Modeling 

Attribution modeling is a framework for analyzing which touchpoints, or marketing channels, receive credit for a conversion. Each attribution model distributes the value of a conversion across each touchpoint differently. A model comparison tool allows you to analyze how each model distributes the value of a conversion. There are six common attribution models: First Interaction, Last Interaction, Last Non-Direct Click, Linear, Time-Decay, and Position-Based.


![Attribution Modeling](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3_Attribution_Modeling/Panel%20Dashboard/images/theme.PNG)

By analyzing each attribution model, one can get a better idea of the ROI for each marketing channel/campaign.

![Models](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3_Attribution_Modeling/Panel%20Dashboard/images/Model%20Comaprision.JPG)


Types of Marketing Models we will be implementing- 

1. Single Touch Attribution Models:
- Last touch Attribution
- First Touch Attribution

2. Multi-Touch Attribution Models:
- UShape Attribution
- Time Decay Attribution
- Position Decay Attribution
- Reverse Decay: Position
- Linear Attribution
- Mode Attribution

3. Data Driven or Machine Learning Attribution:
- Logistic Regression
- LSTM (Long short term memory)
- LSTM with Attention mechanism
- Shapley and Game Theory
- Markov Chain

We have implemented 10 models to compare and see which works best for us and validate our claim using Simulation algorithm
to optimize the Budget Allocation using the history data to calculate Return on Investment. 

### Dashbaord -

We also create a Dashbaord using Panel to summarize our insights and model outcomes. 

![Dashboard1](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3_Attribution_Modeling/Panel%20Dashboard/Dash1.PNG)

![Dashboard2](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment3_Attribution_Modeling/Panel%20Dashboard/Dash2.PNG)


