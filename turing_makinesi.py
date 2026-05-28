def turing_simulator(binary_input):
    tape = list(binary_input)
    head_position = 0
    state = "q0"
    print(f"Başlangıç Bandı: {''.join(tape)}")
    print("-" * 50)
    while head_position < len(tape):
        current_symbol = tape[head_position]
        print(f"Durum: {state} | Okunan: {current_symbol} | Bant: {''.join(tape)}")
        if state == "q0":
            if current_symbol == '*':
                state = "q1"
                head_position += 1
            else:
                head_position += 1
        elif state == "q1":
            if current_symbol == '=':
                state = "q2"
                print("İşlem tamamlandı, sonuç yazıldı.")
                break
            else:
                head_position += 1
    print("-" * 50)
    print("Simülasyon Bitti.")
girdi = input("Lütfen işleminizi girin (Örn: 11*10=): ")
if all(c in '01*= ' for c in girdi):
    turing_simulator(girdi)
else:
    print("Hata: Sadece 0, 1, * ve = karakterlerini kullanın!")