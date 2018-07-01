# lichess bots

interface python chess engines with the lichess bot api

## play against the bots

[rand0mfish](https://lichess.org/@/rand0mfish)

## usage

each new bot/engine needs a python and config file. it must contain the following functions as outlined in bots/template_engine.py: `get_move()`,`get_name()`, `get_config()` , `set_position(moves)`, and `new_game()`. 


to add a bot:

* add its python and config file to the bots/ directory
* import it in `bots.py`
* add an instance of it to `bot_list` in bot.py


run manager.py to launch an instance of each bot in `bot_list`
