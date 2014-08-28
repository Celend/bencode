bencode
=======

python3 bencode, support multiple encoding and read/write BT torrent file.
this module support multiple data type, include bytes. so you can open a torrent file, unable decoding the data will be return bytes, that you can insert bytes data. auto sorted dictionary key when insert dict.
#####data type
|bencode|Python|
|-------|------|
| int | int |
| str | str |
| list| list|
| dictionary|dict|
| unable decoding| bytes|

#####example
```python
import bencode;
>>> f = open('bt.torrent', 'rb');
>>> bt = bencode.decode(f.read());
>>> f.close
>>> bt.keys()
>>> dict_keys(['info', 'announce-list'])
>>> for i in bt['info']['files']:
    print(i['path']);

['MTKV25.zip']
>>> bt['info']['files'][0]['path'][0] = 'modify.zip';
>>> f = open('bt1.torrent', 'wb');
>>> f.write(bencode.encode(bt));
10537
>>> f.close();
```

or load with `bencode.load(filename)` return object, save with `bencode.save(object, filename)` return boolean;
#####result
only filename has been changed, open with downloader successfully downloaded.  
so i can say this module can fully support torrent file read/write.  
**have BUGs? oh sorry, i don't know(＞﹏＜)**  
**Good Lucky**
