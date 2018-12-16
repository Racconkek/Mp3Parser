def default_handler(info):
    if info[:1] == b'\x00':
        return info[1:].decode('iso-8859-1')
    elif info[:1] == b'\x01' and info[1:3] == b'\xff\xfe':
        return info[3:].decode('utf-16')
    elif info[:1] == b'\x01' and info[1:3] == b'\xfe\xff':
        temp = bytearray(info[3:])
        temp.reverse()
        return bytes(temp).decode('utf-16')
    else:
        return info.decode('iso-8859-1')

def COMM_handler(info):
    encoding = 'iso-8859-1'
    if info[:1] == b'\x01':
        end = info.find(b'\x00')
        if info[end + 2: end + 4] == b'\xff\xfe':
            return info[end + 4:].decode('utf-16-le')
        elif info[end + 2: end + 4] == b'\xfe\xff':
            return info[end + 4:].decode('utf-16-be')
    end = info[1:].find(b'\x00')
    return info[end + 1:].decode(encoding)


def APIC_handler(info):
    return 'this is picture'

def POPM_handler(info):
    email_end =  info.find(b'\x00')
    email = info[:email_end].decode('iso-8859-1')
    rating = int.from_bytes(info[email_end + 1: email_end + 2], byteorder='big')
    counter = int.from_bytes(info[email_end + 2:], byteorder='big')
    return "Email to user: " + email + ", Rating: " + str(rating) + ", Counter: " + str(counter)


def PRIV_handler(info):
    id_end = info.find(b'\x00')
    owner_id = info[:id_end].decode('iso-8859-1')
    data = info[id_end + 1:].decode('iso-8859-1')
    return "Owner ID: " + owner_id + ", Data: " + data

tag_to_handler = {
    'COMM': COMM_handler,
    'APIC': APIC_handler,
    'POPM': POPM_handler,
    'PRIV': PRIV_handler
}
