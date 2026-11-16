import sys
from variant4_mod import parse_frame, filter_known_slaves, format_telemetry_dict

target = int(sys.argv[1]) if len(sys.argv) > 1 else 5

frame = [5, 3, 0, 100, 0, 2, 180, 22]
allowed = {1, 3, 5, 12}

dev_id, func, data = parse_frame(frame)
ok = filter_known_slaves(dev_id, allowed)

print(f"Устройство: {dev_id}, функция: {func}, данные: {data}")
print(f"Доступ: {'да' if ok else 'нет'}")
print(f"Телеметрия: {format_telemetry_dict(dev_id, {'reg0': 100, 'status': 'OK'})}")

if target == dev_id:
    print(f"ID {target} совпал с кадром")
else:
    print(f"ID {target} не совпал (в кадре {dev_id})")