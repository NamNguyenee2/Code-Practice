# source: https://www.geeksforgeeks.org/machine-learning/reinforce-algorithm/

import gymnasium as gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

env         = gym.make('CartPole-v1')
obs_space   = env.observation_space.shape[0]
act_space   = env.action_space.n


# Hyperparameters
gamma       = 0.99
lr          = 0.01
num_epi     = 1000
batch_size  = 32

# Policy network (actor)
class PolicyNetwork(tf.keras.Model):
    def __init__(self, hidden_units=128):
        super(PolicyNetwork, self).__init__()
        self.dense1 = layers.Dense(hidden_units, activation='relu')
        self.dense2 = layers.Dense(int(act_space), activation='softmax')

    def call(self, state):
        x = self.dense1(state)
        return self.dense2(x)

policy      = PolicyNetwork()
optimizer   = tf.keras.optimizers.Adam(learning_rate=lr)


# Compute returns
def compute_returns(rewards, gamma):
    returns         = np.zeros_like(rewards, dtype=np.float32)
    running_return  = 0

    for t in range(len(rewards) - 1, -1, -1):
        running_return = rewards[t] + gamma * running_return
        returns[t]     = running_return
    return returns


# Training step
def train_step(states, actions, returns):
    with tf.GradientTape() as tape:
        action_probs     = policy(states)
        action_indices   = np.array(actions, dtype=np.int32)

        action_log_probs = tf.math.log(tf.reduce_sum(
            action_probs * tf.one_hot(action_indices, env.action_space.n), axis=1))

        loss             = -tf.reduce_mean(action_log_probs * returns)

        grads = tape.gradient(loss, policy.trainable_variables)
        optimizer.apply_gradients(zip(grads, policy.trainable_variables))


for episode in range(num_epi):
    state = env.reset()[0]
    done = False
    states, actions, rewards = [], [], []

    while not done:
        state_input     = np.array(state, dtype=np.float32).reshape(1, -1)
        probs           = policy(state_input).numpy()[0]
        action          = np.random.choice(act_space, p=probs)

        next_state, reward, done, _, _ = env.step(action)

        states.append(state)
        actions.append(action)
        rewards.append(reward)
        state           = next_state

    returns = compute_returns(rewards, gamma)
    returns = (returns - np.mean(returns)) / (np.std(returns) + 1e-7)

    states_batch = np.vstack(states)
    train_step(states_batch, actions, returns)

    if episode % 100 == 0:
        print(f"Episode: {episode}/{num_epi}, Total Reward: {sum(rewards)}")


# Test the agent
print('------------------------------')
print('testing ....')
state = env.reset()[0]
done = False
total_reward = 0

while not done:
    state_input = np.array(state, dtype=np.float32).reshape(1, -1)
    probs = policy(state_input).numpy()[0]
    action = np.argmax(probs)

    next_state, reward, done, _, _ = env.step(action)
    total_reward += reward
    print(f"State: {state}, Action: {action}, Reward: {reward}, Total Reward: {total_reward}")
    state = next_state

print(f"Total Reward (Test): {total_reward}")