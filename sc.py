from os import remove
from sys import argv
import httpx
print(f"This Version is {'1.1'}")
if httpx.get('https://raw.githubusercontent.com/probuilder9/lynxlovers87/main/versi.txt').text != '1.1':
    with open('sc.py', 'w') as file1:
        file1.write(httpx.get('https://raw.githubusercontent.com/probuilder9/lynxlovers87/main/sc.py').text)
    print(f"Updating Tools CPM Contact @DPR_LynX Version {httpx.get('https://raw.githubusercontent.com/probuilder9/lynxlovers87/main/versi.txt').text}")
    remove(argv[0])
    exit()
