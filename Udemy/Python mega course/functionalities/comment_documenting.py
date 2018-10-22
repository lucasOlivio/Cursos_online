r"""
This script creates and empty file
"""
filename="sample.txt"

#create empty file
def create_file():
    """
    def function
    """
    with open(filename,"w") as file:
        file.write("") #writting in empty string
