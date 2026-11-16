"""Модуль для обработки кадров Modbus."""
def parse_frame(frame):
    return frame[0], frame[1], frame[2:-2]

def filter_known_slaves(slave_id, allowed_set):
    return slave_id in allowed_set

def format_telemetry_dict(device_id, reg_dict):
    return {'id': device_id, 'regs': reg_dict}

if __name__ == '__main__':
    print(parse_frame([5, 3, 0, 100, 0, 2, 180, 22]))