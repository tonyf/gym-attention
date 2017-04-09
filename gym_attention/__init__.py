from gym.envs.registration import register

register(
    id='attention-v0',
    entry_point='gym_attention.envs:AttentionEnv',
)
