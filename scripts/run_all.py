import os

# runs all scripts in the scripts folder

print("running cleaning.py...")
os.system("python scripts/cleaning.py")

print("running merging.py...")
os.system("python scripts/merging.py")

print("running analysis.py...")
os.system("python scripts/analysis.py")

print("full workflow successfully executed")