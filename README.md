### multi-agent-rl

Cloning Steps:
```
git clone --recursive -j8 git@github.com:VineetTambe/multi-agent-rl.git
```

Installation steps:

It is recomended that you create a python virtual environment and install the following packages.

1. `cd gym-multigrid/ && pip install -e .`
2. `cd ..`
3. `cd rl-baselines3-zoo/ && pip install -e . && pip install -r requirements.txt`

If you face any errors while install box2d run the following - 
```
sudo apt install swig
```

```
pip install -r requirements.txt
```

How to train:

cd to the  `rl-baselines3-zoo` repository and run the following command:

```
python3 train.py --env multigrid-mapf-v0 --algo ppo --env-kwargs scenario_file:\'/home/vineet/competition/Start-Kit/example_problems/warehouse.domain/warehouse_small_10.json\'
```

How to update training params:

The training params are located in the `hyperparams` folder in `rl-baselines3-zoo` directory - you can update the params for the algorithm being used here.