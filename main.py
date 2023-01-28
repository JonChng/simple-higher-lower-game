from art import logo, vs
from game_data import data
import random
from replit import clear

ok = True

win_count = 0

while ok:
  

  print(logo)
  if win_count > 0:
    print(f"You're right! Current score: {win_count}")

  a = random.randint(0,len(data) + 1)
  b = random.randint(0,len(data) + 1)

  data_a = data[a]
  data_b = data[b]

  print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")

  print(vs)

  print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")

  ans = max(data_a["follower_count"], data_b["follower_count"])

  guess = input("Who has more followers? 'A' or 'B': ")

  if guess.upper() == "A" and data_a["follower_count"] == ans:
    win_count += 1
    clear()

  elif guess.upper() == "B" and data_b["follower_count"] == ans:
    win_count += 1
    clear()

  else:
    clear()
    print(logo)
    print(f"Sorry, that is wrong. Final score {win_count}.")
    break
    
  
    

  



  