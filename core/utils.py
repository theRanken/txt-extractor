import time, re, sys, os
from datetime import datetime
from random import randint

def get_data():
	f = open("data/cards_db.txt", encoding="utf8")
	uncleaned = f.readlines()
	return uncleaned
	
def clean_data(data:list)->list:
	new_dataset = list()
	for i in data:
			t = i.strip()
			new_dataset.append(t)
	return new_dataset
	
def create_frame():
	return {
		"NAME" :  list(),
		"BANK" : list(),
		"EMAIL" : list(),
		"PHONE" : list()
	}

def search_text(data:list, value)->list:
	matches = []
	for x in data:
		if value.casefold()  in x.casefold():
			matches.append(x)
			
	return matches
	
def frame_data(data:list, frame:dict, search_term=None):
		if search_term is not None:
			term = search_text(data, search_term)
			if len(term) == 0:
				return sys.exit(f"No record of '{search_term}' found!")
		final_data = data if search_term is None else term
		
		for i in final_data:
			new = i.split("|")
			name = new[3] if new[3] != "None" else "Empty"
			bank = new[4] if new[4] != "None" else "Empty"
			email = new[-2] if new[-2] != "None" else "Empty"
			phone = new[-1] if new[-1] != "None" else "Empty"
					
			frame["NAME"].append(name)
			frame["BANK"].append(bank)
			frame["EMAIL"].append(email)
			frame["PHONE"].append(phone)
					
		return frame

def get_base_dir()->None:
	return os.path.dirname(os.path.dirname(__file__))

def get_random_number()->int:
	num = f"{randint(000, 999)}{datetime.now().microsecond}"
	num = int(num)
	return num

def get_filename(filename:str, extension:str)->str:
	return f"{filename}-{get_random_number()}.{extension}"

def create_directory_if_non_exists(dirname:str)->None:
	try: 
		os.makedirs(dirname)
		return os.path.exists(dirname)
	except: pass

def extract(filename:str, data, file_type:str=None)->None:
	time = datetime.now()
	file = get_filename(filename, "txt")
	base_dir = get_base_dir()
	directory = "extracted" if file_type is None else "extracted/excel"
	folder = os.path.join(base_dir, directory)
	default_path = f"{folder}/{file}"

	create_directory_if_non_exists(folder)
	print(f"\nSaving file '{file}' to '{default_path}'...")
	with open(default_path, "w", encoding="utf8") as f:
		f.write(data)
		f.close()
	
	print("File saved!\n")

	return None