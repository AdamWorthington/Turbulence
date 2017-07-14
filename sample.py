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

def post(payload):
	url = 'http://httpbin.org/post'
	headers = {'content-type': 'application/json'}
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	print str(response.text)

def main():
	i = 0
	while 1 :
		j = 0
		data = {}
		data['id'] = i + 1
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
		#print str(data)
		post(data)
		i = (i + 1)% 3


if __name__== "__main__":
  main()