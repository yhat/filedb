# filedb
Create a file that pretends to be a MongoDB collection. If you try 
to open the file, it will JSONify the collection and dump it back to you.

## Why?
Because our enterprise database is file based, but our cloud based database
isn't.

## ...no really why?
Files are simpler and don't break. The database operations we need to perform
aren't complicated and don't require high performance. By using files there
isn't a database that can fail. There's the added benefit that if customers want
to use different types of databases for distributed systems, we can plug into 
any of them using a `filedb` (we just have to make something that dumps out JSON
.

## Quickstart

#### Install FUSE
Make sure you have [FUSE](http://fuse.sourceforge.net/) installed.

- [FUSE for OSX](http://osxfuse.github.io/)
- Ubuntu: `sudo apt-get install g++ libfuse-dev`

#### Install filedb
```bash
$ pip install filedb
```

### Running via python
```bash
$ filedb /tmp/tutorial/mnt/ mongodb://localhost:27017/test people
```

### Upstart job
```bash
cp -R overlay/* /
sudo start filedb
```
