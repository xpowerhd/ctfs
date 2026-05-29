f = open("/home/georgi/Desktop/CTFs/Crypto Failures/sec_cookie.txt")
data = f.read()
chunks = [data[i:i+13] for i in range(0, len(data), 13)]
for chunk in chunks:
    print(chunk)
