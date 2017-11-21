import random

class Markov(object):

  def __init__(self):
    self.model = {}
    self.state = (None, None)


  def add(self, word):
    if self.state in self.model:
      self.model[self.state].append(word)
    else:
      self.model[self.state] = [word]
    self.transition(word)

  def reset(self):
    self.state = (None, None)

  def random_next(self):
    list = self.model[self.state]
    choice = random.choice(list)
    self.transition(choice)
    return choice

  def transition(self, next):
    self.state = (self.state[1], next)

def make_word_model(filename):
  infile = open(filename)
  model = Markov()
  for line in infile:
    words = line.split()
    for w in words:
      model.add(w)
  infile.close()
  model.add(None)
  model.reset()
  return model

def generate_word_chain(markov, n):
  words = []
  for i in range(n):
    next = markov.random_next()
    if next is None: break
    words.append(next)
  return " ".join(words)

model = make_word_model("alice.txt")
print(generate_word_chain(model, 100))
