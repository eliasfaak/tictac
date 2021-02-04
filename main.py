from learningkeras import Agent
from tictac import tictac
import numpy as np
from utils import plotLearning

if __name__ == "__main__":
    env = tictac()
    n_games = 500
    Xagent = Agent(gamma=0.99, epsilon=1.0, alpha=0.0005, input_dims=9,
                    n_actions = 9, mem_size=1000000, batch_size=64, epsilon_end=0.01)
    Oagent = Agent(gamma=0.99, epsilon=1.0, alpha=0.0005, input_dims=9,
                    n_actions = 9, mem_size=1000000, batch_size=64, epsilon_end=0.9)

    Xwins = []
    Owins = []

    for i in range(n_games):
        done = False
        valid = False
        Xscore = 0
        Oscore = 0
        observation = env.reset()
        while not done:
            Xaction = Xagent.choose_action(observation)
            observation_, reward, done, winner, valid = env.Xstep(Xaction)
            Xscore += reward+10*winner
            Oscore += -10*winner
            if winner == 1:
                Xwins.append(winner)
            if winner == -1:
                Owins.append(winner)
            Xagent.remember(observation, Xaction, Xscore, observation_, done)
            observation = observation_
            Xagent.learn()

            Oaction = Oagent.choose_action(observation)
            observation_, reward, done, winner, valid = env.Ostep(Oaction)
            Oscore += reward-10*winner
            Xscore += 10*winner
            if winner == 1:
                Xwins.append(winner)
            if winner == -1:
                Owins.append(winner)
            Oagent.remember(observation, Oaction, Oscore, observation_, done)
            observation = observation_
            Oagent.learn()



        print("episode", i, "Xwins %2f Owins %2f Xscore %2f Oscore %2f" %(len(Xwins),len(Owins),Xscore,Oscore))

        if i %10 == 0 and i > 0:
            Xagent.save_model()

    filename = "tictac.png"
    x = [i+1 for i in range(n_games)]
    plotLearning(x, score, eps_history, filename)
