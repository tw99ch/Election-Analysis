county = ["Arapahoe","Denver","Jefferson"]

county_dict = str
county=str

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)100
