# Election-Analysis
## Overview of Election Audit: 
### Explain the purpose of this election audit analysis.
The purpose of this election audit analysis is to evalulate of the outcome from the election data using python script to sum up the election result based on candidate and to identify the largest votes county in this election.

## Election-Audit Results: 
#### How many votes were cast in this congressional election?
Total of 369,711 votes were cast in this congressional election.

#### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- The number of votes and the percentage of total votes for each county:

  Jefferson: 10.5% (38,855)
  
  Denver: 82.8% (306,055)
  
  Arapahoe: 6.7% (24,801)

#### Which county had the largest number of votes?
- Denver had the largest number of votes

#### Breakdown of the number of votes and the percentage of the total votes each candidate received.

  Charles Casper Stockham: 23.0% (85,213)
  
  Diana DeGette: 73.8% (272,892)
  
  Raymon Anthony Doane: 3.1% (11,606)

#### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  Diana DeGette won the election with 272,892 of total counts, which was 73.8% of total votes.

## Election-Audit Summary: 
### In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This code can be used for other elections with modification of the row number and file name.
With the modification of row number, the commission can run the audit for any vote result with the same information including Ballot ID, County and voted candidate name by changing the row number to match the county info or the candidate name.  
'Get the candidate name from each row.
    candidate_name = row[2]

' Extract the county name from each row.
    county_name = row[1]

With the modification of the file name, the commision can run the audit for different file name. For example, the result my by stored in different region name. The commision can simply change the file name to load the data into analysis. 
'file_to_load = os.path.join("Resources","election_results.csv")

In addition, the commision can export the analysis into different file name by changing the code.
'ile_to_save = os.path.join("analysis", "election_results.txt")


