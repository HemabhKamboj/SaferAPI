# Safer
Better safe than sorry!

We will address the issue of safety in our project named ‘Safer’.

The national capital of India, Delhi has got the dubious distinction of topping the list in cases of murder, kidnapping and abduction, juveniles in conflict and economic offences. Delhi reported 33% (13,803 cases out of total 41,761 cases in 19 cities) of total crimes against women, followed by Mumbai at 12.3% (5,128 cases) last year among the 19 cities with population above two million.

## How we try to solve the problem?

MapMyIndia tries to find the fastest route between two paths even if it may mean compromising on security.
Our app aims at detecting the safest route by finding danger index of all possible paths between two places which is a weighted sum of numeric values our unsupervised machine learning algorithm devised and assigned to 166 places in Delhi .
We hope to extend that by including more detailed and transparent data which is not currently available.


## Technical concept used:

We have applied Unsupervised Machine Learning Algorithm to find danger index of multiple routes between two places.

We have used a Clusterring algorithm : K-Means , to rate criminal activities of 166 places on the map of Delhi in range of 0 to 5.
K-means clustering is a type of unsupervised learning, which is used when you have unlabeled data (i.e., data without defined categories or groups). The goal of this algorithm is to find groups in the data, with the number of groups represented by the variable K. The algorithm works iteratively to assign each data point to one of K groups based on the features that are provided. Data points are clustered based on feature similarity. The results of the K-means clustering algorithm are:
1.The centroids of the K clusters, which can be used to label new data
2.Labels for the training data (each data point is assigned to a single cluster)

## Displaying maps:

We used MapMyIndia API to display all possible routes between any two location along with danger index of that route. This leads to displaying routes with markers indicating danger level of a place that falls on that route. The data below the map shows relevant statistics like time durations , distance and safety index of all possible routes between two places entered. This would enable user to make smart decisions while choosing any route.

## Result of training the model:

The k-means algorithm assigns 0-5 values to 166 locations in Delhi. An index of 0 indicates that the place is relatively safe with less crime rates in past while an index of 5 means that the place has high crime records in the past.
We used various legends to display safety index of various locations in Delhi.

