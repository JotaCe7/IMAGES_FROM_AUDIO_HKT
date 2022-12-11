

def read_file(filename, chunk_size=5242880):
    '''
    Reads an audio file
    '''
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data