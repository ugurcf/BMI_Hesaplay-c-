import tkinter as tk

def bmi_hesapla():
    try:
        kilo = float(entry_kilo.get())
        boy_cm = float(entry_boy.get())
        boy_m = boy_cm / 100  # cm'yi metreye çevir
        bmi = kilo / (boy_m ** 2)

        if bmi < 18.5:
            sonuc_text = (
                f"Formül: BMI = Kilo / (Boy (m))²\n"
                f"BMI = {kilo} / ({boy_m:.2f}²)\n"
                f"BMI Değeriniz: {bmi:.2f}\n"
                "Vücut Kitle İndeksiniz: Aşırı Zayıf"
            )
        elif bmi < 25:
            sonuc_text = (
                f"Formül: BMI = Kilo / (Boy (m))²\n"
                f"BMI = {kilo} / ({boy_m:.2f}²)\n"
                f"BMI Değeriniz: {bmi:.2f}\n"
                "Vücut Kitle İndeksiniz: Zayıf"
            )
        elif bmi < 30:
            sonuc_text = (
                f"Formül: BMI = Kilo / (Boy (m))²\n"
                f"BMI = {kilo} / ({boy_m:.2f}²)\n"
                f"BMI Değeriniz: {bmi:.2f}\n"
                "Vücut Kitle İndeksiniz: Kilolu"
            )
        elif bmi < 35:
            sonuc_text = (
                f"Formül: BMI = Kilo / (Boy (m))²\n"
                f"BMI = {kilo} / ({boy_m:.2f}²)\n"
                f"BMI Değeriniz: {bmi:.2f}\n"
                "Vücut Kitle İndeksiniz: Obez"
            )
        else:
            sonuc_text = (
                f"Formül: BMI = Kilo / (Boy (m))²\n"
                f"BMI = {kilo} / ({boy_m:.2f}²)\n"
                f"BMI Değeriniz: {bmi:.2f}\n"
                "Vücut Kitle İndeksiniz: Aşırı Obez"
            )

        sonuc_label.config(text=sonuc_text)
    except ValueError:
        sonuc_label.config(text="Lütfen geçerli bir sayı giriniz. Sayınız "0" olamaz.")

# Ana pencere
window = tk.Tk()
window.title("BMI Hesaplayıcı")
window.minsize(width=400, height=300)
window["bg"] = "lightblue"

# Kilo giriş
tk.Label(window, text="Enter Your Weight (kg):").pack()
entry_kilo = tk.Entry(window)
entry_kilo.pack(pady=5)

# Boy giriş
tk.Label(window, text="Enter Your Height (cm):").pack()
entry_boy = tk.Entry(window)
entry_boy.pack(pady=5)

# Hesapla butonu
buton = tk.Button(window, text="Calculate", command=bmi_hesapla)
buton.pack(pady=10)

# Sonuç gösterimi
sonuc_label = tk.Label(window, text="", justify="left")
sonuc_label.pack(pady=10)

# Başlat
window.mainloop()
