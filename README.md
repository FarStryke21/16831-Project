### multi-agent-rl

Cloning Steps:
```
git clone --recursive -j8 git@github.com:VineetTambe/multi-agent-rl.git
```

#### Installation steps:

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

#### How to train:

cd to the  `rl-baselines3-zoo` repository and run the following command:

```
python3 train.py --env multigrid-mapf-v0 -lb ./logs/ppo/ --algo ppo --env-kwargs scenario_file:\'/home/vineet/competition/Start-Kit/example_problems/warehouse.domain/warehouse_small_10.json\'
```
```
python3 train.py -tb ./logs/ppo/ --env multigrid-mapf-v0 --conf-file ./hyperparams/python/ppo_cnn_config.py --algo ppo --env-kwargs scenario_file:\'/home/admin/multi-agent-rl/Start-Kit/example_problems/warehouse.domain/warehouse_small_10.json\' agent_view_size:40
```
#### How to update training params:

The training params are located in the `hyperparams` folder in `rl-baselines3-zoo` directory - you can update the params for the algorithm being used here.

#### Use the following file to run the model with other python code:

cd to the  `rl-baselines3-zoo` repository and run the following command:

You will have to modify the following lines `87 - 90`
The model.predict code is at `215 - 225`

```
python3 custom_runner.py
```

#### How to run stand alone:

cd to the  `rl-baselines3-zoo` repository and run the following command:

```
python3 enjoy.py --env multigrid-mapf-v0 --algo ppo --env-kwargs scenario_file:\'/home/vineet/competition/Start-Kit/example_problems/warehouse.domain/warehouse_small_10.json\' -f logs/ --exp-id 2 --load-best

```