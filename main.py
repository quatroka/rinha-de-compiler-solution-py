from src.interpreter import process_file

filepath = "/var/rinha/source.rinha.json"
# import sys
# filepath = sys.argv[1] if len(sys.argv) > 1 else '/var/rinha/source.rinha.json'

process_file(filepath)
