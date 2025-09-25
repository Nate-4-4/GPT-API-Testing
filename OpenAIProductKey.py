def readKeyFromFile(filename : str) -> str:
    with open(filename) as file:
        key = file.readline()
        key = key.strip()
        return key