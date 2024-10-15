import csv
from pprint import pprint

aiMemList = []
aiDict = {}
compList = []

# Get AI list
# GoMembership -> Club Reports -> Customer Reports -> Events -> club membership list for competitions
with open("Club Membership list - for competitions.csv", 'r', encoding='utf-8') as activeMembershipFile:
  csvreader = csv.reader(activeMembershipFile, delimiter=',')
  for row in csvreader:       # iterate over all rows in the csv file of active memberships
    aiMemList.append(row[1])        # make a list of all AI numbers with active memberships
    aiDict[row[0]] = row[2]         # make a list of all first names

# Get competition list
with open("DUCC24MagicalIANSEOSheet.csv", 'r', encoding='utf-8-sig') as competitionSignUpsFile:
  csvreader = csv.reader(competitionSignUpsFile, delimiter=',')
  for row in csvreader:        # iterate over all rows in the csv file of people who've signed up
    compList.append(row)              # add all the details

# Sort competitors by club
compList.sort(key = lambda x: x[13])

# Check if Competitor number is on AI list
invalidMem = []
for archer in compList[1:]:         # For each person signed up to the competition, skipping first row of headers
  if archer[0] not in aiMemList:      # check if their membership number is in AI's list of active memberships
    invalidMem.append(archer)           # if not, add them to t list of people without memberships
  elif not archer[0]:                 # OR, if they don't have a membership number at all
    invalidMem.append(archer)           # also add them to the list of people without memberships

# # Check if name is same when a membership is valid. For visual comparison (not updated)
# print("Comp" + "\t\t" + "AI")
# for archer in compList:
#   if archer[0] in aiDict.keys():
#     print(archer[1] + "\t\t" + aiDict[archer[0]])

# pprint(invalidMem)

# This will print out the archers who don't have active memberships and/or don't have AI numbers
for archer in invalidMem:
  print(archer[0] + "\t\t" + archer[11] + " " + archer[10] + ", " + archer[13])