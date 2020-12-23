import tarfile

def tar_extract(filepath):
    tar = tarfile.open(filepath, 'r:gz')
    tar.extractall()

if __name__ == '__main__':
    filepath = 'mini_newsgroups.tar.gz'
    tar_extract(filepath)