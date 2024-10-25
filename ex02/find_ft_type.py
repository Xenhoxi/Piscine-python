def all_thing_is_obj(object: any) -> int:
	object_type = type(object)
	name = None
	if object_type is list:
		name = "List :"
	elif object_type is tuple:
		name = "Tuple :"
	elif object_type is set:
		name = "Set :"
	elif object_type is dict:
		name = "Dict :"
	elif object_type is str:
		name = object + " is in the kitchen :"
	else:
		print("Type not found")
	if name:
		print(f"{name} {object_type}")
	return 42

