from classes.HDFFile import HDFFile
from classes.API import API
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("bearer")
parser.add_argument("file")
args = parser.parse_args()

def upload(host, bearer, file):
    api = API(host, f"Bearer {bearer}")
    uploadfile = HDFFile(file.split('/')[-1], open(file, 'r').read(), api, public=True)
    result = uploadfile.upload()
    if(result.status_code == 201):
        print(f"[Success] {result.json()['shareURL']}")
    else:
        print(f"[Fail] {result.status_code}: {result.text}")


upload(args.host, args.bearer, args.file)