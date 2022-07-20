import os 

print('''
              ▓▓▒▒                  
              ▓▓▓▓██                
            ░░▓▓██▓▓                
          ░░▒▒▓▓▒▒▓▓                
          ██▓▓▒▒▒▒▒▒                
        ▓▓▓▓████    ██              
          ▒▒██░░      ▒▒▓▓░░        
  ▒▒▓▓██▓▓██▓▓▓▓██▓▓▓▓    ▓▓▓▓      
  ▓▓▓▓████████████████        ██▓▓  
  ░░░░░░░░░░░░░░░░░░░░        ░░░░  
''')
print("Welcomde to the secret auction program.")

bids = {}
auction = True
values = []

def find_highest_bidder(bidding_record):
  for bidder in bidding_record:
    values.append(bidding_record[bidder])
  
  max = 0
  for val in values:
    if(val > max):
      max = val

  print(max)

while auction:
  bidder_name = input("What is your name?: ")
  amount_bid = int(input("What's your bid?: $"))
  bids[bidder_name] = amount_bid
  decision = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if(decision == "no"):
    auction = False
    os.system('cls')
    find_highest_bidder(bids)
    #print(bids)
  elif(decision == "yes"):
    os.system('cls')
  else:
    os.system('cls')
    print("Error... Try Again...")
    decision = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()