import socket
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-uid', '--param1', required=True)
parser.add_argument('-file', '--param2', required=True)
parser.add_argument('-data', '--param3', required=True)

args = parser.parse_args()

fp = open(args.param3, 'r')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
client.connect((host, port))
res = {"UID":args.param1,
	"File":args.param2,
	"Data":fp.read()}
client.send(json.dumps(res))
