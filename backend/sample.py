import json, requests, time
import websocket

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

con_url = 'wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'
predix_zone_id = 'd97f5953-2c07-4e8f-ac0d-8b8df897135e'

def gettoken():

   url = 'https://ff2359d6-05b4-4a0f-9001-2533c77cfe9d.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'

   payload = "grant_type=client_credentials"
   headers = {
       'content-type': "application/x-www-form-urlencoded",
       'authorization': 'Basic dHMtY2xpZW50MTpLZld1cHhTd001Q1hmaDg='
   }

   response     = requests.request("POST", url, data=payload, headers=headers)
   access_token = json.loads(response.text)[u'access_token']
   return access_token

def post2(payload):

	zone_id = (predix_zone_id)
	ingestion_url = (con_url)
	data = payload
	headers = {
		'Authorization': gettoken(),
		'Predix-Zone-Id': zone_id,
		'Content-Type': 'application/json',
	}

	ws = websocket.create_connection(ingestion_url, header=headers)
	ws.send(json.dumps(payload))
	result = ws.recv()
	print('Got back message confirmation TimeSeries:\n %s' % result)


def post(payload):
	url = "http://httpbin.org/post"
	headers = {"content-type": "application/json", "Authorization" : gettoken(), "Predix-Zone-Id" : predix_zone_id}
	response = requests.post(con_url, data=json.dumps(payload), headers=headers)
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
				# inner["name"] = "turbulence-turbine-" + str(i + 1) + "-temperature"
				inner["name"] = "turbulence-turbine-" + '4' + "-temperature"
				datapoints = [int(cur_time), temperature, voltage]
				dataset = [datapoints]
				inner["datapoints"] = dataset
				data_arr = [inner]
				outer["body"] = data_arr
				j = j + 1
		print outer
		post2 (outer)
		i = (i + 1)% 3

if __name__== "__main__":
  main()

