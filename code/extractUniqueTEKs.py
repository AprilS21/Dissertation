import os
import subprocess
import zipfile
import tempfile
from datetime import datetime
import glob
import sys
import binascii
import TemporaryExposureKeyExport_pb2

def when_is_it_again():
    return datetime.utcnow().strftime("%Y%m%d-%H%M%S")

def how_many(lst):
    return len(lst)

# HOME = os.getenv('HOME', r'C:\Users\stephen')
# DOCROOT = os.getenv('DOCROOT', r'C:\var\www\tact\tek-counts')
# TOP = os.getenv('TOP', os.path.join(HOME, 'code', 'tek_transparency'))
# DATADIR = os.getenv('DATADIR', os.path.join(TOP, 'data'))
# ARCHIVE = os.getenv('ARCHIVE', os.path.join(DATADIR, 'all-zips'))
# DAILIES = os.getenv('DAILIES', os.path.join(DATADIR, 'dailies'))
# DAILIES2 = os.getenv('DAILIES2', os.path.join(DATADIR, 'dailies2'))

# TEK_LIST = os.path.join(TOP, 'tek_list.py')

TOP = 'code'
DATADIR = 'D:\\Dissertation\\data_dest'
ARCHIVE = 'D:\\Dissertation\\data_dest\\all-zips'
TEK_LIST = 'tek_list.py'

#CURL = r"C:\Program Files\Curl\bin\curl.exe"

def extract(file_path):
    f = open(file_path + "\export.bin", "rb")
    g = TemporaryExposureKeyExport_pb2.TemporaryExposureKeyExport()
    header = f.read(16)
    #print("header:"+str(header))
    try:
        g.ParseFromString(f.read())
    except:
        sys.exit(-1)
    f.close()
#print("file timestamps: start "+str(g.start_timestamp)+", end "+str(g.end_timestamp))
#print("batch_num: "+str(g.batch_num)+", batch_size: "+str(g.batch_size))
#print("region: "+str(g.region))
#print("signature info:")
#print(str(g.signature_infos))
    x =''
    for key in g.keys:
	#print(str(binascii.hexlify(key.key_data))+
                #str(key.rolling_start_interval_number)+", period:"+str(key.rolling_period)+
	        #str(key.transmission_risk_level))
	    #print(binascii.hexlify(key.key_data).decode())
        x += '' + binascii.hexlify(key.key_data).decode()
	#print("start interval: "+str(key.rolling_start_interval_number)+", period:"+str(key.rolling_period))
	#print("transmission risk level: "+str(key.transmission_risk_level))
    return x

def main():
    NOW = when_is_it_again()
    temp_file = tempfile.NamedTemporaryFile(suffix=".teksXXXX", dir="D:\\Dissertation\\data_dest\\uniques", delete=False)
    tmpf = temp_file.name


    list_files = os.path.join(ARCHIVE, '*.zip')
    files = glob.glob(list_files)
    num = how_many(files)

    print(f"Starting processing at {NOW} of {num} into {tmpf}")

    count = 0
    good_count = 0
    bad_count = 0

    with open(tmpf, "w") as output_file:
        for file in files:
            count += 1
            print(f"Doing {count} of {num} which is {file}")
            
            # Create a new directory based on the ZIP file name
            dest_dir = os.path.splitext(file)[0]
            os.makedirs(dest_dir, exist_ok=True)

            # try unzip and decode
            try:
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(path=dest_dir)
                good_count += 1
                result = extract(dest_dir)
                output_file.write(result)
            except Exception as e:
                bad_count += 1
                print(f"Unzip of {file} failed: {e}")

    with open(tmpf, "r") as input_file:
        all_teks = sum(1 for line in input_file)

    print(f"result of processing {num} (good: {good_count}, bad: {bad_count}) is {all_teks}")

    with open(tmpf, "r") as input_file:
        unique_teks = set(input_file)

    unique_teks_file = f"{tmpf}.uni"
    with open(unique_teks_file, "w") as output_file:
        output_file.writelines(sorted(unique_teks))

    NOW = when_is_it_again()
    print(f"Finished at {NOW}, de-duped result is {len(unique_teks)}, non de-duped set in {tmpf}")

if __name__ == "__main__":
    main()
