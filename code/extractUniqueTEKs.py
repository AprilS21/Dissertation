import os
import zipfile
import tempfile
from datetime import datetime
import glob
import binascii
import numpy as np
import TemporaryExposureKeyExport_pb2

def when_is_it_again():
    return datetime.utcnow().strftime("%Y%m%d-%H%M%S")

def extract(file_path):
    g = TemporaryExposureKeyExport_pb2.TemporaryExposureKeyExport()
    with open(os.path.join(file_path, "export.bin"), "rb") as f:
        header = f.read(16)
        try:
            g.ParseFromString(f.read())
        except:
            return ""
    
    return '\n'.join(binascii.hexlify(key.key_data).decode() for key in g.keys)

def main():
    NOW = when_is_it_again()
    temp_file = tempfile.NamedTemporaryFile(suffix=".teksXXXX", dir="D:\\Dissertation\\data_dest\\uniques", delete=False)
    tmpf = temp_file.name

    list_files = os.path.join("D:\\Dissertation\\data_dest\\all-zips", '*.zip')
    files = glob.glob(list_files)
    num = len(files)

    print(f"Starting processing at {NOW} of {num} into {tmpf}")

    count = 0
    good_count = 0
    bad_count = 0

    unique_teks_set = set()

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
                if result:
                    output_file.write(result + '\n')
                    unique_teks_set.update(result.splitlines())
            except Exception as e:
                bad_count += 1
                print(f"Unzip of {file} failed: {e}")

    unique_teks_list = sorted(unique_teks_set)
    with open(tmpf, "w") as output_file:
        output_file.write('\n'.join(unique_teks_list))

    NOW = when_is_it_again()
    print(f"Finished at {NOW}, de-duped result is {len(unique_teks_list)}, non de-duped set in {tmpf}")

if __name__ == "__main__":
    main()
