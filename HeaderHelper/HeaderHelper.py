import datetime

##############################################################################
# Creates main function header for .h files and smaller headers for .c files
# Input:	None
# Return:	None
##############################################################################
def CreateFunctionHeader():

    # Get module description
    sFunctionDescription = input ('Description: If more than one line is needed, end each line with a comma\n')

    while sFunctionDescription.endswith(','):
        sFunctionDescription = sFunctionDescription.rstrip(',')
        sFunctionDescription += '\n*\t\t\t\t' + input()

    # Get input arguments

    print('\n************************ Arguments ************************\n'
          'Enter the values name followed by a short description.\n'
          'If there is another argument, end your description with a comma.')

    asArguments = list()

    x = 0
    while True:
        sTemp = str(x+1) + ': '
        asArguments.append(input (sTemp))
        
        if not asArguments[x].endswith(','):
            # End of arguments
            break
        else:
            # Strip off comma
            asArguments[x] = asArguments[x].rstrip(',')
        
        x += 1

    # Get return values

    print('\n************************ Returns ************************\n'
          'Enter the values name followed by a short description.\n'
          'If there is another return value, end your description with a comma.')

    asReturns = list()

    x = 0
    while True:
        sTemp = str(x+1) + ': '
        asReturns.append(input (sTemp))
        
        if not asReturns[x].endswith(','):
            # End of returns
            break
        else:
            # Strip off comma
            asReturns[x] = asReturns[x].rstrip(',')
        x += 1

    # Get dev info
    sInitials = input('\nInitials: ').upper()

    sChanges = "Initial revision"

    # Format date
    sToday = datetime.date.today().strftime('%m/%d/%Y')

    print('')
    print('/**************************************************************************')
    print('* DESCRIPTION:\t' + sFunctionDescription)
          
    print('*\n* INPUTS:\t\t' + asArguments[0])
    for each in range(1,len(asArguments)):
        if each == 0:
          continue
        else:
          print ('*\t\t\t\t' + asArguments[each])

    print('*\n* RETURNS:\t\t' + asReturns[0])
    for each in range(1,len(asReturns)):
        if each == 0:
          continue
        else:
          print ('*\t\t\t\t' + asReturns[each])
    print('**************************************************************************/')

    # Print mini header
    print('')
    print('/**************************************************************************')
    print('* HISTORY:\t' + sToday + ' ' + sInitials + ' ' + sChanges)
    print('**************************************************************************/')
    return


##############################################################################
# Creates .h style file header
# Input:	Path where output file should be placed (optional -- will be printed on screen otherwise)
# Return:	None
##############################################################################
def CreateFileHeader (sFilePath = 'null'):

    # Get file name
    sFileName = input ('File Name: ')
    if not sFileName.endswith('.h'):
        sFileName += '.h'

    # Create include guards
    sIncludeGuardName = '_' + sFileName.upper().replace('.','_') + '_'

    # Get module description
    sDescription = input ('Description: If more than one line is needed, end each line with a comma\n')

    while sDescription.endswith(','):
        sDescription = sDescription.rstrip(',')
        sDescription += '\n*\t\t\t\t' + input()

    # Get author
    sAuthor = input ('Author: ').title()

    # Format date
    sToday = datetime.date.today().strftime('%m/%d/%Y')

    if not sFilePath == 'null':
        try:
            # Make sure file ends with /
            if not sFilePath.endswith('/'):
                sFilePath += '/'

            File = open(sFilePath + sFileName, 'x')

            # Print header
            File.write('/**************************************************************************')
            File.write('\n')
            File.write('* DESCRIPTION:\t' + sDescription)
            File.write('\n')
            File.write('*')
            File.write('\n')
            File.write('* AUTHOR:\t\t' + sAuthor)
            File.write('\n')
            File.write('*')
            File.write('\n')
            File.write('* CHANGELOG:\t' + sToday + ' ' + sAuthor + ' | Initial revision')
            File.write('\n')
            File.write('*')
            File.write('\n')
            File.write('**************************************************************************/')
            File.write('\n')
            File.write('#ifndef ' + sIncludeGuardName)
            File.write('\n')
            File.write('#define ' + sIncludeGuardName)
            File.write('\n')
            File.write('\n')
            File.write('#endif')
            File.write('\n')

            File.close()

        except OSError:
            # Error opening file
            print ('Error opening file!\nVerify the path is correct and that the file does not already exist')

    else:
        # Print header
        print('/**************************************************************************')
        print('* DESCRIPTION:\t' + sDescription)
        print('*')
        print('* AUTHOR:\t\t' + sAuthor)
        print('*')
        print('* CHANGELOG:\t' + sToday + ' ' + sAuthor + ' | Initial revision')
        print('*')
        print('**************************************************************************/')
        print('#ifndef ' + sIncludeGuardName)
        print('#define ' + sIncludeGuardName)
        print()
        print('#endif')
    return
                  
