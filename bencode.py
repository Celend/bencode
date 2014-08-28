#
__data = bytes();
s = 0;
e = 0;
l = 0;
def encode(x):
    if type(x) == int:
        return 'i'.encode() + str(x).encode() + 'e'.encode();
    elif type(x) == str:
        x = x.encode('utf-8');
        return (str(len(x)) + ':').encode('ascii') + x;
    elif type(x) == dict:
        keys = list(x.keys());
        keys.sort();
        end = 'd'.encode();
        for i in keys:
            if type(i) == str:
                end += encode(i);
            else:
                raise TypeError("the kay must be str for dict.");
            end += encode(x[i]);
        end += 'e'.encode();
        return end;
    elif type(x) == list:
        end = 'l'.encode();
        for i in x:
            end += encode(i);
        end += 'e'.encode();
        return end;
    raise TypeError('the arg data type is not support for bencode.');

def decode(x = None):
    global __data, s, e, l;
    if type(x) != bytes and x != None:
        raise TypeError("To decode the data type must be bytes.")
    elif x != None:
        e = 0;
        s = 0;
        l = 0;
        __data = x;
        l = len(__data);
    #dict
    if __data[s] == 100:
        s += 1;
        e += 1;
        d = {};
        while s < l-1:
            if __data[s] not in range(48, 58):
                break;
                #raise RuntimeError("the dict key must be str.");
            key = decode();
            value = decode();
            d.update({key:value});
        s += 1;
        return d;
    #int
    elif __data[s] == 105:
        temp = s + 1;
        key = '';
        while __data[temp] in range(48, 58):
            key += str(__data[temp]-48);
            temp += 1;
        s += len(key) + 2;
        return int(key);
    #string
    elif __data[s] in range(48, 58):
        temp = s;
        key  = '';
        while __data[temp] in range(48, 58):
            key += str(__data[temp]-48);
            temp += 1;
        temp += 1;
        key = __data[temp:temp+int(key)];
        s = len(key)+temp;
        try:
            return key.decode();
        except:
            return key;
    #list
    elif __data[s] == 108:
        li = [];
        s += 1;
        while s < l:
            if __data[s] == 101:
                s += 1;
                break;
            li.append(decode());
        return li;
    
    
    
        



    
    
    
    
