def default_handler(info):
    if info[:1] == b'\x00':
        return info[1:].decode('iso-8859-1')
    elif info[:1] == b'\x01' and info[1:3] == b'\xff\xfe':
        return info[3:].decode('utf-16')
    elif info[:1] == b'\x01' and info[1:3] == b'\xfe\xff':
        temp = bytearray(info[3:])
        temp.reverse()
        return bytes(temp).decode('utf-16')

def COMM_handler(info):
    encoding = 'iso-8859-1'
    if info[:1] == b'\x01':
        encoding = 'utf-16'
    language = info[1:4]
    return info[10:].decode(encoding)


def APIC_handler(info):
    return 'this is picture'

tag_to_handler = {
    'COMM': COMM_handler,
    'APIC': APIC_handler,
}
