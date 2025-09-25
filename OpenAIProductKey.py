def readKeyFromFile(filename : str) -> str:
    try:
        with open(filename) as file:
            key = file.readline()
            key = key.strip()
            return key
    except Exception as e:
        print(f"Failed to load OpenAI Product Key: {e}")
        return None