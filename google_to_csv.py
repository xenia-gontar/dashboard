import os
import requests
import sys

def getGoogleSeet(spreadsheet_id, outDir, outFile):
  
  url = f'LINK'
  response = requests.get(url)
  if response.status_code == 200:
    filepath = os.path.join(outDir, outFile)
    with open(filepath, 'wb') as f:
      f.write(response.content)
      print('CSV file saved to: {}'.format(filepath))    
  else:
    print(f'Error downloading Google Sheet: {response.status_code}')
    sys.exit(1)


##############################################

outDir = os.getcwd()

os.makedirs(outDir, exist_ok = True)
filepath = getGoogleSeet('1234567890', outDir, "text.csv")

sys.exit(0); ## success
