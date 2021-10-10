import time
import requests

# DNS address of the load balancer, like
url = "http://tp1-408593023.us-east-1.elb.amazonaws.com/"

def sendRequest(cluster, iter):
    for i in range(iter):
        print('%3d' % i + ': ', end='')
        r = requests.get(url + cluster)
        try:
            print(str(r.json()) + '\tstatus ' + str(r.status_code))
        except:
            print('\033[0;31mFailed to responce\033[0m\t\t\tstatus ' + str(r.status_code))

def scenario1(cluster):
    print('\033[1;33m' + '-'*15 + cluster + ' starts scenario1' + '-'*15 + '\033[0m')
    start = time.time()
    sendRequest(cluster, 1000)
    duration = time.time()-start

    print('\033[1;33m' + '-'*8, end='')
    print(cluster + ' completed scenario1 in ' + '%.2f' % duration + ' sec', end='')
    print('-'*7 + '\033[0m', end='\n\n')

def scenario2(cluster):
    print('\033[1;36m' + '-'*15 + cluster + ' starts scenario2' + '-'*15 + '\033[0m')
    start = time.time()
    sendRequest(cluster, 500)
    print('\033[1;36m' + '-'*21 + 'Sleep 60 sec ' + '-'*21 + '\033[0m')
    time.sleep(60)
    sendRequest(cluster, 1000)
    duration = time.time()-start

    print('\033[1;36m' + '-'*8, end='')
    print(cluster + ' completed scenario2 in ' + '%.2f' % duration + ' sec', end='')
    print('-'*7 + '\033[0m', end='\n\n')

if __name__ == '__main__':
    scenario1('cluster1')
    scenario1('cluster2')
    scenario2('cluster1')
    scenario2('cluster2')