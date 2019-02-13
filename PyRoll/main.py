import os
import csv
import collections

electiondata = os.path.join("./Resources/election_data.csv")


#open and read the csv file and calculate total of votes
with open(electiondata, "r", newline="") as votingdata:
    reader_file = csv.reader(votingdata, delimiter=',')
    value = len(list(reader_file))
    #count the rows in the csv file
    value -= 1
    row_count = 0
    for row in reader_file:
        value.append(row[0])
        row_count += 1


#this script will give me the count of votes per candidate, plus the vote percentage
votecount = collections.Counter()
with open(electiondata) as votingdata:
    for row in csv.reader(votingdata, delimiter=","):
        votecount[row[2]] += 1
        kh = (round(votecount["Khan"] / (value)*100))
        cor = (round(votecount["Correy"] / (value)*100))
        li = (round(votecount["Li"] / (value)*100))
        ot = (round(votecount["O'Tooley"] / (value)*100))
        win = ("Khan")


#Print the results below this line
# Display summary header
print("\nElection Results", "\n-------------------------------------------" + "\n")
# Display Total votes    
print("Total Votes:" + " " + str(value) + "\n")    
print("-------------------------------------------" + "\n")
# Display Khan's vote summary           
print("Khan: " + str(kh) + "%" + "  (" + str(votecount["Khan"]) + ")" + "\n")
# Display Correy's vote summary 
print("Correy: " + str(cor) + "%" + "  (" + str(votecount["Correy"]) + ")" + "\n")
# Display Li's vote summary 
print("Li: " + str(li) + "%" + "  (" + str(votecount["Li"]) + ")" + "\n")
# Display O'Tooley's vote summary 
print("O'Tooley: " + str(ot) + "%" + "  (" + str(votecount["O'Tooley"]) + ")" + "\n")
# Display winner's name
print("-------------------------------------------" + "\n")
print("Winner: " + str(win))
print("-------------------------------------------" + "\n")


#Export a text file with the results
file = open("./Resources/mypyroll.txt", "w")
file.write("\nElection Results"  + "\n")
file.write("\n--------------------------------------------" + "\n")
file.write("Total Votes:" + str(value)  + "\n")
file.write("\n--------------------------------------------" + "\n")
file.write("Khan: " + str(kh) + "%" + "  (" + str(votecount["Khan"]) + ")"  + "\n")
file.write("Correy: " + str(cor) + "%" + "  (" + str(votecount["Correy"]) + ")"  + "\n")
file.write("Li: " + str(li) + "%" + "  (" + str(votecount["Li"]) + ")" + "\n")
file.write("O'Tooley: " + str(ot) + "%" + "  (" + str(votecount["O'Tooley"]) + ")"  + "\n")
file.write("\n-------------------------------------------" + "\n")
file.write("Winner: " + str(win)  + "\n")
file.write("\n-------------------------------------------" + "\n")

file.close() 