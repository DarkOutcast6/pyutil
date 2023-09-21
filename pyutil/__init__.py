import math
import random

# Random Number
def randNum(start=0,end=10):
  return random.randint(start,end)

def remove(text,remove=[],amount=math.inf):
  if amount == math.inf:
    if len(remove) == 1:
      remove = remove[0]
      return text.replace(remove,"")
    else:
      for i in remove:
        text.replace(i,"")
  else:
    if len(remove) == 1:
      remove = remove[0]
      return text.replace(remove,"",amount)
    else:
      for i in remove:
        text.replace(i,"",amount)