def calculate_turbine_fuel(p_start=10, p_end=100, p_step=10):
    total_fuel = 0.0
    print(f"{'Нагрузка (МВт)':>15} | {'q (кг/кВт·ч)':>15} | {'Расход (кг)':>15}")
    for p in range(p_start, p_end, p_step):
        if p < 40:
            q = 0.25      # при P < 40 q = 0.25
        else:
            q = 0.21      # при P >= 40 q = 0.21
        fuel = p * 1000 * q   # переход из МВт в кВт
        total_fuel = total_fuel + fuel
        print(f"{p:>15} | {q:>15} | {fuel:>15}")
    return total_fuel          # возвращение суммарного расхода топлива

if __name__ == '__main__':
    print("1. Стандартный диапазон (10..100, шаг 10)")
    result1 = calculate_turbine_fuel(10, 100, 10)
    print(f"Суммарный расход топлива: {result1:.1f} кг\n")

    print("2. Диапазон с переходом через 40 МВт (20..60, шаг 10)")
    result2 = calculate_turbine_fuel(20, 60, 10)
    print(f"Суммарный расход топлива: {result2:.1f} кг\n")
