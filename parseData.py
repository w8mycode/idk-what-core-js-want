import os
import re
import json


def is_required_key(line):
  return "optimal implementation of" in line


def is_required_value(line):
  return "fnStr.includes" in line and not "return" in line

def fill(result_dic_, file):
  keys = []
  values = []

  for line in parse(file):
    line = line.strip()

    if is_required_key(line):
      key = re.findall("of (.+?)\'", line)
      keys.append(key)

    if is_required_value(line):
      value = re.findall("\'(.+?)\'", line)
      values.append(value)

  for index, _ in enumerate(keys):
    key = keys[index][0]
    value = values[index][0]

    if (len(values[index]) > 1):
      value = (', ').join(values[index])

    result_dic_[key] = value

  return result_dic_


def parse(file_name):
  with open(file_name, encoding='utf-8') as file: 
    while True:
      line = file.readline()
      if not line:
        break

      yield line


in_file_strings = os.path.join('data', 'strings-tests.js')
in_file_numbers = os.path.join('data', 'numbers-tests.js')
out_json_file = os.path.join('data', 'data.json')

data = {}

data = fill(data, in_file_strings)
data = fill(data, in_file_numbers)


with open(out_json_file, "w") as outfile:
  json.dump(data, outfile, indent=1)
