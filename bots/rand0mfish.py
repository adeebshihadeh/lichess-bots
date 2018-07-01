import chess
from random import choice, getrandbits
from stockfish import Stockfish

class RandomFish():
  def __init__(self):
    self.stockfish = Stockfish()
    self.board = chess.Board()

  def get_config(self):
    return 'rand0mfish.yml'

  def get_name(self):
    return 'rand0mfish'

  def new_game(self):
    self.board.reset()

  def set_position(self, moves):
    self.board.reset()
    for m in moves:
      self.board.push(chess.Move.from_uci(m))

  def get_move(self):
    # random move
    if bool(getrandbits(1)): return choice(list(self.board.legal_moves))

    # stockfish move
    self.stockfish.set_fen_position(self.board.fen())
    return self.stockfish.get_best_move()
