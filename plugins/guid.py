# taken from documentation, written by Will
# add 'guid' property to entry to override the GUID
def cb_story(args):
	entry = args["entry"]
	entry["guid"] = entry.get("guid", entry.get("file_path"))
	return args
