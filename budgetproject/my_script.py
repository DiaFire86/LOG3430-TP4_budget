import os

badHash = "bad_commit_hash" 
goodHash = "good_commit_hash" 

os.system(f"git bisect start {badHash} {goodHash}")
os.system("git bisect run pytest")