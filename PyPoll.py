import datetime as dt
now=dt.datetime.now()
print("the time righgt now is",now)

import csv
print(dir(csv))

#Read data from file:

file_to_load="Resources/election_results.csv"
election_data=open(file_to_load,'r')
election_data.close()

#with statement format READ

with open(file_to_load) as election_data:
    print(election_data)
    
#indirect path to file :

import os
dir(os)

file_to_load=os.path.join('Resources','election_results.csv')


import csv
import os
file_to_load=os.path.join("Resources","election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)
    
#WRITE FILES IN PYTHON:

# file_to_save=os.path.join("analysis","election_analysis.txt")
# open(file_to_save,"w")
    
# file_to_save=os.path.join("analysis","election_analysis.txt")
# outfile=open(file_to_save,"w")
# outfile.write('hello sworld')
# outfile.close()

#now wtih with statement WRITE:

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save,"w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")


#READ THE ELECTION RESULTS:

import csv
import os
files_to_load=os.path.join("Resources","election_results.csv")
files_to_save=os.path.join("analysis","election_analysis.txt")

total_votes=0

candidate_options=[]

candidate_votes={}

winning_candidate=""
winning_count=0
winning_percentage=0


with open(files_to_load) as election_data:
    #read the fil object with the reader function
    file_reader=csv.reader(election_data)
    
    #read the header row
    headers=next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
        total_votes+=1
        
    #print the candidate name from each row
        candidate_name=row[2]
    
    #add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            #begin tracking that candidate's vioite count
            candidate_votes[candidate_name]=0
            
            #add a vote to that candidates count
        candidate_votes[candidate_name]+=1
        
with open(file_to_save,"w") as txt_file:

    election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
    
    print(election_results, end="")
        # Save the final vote count to the text file.
    txt_file.write(election_results)
     
#print(candidate_votes)       
#GET TOTAL VOTES

    for candidate_name in candidate_votes:
        #retreive vote count of a candidate
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        #print(f"{candidate_name}: received {vote_percentage} of the vote")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        
        txt_file.write(candidate_results)
        
    #determine the winning candidate::

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            ## 2. If true then set winning_count = votes and winning_percent =
            # # vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    #print(winning_candidate_summary)