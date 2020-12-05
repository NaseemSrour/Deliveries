# Utlity functions:

def convertToBinaryData(filepath):
    # Convert digital data to binary format
    with open(filepath, 'rb') as file:
        binaryData = file.read()
    return binaryData

def writeBinaryFile(dst_path, data):
    # Convert binary data to proper format and write it on Hard Disk
    with open(dst_path, 'wb') as file:
        file.write(data)

def test():
    # Double slash your (absolute) path, the \U is some unicode character.
    mydata = convertToBinaryData('C:\\Users\\Naseem\\Desktop\\Untitled.png')
    writeBinaryFile('C:\\Users\\Naseem\\Desktop\\Untitled_3.png', mydata)
