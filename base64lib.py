import base64



def encode1(data):
    return base64.b64encode(data.encode("utf-8"))

def decode1(data):
    return base64.b64decode(data)

def encode2(data):
    return base64.b32encode(data.encode("utf-8"))

def decode2(data):
    return base64.b32decode(data.decode("utf-8"))