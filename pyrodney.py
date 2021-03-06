# pyrodney.py -- Rodney Lewis (http://www.VoteForRodneyLewis.com)
# Free for most uses. Please distribute with my name and URL prominently cited

import zlib


def ap_headline_caps(headline):
    r"""
    Returns string with proper Associated Press headline capitalization
    >>> APHeadlineCaps( "Kids In The Hall" )
    Kids in the Hall
    >>> APHeadlineCaps( "Strangers With Candy" )
    Strangers with Candy
    >>> APHeadlineCaps( "the lost boys" )
    The Lost Boys
    >>> APHeadlineCaps( "Where I'm from" )
    Where I'm From
    >>> APHeadlineCaps( "fALLiNG aWAY fROM mE" )
    Falling Away from Me
    """
    toLower = ['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'from', 'in',
               'nor', 'of', 'off', 'on', 'so', 'the', 'to', 'with', 'yet']
    headline = headline.split('')  # split string into list of words

    for index, item in enumerate(headline):
        if item.lower() in toLower:  # if this a word we want in lowercase...
            headline[index] = item.lower()  # make sure it's lowercase
        else:
            headline[index] = item.capitalize()  # or capitaize it

    headline[0] = headline[0].capitalize()  # captalize first and last words
    lastWordIndex = len(headline) - 1
    headline[lastWordIndex] = headline[lastWordIndex].capitalize()

    return ' '.join(headline)  # convert list back to string


def compare_signs(num1, num2):
    r"""
    Returns True if signs match
    >>> CompareSigns(-1, -1)
    True
    >>> CompareSigns(-1, 0)
    False
    >>> CompareSigns(-1, 1)
    False
    >>> CompareSigns(0, -1)
    False
    >>> CompareSigns(0, 0)
    True
    >>> CompareSigns(0, 1)
    True
    >>> CompareSigns(1, -1)
    False
    >>> CompareSigns(1, 0)
    True
    >>> CompareSigns(1, 1)
    True
    """
    if num1 < 0 and num2 < 0 or num1 >= 0 and num2 >= 0:
        return True
    else:
        return False


def file_checksum(filename):
    """Returns checksum for any arbitrarily-lengthed file"""
    checksumTally = 0

    with open(filename, 'rb') as fileHandle:
        while True:
            chunk = fileHandle.read(102400)
            if chunk != '':
                checksumTally = checksumTally + zlib.crc32(chunk)
            else:
                break

    checksum = zlib.crc32(str(checksumTally))

    return checksum


def listify-textfile(filename):
    """Returns a list made from the lines of the text file passed it"""
    inputFile = open(filename, 'r')
    inputData = inputFile.read()  # read file as one big chunk
    inputFile.close()
    inputData = inputData.splitlines()  # split file into list of lines
    return inputData