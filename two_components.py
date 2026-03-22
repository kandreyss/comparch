def get_min_bytes(num):
    """Определяет минимальное количество байт для представления числа."""
    if -128 <= num <= 127:
        return 1
    elif -32768 <= num <= 32767:
        return 2
    elif -2147483648 <= num <= 2147483647:
        return 4
    else:
        return 8
 
 
def to_twos_complement(num):
    """Преобразует число в двоичный и шестнадцатеричный дополнительный код."""
    bytes_count = get_min_bytes(num)
    bits = bytes_count * 8
    
    # Получаем двоичное представление
    if num >= 0:
        binary = format(num, f'0{bits}b')
        hex_val = format(num, f'0{bytes_count * 2}x')
    else:
        twos_comp = (1 << bits) + num
        binary = format(twos_comp, f'0{bits}b')
        hex_val = format(twos_comp, f'0{bytes_count * 2}x')
    
    return num, bytes_count, binary, hex_val
 
 
def main():
    while True:
        try:
            user_input = input("Введите число: ").strip()
            
            if user_input.lower() == 'выход':
                break
            
            num = int(user_input)
            number, bytes_count, binary, hex_code = to_twos_complement(num)
            
            print(f"Число:           {number}")
            print(f"Байт:            {bytes_count}")
            print(f"Двоичный код:    {binary}")
            print(f"Шестнадцатеричный: 0x{hex_code.upper()}")
            print()
        
        except ValueError:
            print("Ошибка: введите корректное целое число\n")
        except KeyboardInterrupt:
            break
 
 
if __name__ == "__main__":
    main()
