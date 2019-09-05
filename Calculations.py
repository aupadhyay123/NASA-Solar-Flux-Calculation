#Atharva Upadhyay
#NASA Ames

import csv
import math

def main():
    fileIn = open("NASA Absorption Coeff. of Water.csv", "r")
    solarConstant = 1366
    wavelengths = []
    absorptions = []
    depth100 = []
    depth0 = []
    depth10 = []
    with open('NASA Absorption Coeff. of Water.csv') as csvfile:
        fileIn = csv.reader(csvfile, delimiter=',')
        for row in fileIn:
            wavelength = float(row[0])
            absorption = float(row[1])
            wavelengths.append(wavelength)
            absorptions.append(absorption)
    solarFlux0(wavelengths, absorptions, depth0)
    solarFlux10(wavelengths, absorptions, depth10)
    solarFlux100(wavelengths, absorptions, depth100)
    writeToFile(depth0, depth10, depth100)

def solarFlux0(wavelengths,absorptions,depth0):
    counter = 0
    for i in absorptions:
        x = wavelengths[counter] * (math.exp(-1*(i * 0)))
        counter += 1
        depth0.append(x)
def solarFlux10(wavelengths, absorptions,depth10):
    counter = 0
    for i in absorptions:
        x = wavelengths[counter] * (math.exp(-1*(i * 10)))
        counter += 1
        depth10.append(x)
def solarFlux100(wavelengths, absorptions,depth100):
    counter = 0
    for i in absorptions:
        x = wavelengths[counter] * (math.exp(-1*(i * 100)))
        counter += 1
        depth100.append(x)
def writeToFile(depth0, depth10, depth100 ):
    with open('NASA Absorption Coeff. of Water.csv', 'r') as csvinput:
        fileIn = csv.reader(csvinput, delimiter = ',')
        data = []
        counter = 0
        for row in fileIn:
            row.append(depth0[counter])
            row.append(depth10[counter])
            row.append(depth100[counter])
            print(row)
            data.append(row)
            counter += 1
    with open('NASA Absorption Coeff. of Water.csv', 'w') as csvoutput:
        fileOut = csv.writer(csvoutput, lineterminator='\n')
        fileOut.writerows(data)

main()