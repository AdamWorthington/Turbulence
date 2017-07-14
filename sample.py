import json, requests

urls = [
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
	data = {}
	data['status'] = "ERR"
	data['temperature'] = -1
	data['voltage'] = -1
	for val in urls[i]:
		resp = requests.get(url=val)
		o = json.loads(resp.text)
		if (j == 0) and ('status' in o):
			data['status'] = o['status']
		elif (j == 1) and ('value' in o):
			data['temperature'] = o['value']
		elif (j == 2) and ('value' in o):
			data['voltage'] = o['value']
		j = j + 1
	print str(data)
	i = (i + 1)% 3