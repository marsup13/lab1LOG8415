#/bin/bash

# Modify the following information
LB_name=app/TP1/382a875a12350efe
Cluster1=targetgroup/cluster1/95be6976f886b7b0
Cluster2=targetgroup/cluster2/12d870f99353de8c

LB_metric() {
    aws cloudwatch get-metric-statistics --namespace AWS/ApplicationELB --metric-name $1 --statistics $2 --period 60 --dimensions Name=LoadBalancer,Value=$LB_name --start-time $startT --end-time $endT > $1_$2.json
}

TARGET_metric() {
    aws cloudwatch get-metric-statistics --namespace AWS/ApplicationELB --metric-name $1 --statistics $2 --period 60 --dimensions Name=LoadBalancer,Value=$LB_name Name=TargetGroup,Value=$Cluster1 --start-time $startT --end-time $endT > cluster1_$1_$2.json

    aws cloudwatch get-metric-statistics --namespace AWS/ApplicationELB --metric-name $1 --statistics $2 --period 60 --dimensions Name=LoadBalancer,Value=$LB_name Name=TargetGroup,Value=$Cluster2 --start-time $startT --end-time $endT > cluster2_$1_$2.json

}

# Start point
startT=$(date --iso-8601=seconds -u)
source venv_evaluate/bin/activate
python3 evaluate.py
deactivate
endT=$(date --iso-8601=seconds -u)

LB_metric ActiveConnectionCount Sum
LB_metric NewConnectionCount Sum
LB_metric RequestCount Sum
LB_metric RuleEvaluations Sum
TARGET_metric TargetResponseTime Average
TARGET_metric RequestCountPerTarget Sum

echo '----------------------------------------'
echo 'start:' $startT
echo 'end:  ' $endT
