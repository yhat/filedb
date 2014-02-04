from errno import ENOENT
from stat import S_IFDIR, S_IFREG
import time
import json

from fuse import FuseOSError, Operations


class FileDB(Operations):
    def __init__(self, db, collection):
        self.db = db
        self.collection = self.db[collection]

    def dump_db(self):
        collection = []
        keys = {
            "_id": 1,
            "username": 1,
            "apikey": 1,
            "password": 1
        }
        for thing in self.collection.find({}, keys):
            thing['_id'] = str(thing['_id'])
            collection.append(thing)
        return json.dumps(collection) + '\n'

    def getattr(self, path, fh=None):
        if path == '/':
            st = dict(st_mode=(S_IFDIR | 0755), st_nlink=2)
        elif path == '/db':
            data = self.dump_db()
            size = len(data)
            st = dict(st_mode=(S_IFREG | 0444), st_size=size)
        else:
            raise FuseOSError(ENOENT)
        st['st_ctime'] = st['st_mtime'] = st['st_atime'] = time.time()
        return st

    def read(self, path, size, offset, fh):
        if path == '/db':
            data = self.dump_db()
            return data[offset:offset+size]

        raise RuntimeError('unexpected path: %r' % path)

    def readdir(self, path, fh):
        return ['.', '..', 'db']

    # Disable unused operations:
    access = None
    flush = None
    getxattr = None
    listxattr = None
    open = None
    opendir = None
    release = None
    releasedir = None
    statfs = None

if __name__=="__main__":
    pass
