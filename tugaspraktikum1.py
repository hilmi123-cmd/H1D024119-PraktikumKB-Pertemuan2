"""Logika Fuzzy 1 (Kipas Angin)

Menentukan kecepatan kipas berdasarkan:
- Suhu (0-40 derajat C)
- Kelembapan (0-100 persen)

Output:
- Kecepatan kipas (0-100)
"""

import numpy as np

try:
	import skfuzzy as fuzz
	from skfuzzy import control as ctrl
except ImportError as exc:
	raise SystemExit(
		"Library scikit-fuzzy belum terpasang. Jalankan: pip install scikit-fuzzy"
	) from exc


def build_fuzzy_system() -> ctrl.ControlSystemSimulation:
	# Variabel input (antecedent)
	suhu = ctrl.Antecedent(np.arange(0, 41, 1), "suhu")
	kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), "kelembapan")

	# Variabel output (consequent)
	kecepatan_kipas = ctrl.Consequent(np.arange(0, 101, 1), "kecepatan_kipas")

	# Membership function suhu
	suhu["dingin"] = fuzz.trimf(suhu.universe, [0, 0, 20])
	suhu["normal"] = fuzz.trimf(suhu.universe, [15, 25, 35])
	suhu["panas"] = fuzz.trimf(suhu.universe, [30, 40, 40])

	# Membership function kelembapan
	kelembapan["kering"] = fuzz.trimf(kelembapan.universe, [0, 0, 40])
	kelembapan["sedang"] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
	kelembapan["lembap"] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

	# Membership function kecepatan kipas
	kecepatan_kipas["lambat"] = fuzz.trimf(kecepatan_kipas.universe, [0, 0, 40])
	kecepatan_kipas["sedang"] = fuzz.trimf(kecepatan_kipas.universe, [30, 50, 70])
	kecepatan_kipas["cepat"] = fuzz.trimf(kecepatan_kipas.universe, [60, 100, 100])

	# Aturan fuzzy (minimal 3, di sini dibuat 6 aturan)
	rule1 = ctrl.Rule(suhu["dingin"] & kelembapan["kering"], kecepatan_kipas["lambat"])
	rule2 = ctrl.Rule(suhu["dingin"] & kelembapan["lembap"], kecepatan_kipas["sedang"])
	rule3 = ctrl.Rule(suhu["normal"] & kelembapan["sedang"], kecepatan_kipas["sedang"])
	rule4 = ctrl.Rule(suhu["normal"] & kelembapan["lembap"], kecepatan_kipas["cepat"])
	rule5 = ctrl.Rule(suhu["panas"] & kelembapan["kering"], kecepatan_kipas["cepat"])
	rule6 = ctrl.Rule(suhu["panas"] & kelembapan["lembap"], kecepatan_kipas["cepat"])

	sistem_kontrol = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
	return ctrl.ControlSystemSimulation(sistem_kontrol)


def hitung_kecepatan_kipas(suhu_input: float, kelembapan_input: float) -> float:
	simulasi = build_fuzzy_system()
	simulasi.input["suhu"] = suhu_input
	simulasi.input["kelembapan"] = kelembapan_input
	simulasi.compute()
	return float(simulasi.output["kecepatan_kipas"])


def main() -> None:
	print("=== Sistem Logika Fuzzy Kecepatan Kipas ===")

	try:
		suhu_input = float(input("Masukkan suhu (0-40 C): "))
		kelembapan_input = float(input("Masukkan kelembapan (0-100 %): "))
	except ValueError:
		print("Input harus berupa angka.")
		return

	if not 0 <= suhu_input <= 40:
		print("Suhu harus dalam rentang 0 sampai 40.")
		return

	if not 0 <= kelembapan_input <= 100:
		print("Kelembapan harus dalam rentang 0 sampai 100.")
		return

	hasil = hitung_kecepatan_kipas(suhu_input, kelembapan_input)
	print(f"Kecepatan kipas hasil fuzzy: {hasil:.2f}")


if __name__ == "__main__":
	main()
