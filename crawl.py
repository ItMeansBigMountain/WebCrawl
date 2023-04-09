import os

# create project dir
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else: print("DIR ALREADY EXISTS!")





create_directory("affans-test")