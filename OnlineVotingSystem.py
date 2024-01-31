# Online Voting System in Python

# Initialize party votes
party_votes = {
    "TDP": 0,
    "YCP": 0,
    "JANASENA": 0,
    "PRAJASANTHI": 0,
    "NOTA": 0
}

# Get the total number of voters from user input
total_voters = int(input("Enter the number of voters: "))
voter_count = 0

# Main loop for collecting votes from voters
while voter_count < total_voters:
    print(f"\nVoter {voter_count + 1}")

    # Get voter details
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Check eligibility based on age
    if age >= 18:
        print(f"Welcome, {name}! You are eligible to vote.")

        # Display available parties and get the voter's choice
        print("Available parties: 1. TDP, 2. YCP, 3. JANASENA, 4. PRAJASANTHI, 5. NOTA")
        party_choice = int(input("Enter the number of the party you want to vote for (or NOTA): "))

        # Process the vote based on the chosen party
        if 1 <= party_choice <= 5:
            party_name = list(party_votes.keys())[party_choice - 1]
            party_votes[party_name] += 1
            print(f"You voted for {party_name}.")
        else:
            print("Invalid choice.")

        print("Your vote has been recorded. Thank you for voting!")
        voter_count += 1
    else:
        print(f"Sorry, {name}. You are not eligible to vote. Please try again.")

# Display voting results
print("\nVoting Result:")
for party, votes in party_votes.items():
    print(f"{party} Votes: {votes}")

# Check for a clear winner or a tie
nota_votes = party_votes["NOTA"]
if nota_votes == total_voters:
    print("No party wins. NOTA received the majority of votes.")
else:
    max_votes = max(party_votes.values())
    winner = [party for party, votes in party_votes.items() if votes == max_votes][0]

    # Display the winner or declare a tie
    if winner == "TDP":
        print("Chandrababu Naidu is the new Chief Minister of Andhra Pradesh. Congratulations to him!")
    elif winner == "YCP":
        print("Jagan Mohan Reddy is the winner. Congratulations to him!")
    elif winner == "JANASENA":
        print("Pavan Kalyan is the new Chief Minister of Andhra Pradesh. Congratulations to him!")
    elif winner == "PRAJASANTHI":
        print("K.A.Paul is the new Chief Minister of Andhra Pradesh. Congratulations to him!")
    else:
        print("It's a tie or no clear winner.")
