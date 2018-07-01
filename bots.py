import sys


# import bots
path = "./bots/"
sys.path.append(path)
from rand0mfish import RandomFish


bot_list = {
  "rand0mfish": RandomFish()
}

