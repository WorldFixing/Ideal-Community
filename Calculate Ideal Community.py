print ("Enter a value for each from 0 to 100")

bnp1 = int (input ("Basic NeedP Water (0-100)"))
bnp2 = int(input ("Basic NeedP Food (0-100)")) 
bnp3 = int (input ("Basic NeedP Shelter (0-100)"))
bnp4 = int (input ("Basic NeedP Energy (0-100)"))
bnp5 = int (input ("Basic NeedP Clothes/Footwear (0-100)"))
bnp6 = int (input ("Basic NeedP Work (0-100)"))
totalbnp = bnp1*4.63/100 +bnp2*9.26/100 +bnp3*4.63/100 + bnp4*6.94/100 + bnp5*9.26/100 + bnp6*11.57/100
print ("Total Basic Needs Primary", totalbnp)
bnp7 = int (input ("Basic NeedS Medical (0-100)"))
bnp8 = int (input ("Basic NeedS Consensus (0-100)"))
bnp9 = int (input ("Basic NeedS Transportation (0-100)"))
bnp10 = int (input ("Basic NeedS Education (0-100)"))
bnp11 = int (input ("Basic NeedS Safety/Security (0-100)"))
bnp12 = int (input ("Basic NeedS Waste Processing (0-100)"))
bnp13 = int (input ("Basic NeedS Household Items (0-100)"))
bnp14 = int (input ("Basic NeedS Maintenance (0-100)"))
bnp15 = int (input ("Basic NeedS News/Entertainment (0-100)"))
bnp16 = int (input ("Basic NeedS Raw Materials (0-100)"))
totalbns = bnp7 *4.63/100 + bnp8 *4.63/100 + bnp9 *4.63/100 + bnp10 *4.63/100 + bnp11 *4.63/100 + bnp12 *4.63/100 + bnp13 *4.63/100 + bnp14 *4.63/100 + bnp15 *4.63/100 +bnp16 * 4.63/100
print ("Total Basic Needs Secondary ", totalbns)
bnp17 = int (input ("Additional Leaderless (0-100)"))
bnp18 = int (input ("Additional Seed Saving (0-100)"))
bnp19 = int (input ("Additional Population(Adults) (#)"))
bnp20 = int (input ("Additional Population(Children) (#)"))
bnp21 = int (input ("Additional Workforce population (#)"))
bnp22 = int (input ("Additional Total Land  (ha's)"))
bnp23 = str (input ("Additional Country (code(2))"))
bnp24 = int (input ("Additional Happiness (0-100)"))

bnpLeaders = bnp17*.93/100
#print ("Leaders ",bnpLeaders)
bnpSeeds = bnp18 * .93/100
#print ("Seeds ",bnpSeeds)


  
bnpPOP = .93
if (bnp19+bnp20)<= 1000 :
  bnpPOP = (bnp19+bnp20)/1000 *.93
else:
  bnpPOP = 1000/(bnp19+bnp20) *.93

#print ("Population ",bnpPOP)

bnpWrkForce= .93
if (bnp21)<= 430 :
  bnpWrkForce = bnp21/430 *.93
else:
  bnpWrkForce = 430/bnp21 *.93

#print ("Workforce ",bnpWrkForce)

bnpHamlets= .93
if (bnp19 + bnp20)/200<= 5 :
  bnpHamlets = ((bnp19+bnp20)/200)/5 *.93
else:
  bnpHamlets = 5/((bnp19+bnp20)/200) *.93

#print ("# Hamlets ",bnpHamlets)


bnpLand= .93
if (bnp22)<= 100 :
  bnpLand = bnp22/100 *.93
else:
  bnpLand = 100/bnp22 *.93

#print ("Land size ",bnpLand)

bnp23INT = .93
if bnp23== "SG" or bnp23== "MO" or bnp23 == "MC" :
  bnp23INT = 0
  print ("warning, country: SG, MO, & MC not Sustainable")


#print ("Country ",bnp23INT)

bnpHappiness = bnp24 * .93/100
#print ("Happiness ",bnpHappiness)







#print ("Primary Needs",bnp1,bnp2,bnp3,bnp4,bnp5,bnp6)
#print ("Secondary Needs",bnp7,bnp8,bnp9,bnp10,bnp11,bnp12,bnp13,bnp14,bnp15,bnp16)
#print ("Additional",bnp17,bnp18,bnp19,bnp20,bnp21,bnp22,bnp23,bnp24)

 
totalbna =  bnp17 *.93/100 + bnp18 *.93/100 + bnpPOP + bnpWrkForce +bnpHamlets + bnpLand + bnp23INT + bnpHappiness 



print ("Total Additional:",totalbna)

Overall = totalbnp + totalbns + totalbna
print ("Overall total ",Overall)
