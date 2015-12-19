##############################################################################
# Counts the number of programming bytes in a hex or s19 file
# Inputs: File, Size Limit (optional)
# Outputs: Byte count, % used of size limit (if given)
##############################################################################

def CountBytes (InputFile, nSizeLimit = 0):

    nByteCount = 0

    try:
        FileToRead = open (InputFile, 'r')

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

    if nSizeLimit != 0:
        print ("Percent used: " + str (float (100 * nByteCount / nSizeLimit)))

    return
