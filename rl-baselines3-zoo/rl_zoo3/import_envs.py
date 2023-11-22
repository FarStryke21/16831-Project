from typing import Callable, Optional

import gymnasium as gym
from gymnasium.envs.registration import register
# from gym.envs.registration import register
from rl_zoo3.wrappers import MaskVelocityWrapper

import rl_zoo3.gym_multigrid.mapf_env_test as MapfEnv

try:
    import pybullet_envs_gymnasium
except ImportError:
    pass

try:
    import highway_env
except ImportError:
    pass
else:
    # hotfix for highway_env
    import numpy as np

    np.float = np.float32  # type: ignore[attr-defined]

try:
    import custom_envs
except ImportError:
    pass

try:
    import gym_donkeycar
except ImportError:
    pass

try:
    import panda_gym
except ImportError:
    pass

try:
    import rocket_lander_gym
except ImportError:
    pass

try:
    import minigrid
except ImportError:
    pass

try:
    import gym_multigrid
    print("Multigrid installed")
except ImportError:
    print("Multigrid not installed")


# # Register no vel envs
# def create_no_vel_env(env_id: str) -> Callable[[Optional[str]], gym.Env]:
#     def make_env(render_mode: Optional[str] = None) -> gym.Env:
#         env = gym.make(env_id, render_mode=render_mode)
#         env = MaskVelocityWrapper(env)
#         return env

#     return make_env


# for env_id in MaskVelocityWrapper.velocity_indices.keys():
#     name, version = env_id.split("-v")
#     register(
#         id=f"{name}NoVel-v{version}",
#         entry_point=create_no_vel_env(env_id),  # type: ignore[arg-type]
#     )


# --------------------------------------------------------------------------------------
register(
    id='multigrid-mapf-v0',
    entry_point='gym_multigrid.envs:MapfEnv',
)
# env = gym.make(
#             "gym_multigrid:multigrid-mapf-v0",
#             # map_file_path="gym_multigrid/envs/maps/mapf_10x10_2.txt",
#             # agent_file_path="gym_multigrid/envs/maps/agents_10x10_2.txt",
#             # task_file_path="gym_multigrid/envs/maps/tasks_10x10_2.txt",
#             # scenario_file="/city.domain/paris_200.json",
#             # scenario_file="/home/vineet/competition/Start-Kit/example_problems/warehouse.domain/warehouse_small_10.json",
#             scenario_file = "mingrid-envs/warehouse.domain/warehouse_small_10.json",
#         )
# _ = env.reset()
print("Multigrid Env Registered!")

