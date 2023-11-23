# 16831-Project

```
cd rl-baseline3-zoo
python train.py
```

Execution is similar to the individual repositories. Call the train script in the root folder of rl-baseline-zoo to start training on the warehouse domain small map of 10 agents. The scenario file can be updated in the mapf_env script of multigrid folder.

The default arguements of train have been set to a2c algo and the MAPF environment. The hyperparams folder has the a2c.yml file which houses the hyperparametes for a2c being used on MAPF. The current values for the hyperparams are dummy values and need to be updated. Similar params need to be added for all other implementations we are interested in (PPO, etc.).

RL-baseline-zoo had an error in the reset call of the environment because it expected the seed argument. For now, I have downgraded rl-baseline-zoo to work with gym instead of gymnasium. When the train script is called, you can expect a ValueError originating from the reset function of multigrid.
