#!/usr/bin/python3
import sys
import os

import bots

lichess_dir = './lichess-bot/'


def main():
  # launch instances of bots
  for bot in bots.bot_list:
    name = bots.bot_list[bot].get_name()
    config = bots.path + bots.bot_list[bot].get_config()
    os.system('engine="{}" python3 {}lichess-bot.py --config {} &'.format(name, lichess_dir, config))

if __name__ == '__main__':
  main()

