import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from collections import defaultdict

num_states = 500
num_actions = 6
Q = np.zeros((num_states, num_actions))

alpha = 0.4  # learning rate
gamma = 0.95  # discount factor
epsilon = 1  # exploration-exploitation trade-off

iterations = 800
iteration_scores = []

epsilon_step = epsilon/iterations
epsilon_coeff = 2

total_score = 0
ten_percent = int(0.1 * iterations)
score_10_perc = 0

success = defaultdict(int)

def train():
    temp_success = defaultdict(int)
    global epsilon, alpha, gamma, iterations, iteration_scores, epsilon_step, epsilon_coeff, total_score, score_10_perc, success
    last_ep = 0
    env = gym.make("Taxi-v3")

    for ep_num in range(iterations):
        observation, info = env.reset()
        ep_score = 0

        for t in range(200):
            if np.random.rand() < epsilon:
                action = env.action_space.sample()  # explore
            else:
                action = np.argmax(Q[observation, :])  # exploit

            next_observation, reward, terminated, truncated, info = env.step(action)

            ep_score += reward

            best_next_action = np.argmax(Q[next_observation, :])

            Q[observation, action] += alpha * (reward + gamma * Q[next_observation, best_next_action] - Q[observation, action])

            observation = next_observation
            if truncated:
                temp_success['cnt'] = 0
                break
            if terminated:
                if last_ep == ep_num - 1:
                    temp_success['cnt'] += 1
                    temp_success['last'] = ep_num
                last_ep = ep_num
                break

        iteration_scores.append(ep_score)

        if epsilon > 0 :
            epsilon -= (epsilon_coeff * epsilon_step)

        if ep_num > iterations * 0.9:   
            score_10_perc += ep_score

        total_score += ep_score
        if temp_success['cnt'] == 10:
            success = deepcopy(temp_success)

    env.close()

def statistics():
    print("\n\n")
    avg = total_score / iterations
    last_10_avg = score_10_perc / ten_percent
    print("Iterations:", iterations)
    print("Average:", avg)
    print(f"Last 10% average: ({score_10_perc} / {ten_percent}) = {last_10_avg:.2f}")
    print(f"Total to learnt ratio: {avg/last_10_avg:.2f}")
    print("10 Times in a row at iteration:", success['last'])

    average_scores = [np.mean(iteration_scores[:i + 1]) for i in range(iterations)]

    improvement = [abs(average_scores[i] - average_scores[i - 1]) if i > 0 else 0 for i in range(iterations)]

    plt.plot(improvement, label='Improvement')
    plt.xlabel('Iteration')
    plt.ylabel('Improvement')
    plt.title('Improvement Function During Training')
    plt.legend()

    # Second plot: Iteration Scores with adjusted layout
    plt.figure()
    plt.subplot(1, 1, 1)  # Single subplot

    plt.plot(iteration_scores, label='Iteration Scores')
    plt.xlabel('Iteration')
    plt.ylabel('Score')
    plt.title('Iteration Scores During Training')
    plt.legend()

    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()

def runModel():
    env = gym.make("Taxi-v3", render_mode="human")
    for ep_num in range(5):
        observation, info = env.reset()
        ep_score = 0
        for t in range(200):

            if np.random.rand() < epsilon:
                action = env.action_space.sample()  # explore
            else:
                action = np.argmax(Q[observation, :])  # exploit

            next_observation, reward, terminated, truncated, info = env.step(action)
        
            ep_score += reward
            print(action)
            observation = next_observation
            if terminated or truncated:
                # passenger dropped off
                break

        print("Episode", ep_num, "score", ep_score)

    env.close()
    # print(Q)

train()
# runModel()
statistics()
# env = gym.make("Taxi-v3", render_mode="human")
