import os
import sys
import yara
from requests import post

if len(sys.argv) < 2:
    sys.exit("yara_rest folder yararule")

# fetch yara signature file
try:
    rule_payload = {'rulename': sys.argv[2]}
    r = post('http://192.168.1.79:80/get', data=rule_payload)
except:
    sys.exit("- Failed to download yara rule")
# fetch the rules
rules = yara.compile(sources={'namespace': r.text})

for root, dirs, filenames in os.walk(sys.argv[1]):
    for name in filenames:
        try:
            file_path = os.path.join(root, name)
            matches = rules.match(filepath=file_path)

            if matches:
                payload = {"rulename": matches[0],
                           "filename": file_path,
                           "hostname": os.environ['COMPUTERNAME']}
                p = post('http://192.168.1.79:80/put', data=payload)
        except:
            continue
