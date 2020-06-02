"""

[
 [x,x,o],
 [o,x,o],
 [o,o,x]
]


"""

class Game:
  def __init__(self):
    self.board=Board()
    self.moves=0
    self.playerX=Player('X')
    self.playerO=Player('O')
    
  def startGame(self):
    self.board.displayBoard()
    while self.moves<9:
      if self.moves%2==0:
        self.promptPlayerX()
        x=int(input())
        y=int(input())
        if self.playerXMove(x,y):
          self.moves+=1
          if self.checkWinner(self.playerX):
            self.WinnerFound(self.playerX)
            return
      else:
        self.promptPlayerO()
        x=int(input())
        y=int(input())
        if self.playerOMove(x,y):
          self.moves+=1
          if self.checkWinner(self.playerO):
            self.WinnerFound(self.playerO)
            return
      self.board.displayBoard()
    self.board.displayBoard()
    print("GAME TIED!!")
    self.resetGame()

  def WinnerFound(self,player):
    print("Player"+player.marker+" Won!!")
    self.resetGame()
    
  def resetGame(self):
    self.moves=0
    self.board=Board()

  def promptPlayerX(self):
    print("Player X's turn")

  def promptPlayerO(self):
    print("Player O's turn")

  def playerXMove(self,x,y):
    return self.board.placeMarker(x,y,self.playerX)

  def playerOMove(self,x,y):
    return self.board.placeMarker(x,y,self.playerO)

  def checkWinner(self,player):
    return self.board.checkIfWinner(player)
    
  
class Player:
  def __init__(self,marker):
    self.marker=marker



class Board:
  def __init__(self):
    self.grid=[['-' for i in range(3)] for j in range(3)]
    self.rowScore=[[0 for i in range(3)] for j in range(2)]
    self.colScore=[[0 for i in range(3)] for j in range(2)]
    self.diagScore=[[0 for i in range(2)] for j in range(2)]

  def placeMarker(self,x,y,player):
    if not self.isValid(x-1,y-1):
      self.invalidMoveAlert()
      return False
    self.grid[x-1][y-1]=player.marker
    player_ptr=0
    if player.marker=='O':
      player_ptr=1

    self.rowScore[player_ptr][x-1]+=1
    self.colScore[player_ptr][y-1]+=1
    if x-1==y-1 or x-1==len(self.grid)-1-(y-1):
      if x==2 and y==2:
        self.diagScore[player_ptr][0]+=1
        self.diagScore[player_ptr][1]+=1
      else:
        if x-1==y-1:
          diagptr=0
        else:
          diagptr=1
        self.diagScore[player_ptr][diagptr]+=1
    return True

  def invalidMoveAlert(self):
    print("Invalid Move")

  def checkIfWinner(self,player):
    """
    self.rowScore=[[3,1,1]]
    """
    if player.marker == 'X':
      if max(self.rowScore[0])==3 or max(self.colScore[0])==3 or max(self.diagScore[0])==3:
        self.displayBoard()
        return True
    elif player.marker == 'O':
      if max(self.rowScore[1])==3 or max(self.colScore[1])==3 or max(self.diagScore[1])==3:
        self.displayBoard()
        return True

  def isValid(self,x,y):
    if x<0 or y<0 or x>2 or y>2:
      return False
    elif self.grid[x][y] != '-':
      return False
    else:
      return True

  def displayBoard(self):
    for row in self.grid:
      print(row)


this_game=Game()
this_game.startGame()
