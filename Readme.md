# TP1

The guide is seperated into three parts. 
* The first half is about how to build up the clusters and load balancer.
* The second part is regarding how to setup the environment of instances (with two options). 
* The third section provides a script to build a virtual environment and evaluate the system.

## Load Balancer and Clusters
### Instance
* Configure Security Group
    * First instance: Create a new security group and choose **All TCP** in order to let the requests reach the instance. 
    * Others: choose **existing security group** and select the group that just created. 
* Name the instances after launching to ease the following procedures.

### Target Group
Bind the instances into clusters, one target group per cluster.
* First step
    * Target type: `instance` 
    * Health check path: `/cluster1` or `/cluster2`
* Second step
    * Register the instances that belong to the cluster
### Load Balancer
* Type: `Application Load Balancer`
* Step1: default configuration is fine, but be awared of choosing the avaliablility zone that the instances stay at.
* Step2: (default)
* Step3: choose the existing security group.
* Step4: choose the existing target group.
* Step5-6: (default)

After launching, do the following steps to redirect requests.
* `Listener` -> `View/edit rules` (add a new one if there isn't any listener exists)
* Add rules
    * `Add condition` -> `path` -> fill in the value (such as */cluster1* or */cluster2*) -> confirm
    * `Add action` -> `Forward to` -> select the target group -> confirm
    * Save


## Instance setup (Option 1)
All the following commands should be run as **root user**.
```
sudo su
```
### Initial
Please run the script if instances just built.
Otherwise, this could be ignored.
```
apt update && apt upgrade -y
```

### Install package
```
apt install python3-venv python3-pip -y
pip install Flask
```

### Execute Flask
Please set up the correct route in `hello.py` in advance.
```
export FLASK_APP=hello.py
flask run --host=0.0.0.0 --port=80
```

## Instance setup (Option 2)
The commands above can be executed by scripts, please also use **root user**.
```
sudo su
```
and run the scripts from root directory
```
./scripts/build.sh
./scripts/run.sh
```

## Evaluation
```
./scripts/evaluate.sh
```