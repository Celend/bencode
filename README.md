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
