import json, requests

test = [
	[
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/heartbeat',
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature',
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/voltage'
	],
	['https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/heartbeat',
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature',
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage'
	],
	['https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/heartbeat',
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature',
	'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/voltage'
	]
]

i = 0
while 1 :
	j = 0
	builder = ""
	builder = builder + ('____________________________\nTurbine ' + str(i+1) + ':\n')
	for val in test[i]:
		resp = requests.get(url=val)
		o = json.loads(resp.text)
		if (j == 0) and ('status' in o):
			
			builder = builder + ('Status: ' + str(o['status']) + '\n')
		elif (j == 1) and ('value' in o):
			builder = builder + ('Temperature: ' + str(o['value'])+ '\n')
		elif (j == 2) and ('value' in o):
			builder = builder + ('Voltage: ' + str(o['value'])+ '\n')
		else:
			builder = builder +  'Could not reach api\n'
		j = j + 1
	print builder
	i = (i + 1)% 3
