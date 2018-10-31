import mfrc522
from os import uname
import urequests
import ujson


def do_read():
	Value = "0"
	print("here")
	rdr = mfrc522.MFRC522(5, 18, 19, 13, 23)

	print("")
	print("Place card before reader to read from address 0x08")
	print("")

	try:
		while True:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					print("New card detected")
					#print("  - tag type: 0x%02x" % tag_type)
					#print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					#print("")
					#print("this is the raw id")
					#print(raw_uid)

					if raw_uid[0] == 136 and raw_uid[1] == 4 and raw_uid[2] == 101 and raw_uid[3] == 88:
						if Value == "1":
							Value = "0"
						else:
							Value = "1"
						print("This is a good card.")
					else:
						print("This is a bad card. Door Status will remain unchanged")
						print("")

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



	except KeyboardInterrupt:
		print("Bye")