import json, requests

#This is bad an need refactored TODO: Make array genius

h1 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/heartbeat'
t1 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature'
v1 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage'

h2 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/heartbeat'
t2 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature'
v2 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage'

h3 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/heartbeat'
t3 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature'
v3 = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/voltage'

# test = ['https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/heartbeat',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/heartbeat',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/heartbeat',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature',
# 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/voltage']

resp = requests.get(url=h1)
o_h1 = json.loads(resp.text)
resp = requests.get(url=v1)
o_t1 = json.loads(resp.text)
resp = requests.get(url=t1)
o_v1 = json.loads(resp.text)

resp = requests.get(url=h2)
o_h2 = json.loads(resp.text)
resp = requests.get(url=v2)
o_t2 = json.loads(resp.text)
resp = requests.get(url=t2)
o_v2 = json.loads(resp.text)

resp = requests.get(url=h3)
o_h3 = json.loads(resp.text)
resp = requests.get(url=v3)
o_t3 = json.loads(resp.text)
resp = requests.get(url=t3)
o_v3 = json.loads(resp.text)

print o_h1

print('_______________________________\nTurbine 1')
print('Status: ' + str(o_h1) + '\nVoltage: ' + str(o_v1) + '\nTemperature: ' + str(o_t1))
print('_______________________________\nTurbine 2')
print('Status: ' + str(o_h2) + '\nVoltage: ' + str(o_v2) + '\nTemperature: ' + str(o_t2))
print('_______________________________\nTurbine 3')
print('Status: ' + str(o_h3)+ '\nVoltage: ' + str(o_v3) + '\nTemperature: ' +str(o_t3))
print('_______________________________\n')