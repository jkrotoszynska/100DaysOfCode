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

def find_highest_bidder(bidding_record):
  max = 0
  for bidder in bidding_record:
    bid = (bidding_record[bidder])
    if(bid > max):
      max = bid
      bidder_max = bidder
    
  print(f"The winner is {bidder_max} with a bid of ${max}")

while auction:
  bidder_name = input("What is your name?: ")
  amount_bid = int(input("What's your bid?: $"))
  bids[bidder_name] = amount_bid
  decision = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if(decision == "no"):
    auction = False
    os.system('cls')
    find_highest_bidder(bids)
  elif(decision == "yes"):
    os.system('cls')
  else:
    os.system('cls')
    print("Error... Try Again...")