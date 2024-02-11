from hashlib import md5


def hash_pwd(initial: str):
    bytes_obj = initial.encode("utf-8")
    return md5(bytes_obj).hexdigest()


if __name__ == '__main__':
    print(hash_pwd("sad"))
