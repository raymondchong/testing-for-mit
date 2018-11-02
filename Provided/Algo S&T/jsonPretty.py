import simplejson
import json
jsons = ['sample_1.json','sample_2.json']
for file in jsons:
	with open(file) as json_data:
		data = json.load(json_data)
		jsonDataFile = open(file, "w")
		jsonDataFile.write(simplejson.dumps(data, indent=4))
		jsonDataFile.close()