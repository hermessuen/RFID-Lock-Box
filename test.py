					from os import uname
					import urequests
					import ujson


					Tag = "RFID"
					Type = "DOUBLE"

					urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
					urlTag = urlBase + Tag
					urlValue = urlBase + Tag + "/values/current"

					headers = {"Content-Type":"application/json",
					"Accept":"application/json","x-ni-api-key": 
					"bBge5gyLU5LabL9caKiRF4oj1XO_ftaMzuRIUL3IVW"}

					propName={"type":Type,"path":Tag}
					propValue = {"value":{"type":Type,"value":Value}}

					# PUT
					print(urequests.put(urlTag,headers=headers,json=propName).text)
					print(urequests.put(urlValue,headers=headers,json=propValue).text)

					#GET
					Tag = "LockStatus"
					urlTag = urlBase + Tag
					urlValue = urlBase + Tag + "/values/current"
					value = urequests.get(urlValue,headers=headers).text

					data = ujson.loads(value)
					result = data.get("value").get("value")
					print ("Door is ",result)