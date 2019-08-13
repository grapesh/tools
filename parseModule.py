import os, glob, sys

#======================================================================
def getFunctions (pyFile):
    """
    Parses py file and returns the list of detected functions
    """
    functions = []
    with open(pyFile,"r") as f:
        lines = f.readlines()       
    for l in lines:
        if l[0:3] == "def":
            fName = l.replace('(',' ').split()[1]
            functions.append ( fName )
    return functions

#======================================================================
def printFunctions(functions, pyFile, reclevel=0):
    """
    Prints the list of detected functions
    """    
    pIdent = '__'
    for n in range(2*reclevel+1):
        pIdent = pIdent + '__'
    print '\n' + pyFile.split('/')[-1]
    for f in functions:
        print pIdent + ' ' + f + '()'

#======================================================================
def recursive (files, reclevel=0):
    """
    Recursively walks on files and folders                
    """
    for f in files:
        if f.endswith('.py'):
            lst = getFunctions(f)
            printFunctions(lst, f, reclevel)
        if os.path.isdir(f):
            recursive(sorted(glob.glob(f+'/*'), key=os.path.isdir), reclevel=reclevel+1)
    
#======================================================================
if __name__ == "__main__":

    #modulePath='C:/Your/Path/To/Python/Repository/'
    try:
        modulePath = str(sys.argv[1])
    except:
        print 'Use python parseModule.py /path/to/your/module'
        exit()

    print 'Repository: ', modulePath
    files = sorted(glob.glob(modulePath+'/*'), key=os.path.isdir)
    recursive (files)
            
