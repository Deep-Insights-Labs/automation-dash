 
import sys


def show_usg():
    print('Usage: read_file <file-name>')

def main(argv):
# Print total number of arguments
    tot_args = len(sys.argv)

    if tot_args != 2 :
        print ('Invalid Arguments')
        show_usg()
        return -1
    
    print ('Total number of arguments:', format(len(sys.argv)))
    
    # Print all arguments
    print ('Argument List:', str(sys.argv))
    
    # Print arguments one by one
    print ('First argument:',  str(sys.argv[0]))
    print ('Second argument:',  str(sys.argv[1]))
 
    # open txt file in read mode
    file1 = open(str(sys.argv[1]), "r")

    # Read all contents of text file in a string s

    str_file = file1.read()

    # show the contents from string s

    print(str_file)

    # close the text file
    file1.close()

if __name__ == '__main__':
    main(sys.argv[1:])
    
