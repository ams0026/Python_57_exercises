#stateparsing.py

USPO, ISOGEOCODE = None, None

STalabama = {'alabama', 'ala','bama', 'us-al', 'al'}
STalaska = {'alaska', 'us-ak', 'ak'}
STarkansas = {'arkansas', 'ark', 'us-ar', 'ar'}
STarizona = {'arizona', 'ariz', 'us-az', 'az'}

STcalifornia = {'california', 'ca', 'cali'}
STcolorado = {'colorado', 'co', 'colo'}

state = input("What state are we looking up? ")

if state.lower() in STalabama:
    USPO = "AL"
    ISOGEOCODE = "US-AL"
if state.lower() in STalaska:
    USPO = "AK"
    ISOGEOCODE = "US-AK"
if state.lower() in STarizona:
    USPO = "AZ"
    ISOGEOCODE = "US-AZ"
if state.lower() in STarkansas:
    USPO = "AR"
    ISOGEOCODE = "US-AR"


if state.lower() in STcalifornia:
    USPO = "CA"
    ISOGEOCODE = "US-CA"
if state.lower() in STcolorado:
    USPO = "CO"
    ISOGEOCODE = "US-CO"

if USPO == None:
    print ("I'm sorry, I don't recognize that state. ")
else: 
    print ("The postal abbreviation is " + USPO + " \nand the ISO-3166 abbreviation is " + ISOGEOCODE)
