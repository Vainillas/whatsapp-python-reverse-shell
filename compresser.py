import zlib
import base64


def compress(data):
    compressed_data = zlib.compress(data.encode())
    return base64.b64encode(compressed_data).decode()


def openfiletocompress(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def writetofile(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"File {filename} has been written")


#main function
def main():
    data = openfiletocompress("pythonreverseshell.py")
    encoded_data = compress(data)
    writetofile(encoded_data, "encodedRS.py")

main()
