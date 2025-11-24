import random

class BoggleBoard:
  
  def __init__(self):
    self.line1 = ["____"]
    self.line2 = ["____"]
    self.line3 = ["____"]
    self.line4 = ["____"]

  def shake(self):
    self.line1 = []
    self.line2 = []
    self.line3 = []
    self.line4 = []
    for i in range(4):
      self.line1.append(chr(random.randint(ord('A'), ord('Z'))))
      self.line2.append(chr(random.randint(ord('A'), ord('Z'))))
      self.line3.append(chr(random.randint(ord('A'), ord('Z'))))
      self.line4.append(chr(random.randint(ord('A'), ord('Z'))))

    print("".join(self.line1))
    print("".join(self.line2))
    print("".join(self.line3))
    print("".join(self.line4))     

boggle_board1 = BoggleBoard()
# print("".join(boggle_board1.line1))
# print("".join(boggle_board1.line2))
# print("".join(boggle_board1.line3))
# print("".join(boggle_board1.line4))
boggle_board1.shake()
