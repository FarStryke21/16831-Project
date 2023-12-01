"""This file just serves as an example on how to configure the zoo
using python scripts instead of yaml files."""
import torch
from gym_multigrid.envs.mapf_env import *

hyperparams = {
    "multigrid-mapf-v0": dict(
        env_wrapper=[{"gym_multigrid.envs.mapf_env.StackMultiGridObsWrapper": {}}],
        # normalize=True,
        n_envs=1,
        n_timesteps=float(5e5),
        policy="CnnPolicy",
        batch_size=128,
        n_steps=512,
        gamma=0.9999,
        learning_rate=2.5e-4,
        # ent_coef=0.00429,
        ent_coef=0.0,
        clip_range=0.2,
        n_epochs=10,
        gae_lambda=0.95,
        max_grad_norm=5,
        vf_coef=0.19,
        use_sde=True,
        policy_kwargs=dict(
            features_extractor_class=CustomCnnFeatureExtractor,
            features_extractor_kwargs=dict(features_dim=128),
            log_std_init=-2,
            ortho_init=False,
            activation_fn=torch.nn.GELU,
            squash_output=True,
            # net_arch=dict(pi=[256], vf=[256]),
        ),
    )
}

# multigrid-mapf-v0:
#   env_wrapper:  # See GH/1320#issuecomment-1421108191
#   # normalize: true
#   n_envs: 8 # number of environment copies running in parallel
#   n_timesteps: !!float 5e5
#   policy: 'CnnPolicy'
#   n_steps: 512 # batch size is n_steps * n_env
#   batch_size: 128 # Number of training minibatches per update
#   gae_lambda: 0.95 #  Factor for trade-off of bias vs variance for Generalized Advantage Estimator
#   gamma: 0.99
#   n_epochs: 10 #  Number of epoch when optimizing the surrogate
#   ent_coef: 0.0 # Entropy coefficient for the loss caculation
#   learning_rate: 2.5e-4 # The learning rate, it can be a function
#   clip_range: 0.2 # Clipping parameter, it can be a function
#   policy_kwargs: "dict(features_extractor_class=gym_multigrid.envs.mapf_env.CustomCnnFeatureExtractor,
#                        features_extractor_kwargs=dict(features_dim=128),
#                        log_std_init=-2,
#                        ortho_init=False,
#                        activation_fn=nn.GELU,
#                        net_arch=dict(pi=[256], vf=[256]),
#                        )"
