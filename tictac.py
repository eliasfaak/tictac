import numpy as np

class tictac:
    def __init__(self):
        self.board = np.zeros(9)
        self.done = False



    def Xstep(self,action):
        reward = 0
        winner = 0
        valid = True
        if self.board[action] == 0:
            self.board[action] = 1
        else:
            reward = -0.1
            valid = False
        if np.prod(self.board)!=0:
            self.done = True

        if self.board[0]==self.board[1]==self.board[2]!= 0:
            self.done = True
            winner = self.board[0]
        if self.board[3]==self.board[4]==self.board[5]!= 0:
            self.done = True
            winner = self.board[3]
        if self.board[6]==self.board[7]==self.board[8]!= 0:
            self.done = True
            winner = self.board[6]
        if self.board[0]==self.board[4]==self.board[8]!= 0:
            done = True
            winner = self.board[0]
        if self.board[2]==self.board[4]==self.board[6]!= 0:
            self.done = True
            winner = self.board[2]

        return self.board, reward, self.done, winner, valid






    def Ostep(self,action):
        reward = 0
        winner = 0
        valid = True
        if self.board[action] == 0:
            self.board[action] = -0.1
        else:
            reward = -1
            valid = False
        if np.prod(self.board)!=0:
            self.done = True

        if self.board[0]==self.board[1]==self.board[2] != 0:
            self.done = True
            winner = self.board[0]
        if self.board[3]==self.board[4]==self.board[5]!= 0:
            self.done = True
            winner = self.board[3]
        if self.board[6]==self.board[7]==self.board[8]!= 0:
            self.done = True
            winner = self.board[6]
        if self.board[0]==self.board[4]==self.board[8]!= 0:
            winner = self.board[0]
        if self.board[2]==self.board[4]==self.board[6]!= 0:
            self.done = True
            winner = self.board[2]
        return self.board, reward, self.done, winner, valid


    def reset(self):
        self.board = np.zeros(9)
        self.done = False
        return self.board#, reward, self.done, winner, valid
