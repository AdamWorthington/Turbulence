import json, requests, time

urls = [
	[
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/heartbeat",
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/temperature",
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/1/sensors/voltage"
	],
	["https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/heartbeat",
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/temperature",
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/2/sensors/voltage"
	],
	["https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/heartbeat",
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/temperature",
	"https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/3/sensors/voltage"
	]
]

def post(payload):
	url = "http://httpbin.org/post"
	headers = {"content-type": "application/json"}
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	print str(response.text)

def main():
	i = 0
	temperature = 0
	voltage = 0
	while 1 :
		j = 0
		outer = {}
		inner = {}
		cur_time = str(int(time.time()))
		outer["messageId"] = "turbulence-" + cur_time
		for val in urls[i]:

			resp = requests.get(url=val)
			o = json.loads(resp.text)
			if o is not None:
				if (j == 0) and ("status" in o):
					status = o["status"]
				elif (j == 1) and ("value" in o):
					temperature = o["value"]
				elif (j == 2) and ("value" in o):
					voltage = o["value"]
				inner["name"] = "turbulence-turbine-" + str(i + 1) + "-temperature"

				datapoints = [int(cur_time), temperature, voltage]
				dataset = [datapoints]
				inner["datapoints"] = dataset
				data_arr = [inner]
				outer["body"] = data_arr
				j = j + 1
		post (outer)
		i = (i + 1)% 3

if __name__== "__main__":
  main()

