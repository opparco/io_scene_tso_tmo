from os import path
import re

rotation_nodes = set()
translation_nodes = set()

filename = path.join(path.dirname(__file__), "resources/turned-nodes.txt")

with open(filename) as f:
	for line in f:
		line = re.sub('\n', '', line)  # chomp
		name, r, t = line.split('\t')
		if r == 'R':
			# print('R {}'.format(name))
			rotation_nodes.add(name)
		if t == 'T':
			# print('T {}'.format(name))
			translation_nodes.add(name)

def in_rotation(name):
	return name in rotation_nodes

def in_translation(name):
	return name in translation_nodes

if __name__ == "__main__":
	print(in_rotation('Head'))
	print(in_translation('Head'))
	print(in_rotation('face_oya'))
	print(in_translation('face_oya'))
