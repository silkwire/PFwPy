import os

def rename_files():
  list_files = os.listdir(r"C:\OOP\files")
  os.chdir(r"C:\OOP\files")
  
  for each in list_files:
    os.rename(each, each.translate(None, "0123456789")

rename_files()
