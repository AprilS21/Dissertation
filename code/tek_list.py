#!/usr/bin/python3
import sys
import binascii
import TemporaryExposureKeyExport_pb2

# # Check if the correct number of arguments is provided
# if len(sys.argv) != 2:
#     print("Usage: python TEK_LIST.py <file_path>")
#     sys.exit(1)

# Extract the file path from the command-line arguments
#print(len(sys.argv))
file_path = sys.argv[1]
#print(file_path)
#sys.exit(1)

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
for key in g.keys:
	#print(str(binascii.hexlify(key.key_data))+
                #str(key.rolling_start_interval_number)+", period:"+str(key.rolling_period)+
	        #str(key.transmission_risk_level))
	print(binascii.hexlify(key.key_data).decode())
	#print("start interval: "+str(key.rolling_start_interval_number)+", period:"+str(key.rolling_period))
	#print("transmission risk level: "+str(key.transmission_risk_level))
sys.exit(len(g.keys))

