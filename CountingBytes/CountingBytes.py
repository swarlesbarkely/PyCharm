##############################################################################
# Counts the number of programming bytes in a hex or s19 file
# Inputs: File, Size Limit (optional)
# Outputs: Byte count, % used of size limit (if given)
# TEST COMMENT
##############################################################################

import parser

def CountBytes (sInputFile, SizeLimit = ''):

    nByteCount = 0

    try:
        FileToRead = open (sInputFile, 'r')

    except OSError:
        print ("Error opening file!")
        return

    sLine = FileToRead.readline ()

    if sLine[0] == ':':
        FileFormat = 'hex'

    elif sLine[0] == 'S':
        FileFormat = 's19'

    else:
        # Unknown file format
        print ("Unknown file format!")
        return

    if FileFormat == 'hex':
        # Read until we get an empty string (this does not include newlines)
        while not sLine == '':
            if sLine[7:9] == '00':
                # This line contains data --> add the byte count to our counter
                nByteCount += int (sLine[1:3], 16)

            sLine = FileToRead.readline ()

    elif FileFormat == 's19':
        # Read until we get an empty string (this does not include newlines)
        while not sLine == '':
            if sLine[1:2] == '1' or sLine[1:2] == '2' or sLine[1:2] == '3':
                # This line contains data --> add the byte count to our counter
                nByteCount += int (sLine[2:4], 16)

            sLine = FileToRead.readline ()

    # Print the results
    print ("Number of data bytes: " + str (nByteCount))

    if not SizeLimit == '':
        # Check for any suffixes on the size limit
        SizeLimit = str (SizeLimit).replace ('k', '* 1024')
        SizeLimit = str (SizeLimit).replace ('M', '* 1024**2')
        SizeLimit = str (SizeLimit).replace ('G', '* 1024**4')
        SizeLimit = eval (parser.expr(SizeLimit).compile())
        print ("Percent used: " + str (float (100 * nByteCount / SizeLimit)))

    return
