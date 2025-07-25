import random

def compute_checksum(data):
    checksum = sum(ord(ch) for ch in data) % 65535
    return format(checksum, '04x')

def simulate_transmission(data, error_rate):
    transmission_log = []
    for i, ch in enumerate(data):
        transmitted = ch
        if random.random() < error_rate:
            transmitted = chr(ord(ch) ^ 0b00000001)  # Flip last bit
        status = 'OK' if transmitted == ch else 'ERROR'
        transmission_log.append({'index': i, 'original': ch, 'transmitted': transmitted, 'status': status})
    return transmission_log
