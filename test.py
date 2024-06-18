import chardet

with open('.env', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result)
