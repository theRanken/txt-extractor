import argparse as cmd
import pandas as pd
from core.utils import *


def run(**kwargs):	
	bank = kwargs['bank']
	output = kwargs['excel']

	pros = get_data()
	cleaned = clean_data(pros)

	print("Loading Frames...")
	
	frame = create_frame()
	
	data = frame_data(cleaned, frame) if bank is None else frame_data(cleaned, frame, search_term=bank)
				
	print("Loading Complete!")	
	
	time.sleep(0.5)
	
	pd.set_option('display.max_rows', None)
	pd.set_option('display.max_columns', 4)
	df = pd.DataFrame(data)
	
	if bank is not None and not output:
		extract(bank, df.to_string(justify="justify_all"))
	elif bank is not None and output:
		create_directory_if_non_exists(os.path.join(get_base_dir(), f'extracted/excel'))
		search_excel_file = f'extracted/excel/{bank.upper()}-excel-{get_random_number()}.xlsx'
		search_excel_dir = os.path.join(get_base_dir(), search_excel_file)
		df.to_excel( f"{search_excel_dir}", index=False, sheet_name=f"{bank.upper()} Extracted")
		print(f"Saved search '{bank}' into {search_excel_file}")
	elif bank is None and output:
		create_directory_if_non_exists(os.path.join(get_base_dir(), f'extracted/excel'))
		excel_dir = os.path.join(get_base_dir(), f'extracted/excel/All-Records-excel-{get_random_number()}.xlsx')
		df.to_excel( f"{excel_dir}", index=False, sheet_name=f"All Data Extracted")
		print("Saved to All Records to Excel")
	else:
		extract("All-Records", df.to_string(justify="justify_all"))
		# print(df.to_string(justify="justify_all"))
	
if __name__ == "__main__":
	parser = cmd.ArgumentParser(
		prog='CARD DATA EXTRACTOR',
		description='Extract relevant data from a database of information',
		epilog='refer to the "requirements.txt" file for more help or type in "python app.py --help" '
	)
	parser.add_argument("-b", "--bank", help="Search based on particular bank")
	parser.add_argument("-e", "--excel", action="store_true", help="supply this to output to excel file")
	args = vars(parser.parse_args())

	if len(args) >= 1:
		run(**args)
	else:
		run()
	