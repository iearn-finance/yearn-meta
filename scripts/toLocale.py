import os
import json

protocolsFolder = "./data/protocols/"
strategiesFolder = "./data/strategies/"
tokensFolder = "./data/tokens/"

folders = [protocolsFolder, strategiesFolder, tokensFolder]
for folder in folders:
	for dirpath, dirnames, filenames in os.walk(folder):
		for fileName in filenames:
			if (fileName.endswith('json')):
				filePath = os.path.join(dirpath, fileName)
				with open(filePath, 'r') as f:
					data = json.load(f)
				if ('name' in data):
					data["localization"] = {
						"en": {"name": data["name"], "description": data["description"]},
						"fr": {"name": data["name"], "description": data["description"]},
						"es": {"name": data["name"], "description": data["description"]},
						"de": {"name": data["name"], "description": data["description"]},
						"pt": {"name": data["name"], "description": data["description"]},
						"el": {"name": data["name"], "description": data["description"]},
						"tr": {"name": data["name"], "description": data["description"]},
						"vi": {"name": data["name"], "description": data["description"]},
						"zh": {"name": data["name"], "description": data["description"]},
						"hi": {"name": data["name"], "description": data["description"]},
						"ja": {"name": data["name"], "description": data["description"]},
						"id": {"name": data["name"], "description": data["description"]},
						"ru": {"name": data["name"], "description": data["description"]},
					}
				else:
					data["localization"] = {
						"en": {"description": data["description"]},
						"fr": {"description": data["description"]},
						"es": {"description": data["description"]},
						"de": {"description": data["description"]},
						"pt": {"description": data["description"]},
						"el": {"description": data["description"]},
						"tr": {"description": data["description"]},
						"vi": {"description": data["description"]},
						"zh": {"description": data["description"]},
						"hi": {"description": data["description"]},
						"ja": {"description": data["description"]},
						"id": {"description": data["description"]},
						"ru": {"description": data["description"]},
					}
				with open(filePath, 'w') as f:
					json.dump(data, f, indent=4)
print("The localization has been updated")
