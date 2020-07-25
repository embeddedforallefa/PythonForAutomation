import sys
from bsedata.bse import BSE
import pandas as pd
import pprint

b = BSE()
b.updateScripCodes()

#store the scripts codes in BseScripCodes.txt
print(b.getScripCodes(), file=open('BseScripCodes.txt','wt'))

#convert scripts codes from BseScripCodes.txt to BseScripCodes.xlsx
df = pd.DataFrame(data=b.getScripCodes(), index=[0])
df = (df.T)
df.to_excel('BseScripCodes.xlsx')
