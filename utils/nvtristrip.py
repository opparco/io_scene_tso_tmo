#!/usr/bin/env python

import os
import subprocess

# 前提: programはPathの通ったフォルダに置いている
program = "NvTriStripper-cli.exe"

def stripify(triangles, stitchstrips=False):
	args = [program]
	proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
	for triangle in triangles:
		proc.stdin.write(' '.join(map(str, triangle)))
		proc.stdin.write(' ')
	proc.stdin.write('-1\n')
	proc.stdin.flush()

	strip_count = int(proc.stdout.readline())
	if strip_count < 1:
		raise Exception("NvTriStrip returned 0 strips. Aborting")
	strip_type = int(proc.stdout.readline())
	length = int(proc.stdout.readline())
	return [map(int, proc.stdout.readline().split())]

if __name__ == "__main__":
	triangles = [(0, 1, 2), (2, 1, 4)]
	strip, = stripify(triangles)
	print(tuple(strip))
