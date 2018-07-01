#!/usr/bin/python3

from __future__ import print_function
from __future__ import division
import importlib
import re
import sys
import time
import os

import bots


if sys.version_info[0] == 2:
  input = raw_input

class Unbuffered(object):
  def __init__(self, stream):
    self.stream = stream
  def write(self, data):
    self.stream.write(data)
    self.stream.flush()
  def __getattr__(self, attr):
    return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

# logging
def printf(msg):
  os.system("printf '{}\n' >> log".format(msg))


def main(bot):
  print(bot.get_name())

  cmds = []
  while True:
    if cmds:
      cmd = cmds.pop()
    else:
      cmd = input()

    if cmd == 'quit':
      break

    elif cmd == 'uci':
      print('uciok')

    elif cmd == 'isready':
      print('readyok')

    elif cmd == 'ucinewgame':
      bot.new_game()

    elif cmd.startswith('position'):
      if 'moves' in cmd:
        bot.set_position(cmd.split('moves ')[1].split(' '))
      elif 'startpos' in cmd:
        bot.new_game()

    elif cmd.startswith('go'):
      print('bestmove {}'.format(bot.get_move()))

if __name__ == '__main__':
  bot = os.environ["engine"]

  if bot not in bots.bot_list:
    printf('bot not found')
    sys.exit(0)

  main(bots.bot_list[bot])
