#The purpose of this script is to calculate the Hamming distance between two sets of 6 bp sequencing barcodes
# I am writing this script to help David Chow pick tw0 9 bp barcode to sequence two bacterial genomes
# These barcodes need to be different from the 6 bp barcodes from the Bloom lab that we are hoping on a lane with
# To do this, I will write a program that takes the Shou lab 9 bp barcodes, takes the first 6 bp, and calculates the minimum hamming distance from all
# of the Bloom lab 6 bp barcodes. I will only retain barcodes that have a minimum hamming distance of N, which will be specified by the user in the 
# command line

#import libraries needed
import sys
import os
import argparse

#define parsing options
parser = argparse.ArgumentParser()
parser.add_argument('-testbarcodes', type=argparse.FileType('r')) # barcodes from shou lab
parser.add_argument('-refbarcodes', type=argparse.FileType('r')) # barcodes from shou lab
parser.add_argument('-dir', dest='dir')

args = parser.parse_args()

# get the path where the data are stored. will be used with other strings later
path=args.dir

ll=args.testbarcodes.readlines() # read shou lab file, build list of barcodes

testbarcodeslist=[]

for line in ll:
	line=line.rstrip('\n')
	line=line.rstrip('\r')
	line = line.split(',')
	#print line
	if line[1] != 'Seq':
		testbarcodeslist.append(line[1])


	
ll=args.refbarcodes.readlines() #  read bloom lab file, build list of barcodes

refbarcodeslist=[]

for line in ll:
	line=line.rstrip('\n')
	line=line.rstrip('\r')
	line = line.split(',')
	#print line
	if line[1] != 'Seq':
		refbarcodeslist.append(line[1])

min_Ham={} # dictionary to hold minimum hamming distance of test barcodes from ref barcodes

for barcode in testbarcodeslist:
	#print barcode
	if barcode not in min_Ham.keys(): # if barcode hasn't been checked, initilze to hamming distance of 6 (totally different barcode at all sites)
		min_Ham[barcode.lower()]=6
	# compare first 6 bp of barcodes 
	for refbarcode in refbarcodeslist:
		hammdist=0
		#print refbarcode
		barcode=barcode.lower()
		i = 0
		while i <6:
			if barcode[i] != refbarcode[i]:
				hammdist+=1
			i+=1
		if hammdist < min_Ham[barcode]:
			min_Ham[barcode]=hammdist


for barcode in min_Ham.keys():
	if min_Ham[barcode] > 2:
			print barcode.upper(), min_Ham[barcode]