"""
Codemonk link: https://www.hackerearth.com/practice/basic-programming/operators/basics-of-operators/practice-problems/algorithm/going-to-office-e2ef3feb/

We can book two types of taxis, an online taxi or a classic taxi. The online taxi costs, Oc for the first Of km and then
Od for every km afterward. The classic taxi travels at speed Cs km per minute and costs Cb, Cm and Cd, that represent
the base fare, the cost for every minute spent in the taxi and the cost for each km that you ride. Find which taxi is
cheaper.

Input - Output:
First line the distance from the destination.
Second line Oc, Of and Od and the third one
Cs, Cb, Cm, Cd.
The output is Online Taxi or Classic taxi.

Sample input:
13
6 7 4
4 2 1 2

Sample Output:
Online Taxi
"""

"""
We compute the cost. This is straight forward.

Final complexity: O(1)
"""

distance = int(input())
online_taxi_params = list(map(int, input().rstrip().split()))
classic_taxi_params = list(map(int, input().rstrip().split()))

remaining = distance - online_taxi_params[1]
if remaining >= 0:
    online_taxi_cost = online_taxi_params[0] + remaining * online_taxi_params[2]
else:
    online_taxi_cost = online_taxi_params[0]

classic_taxi_cost = (classic_taxi_params[1] + distance * classic_taxi_params[3]
                     + (distance // classic_taxi_params[0]) * classic_taxi_params[2])

if online_taxi_cost <= classic_taxi_cost:
    print("Online Taxi")
else:
    print("Classic Taxi")
