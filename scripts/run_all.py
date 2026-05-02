import os

# runs all scripts in scripts/
print("running cleaning.py...")
os.system("scripts/cleaning.py")
print("running merging.py...")
os.system("scripts/merging.py")
print("running analysis.py...")
os.system("scripts/analysis.py")
print("full workflow successfully executed")