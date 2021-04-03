# Election-Analysis

## Overview
The purpose of the election audit was to determine the results at a county level along with the candidate level. The election commission wished to see where the largest shares of voters came from in addition to who they voted for.

## Election Audit Results

**Total Votes:** 

*369,711*

![alt text](https://github.com/CCoelho372/Election-Analysis/blob/main/Total%20Votes.png)

**Number of Votes and Percentage:**

*Jefferson: 10.5% (38,855)*

*Denver: 82.8% (306,055)*

*Arapahoe: 6.7% (24,801)*

![alt text](https://github.com/CCoelho372/Election-Analysis/blob/main/County%20Votes.png)

**County with the Largest Number of Votes:**
*Denver*

**Candidate Outcomes**

*Charles Casper Stockham: 23.0% (85,213)*

*Diana DeGette: 73.8% (272,892)*

*Raymon Anthony Doane: 3.1% (11,606)*

![alt text](https://github.com/CCoelho372/Election-Analysis/blob/main/Candidate%20Votes.png)

**Candidate Winner**
*Diana DeGette: 73.8% (272,892)*

**Overall Election Results**

![alt text](https://github.com/CCoelho372/Election-Analysis/blob/main/Overall%20Results.png)

## Election Audit Summary

This is a valuable coding tool to determine this elections results along with future elections as well. The code has been set up to establish how many votes for any number of candidates and from whichever county they voted from.   

Having code as seen below will add counties that may not have previously existed in a list. The same version of coding is used for candidates.

*if county_name not in county_names:*

*county_names.append(county_name)*

*county_votes[county_name] = 0*

*county_votes[county_name] +=1*

Even when determing the winner or counties with the largest turnout, it is based on the csv in its current format. As long as candidates remain in candidate_name = row[2] and county_name = row[1] results will continue to be seen with this coding. 
