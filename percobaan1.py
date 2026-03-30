# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Menyiapkan himpunan Fuzzy
makanan = ctrl.Antecedent(np.arange(0,11), 'makanan')
pelayanan = ctrl.Antecedent(np.arange(0,11), 'pelayanan')
nilai = ctrl.Consequent(np.arange(0,11), 'nilai')
# Rasa makanan
makanan['TidakEnak'] = fuzz.trimf(makanan.universe, [0, 2, 4])
makanan['Sedang'] = fuzz.trimf(makanan.universe, [3, 5, 7])
makanan['Enak'] = fuzz.trimf(makanan.universe, [6, 8, 10])
# Nilai pelayanan
pelayanan['Ketus'] = fuzz.trimf(pelayanan.universe, [0, 2, 4])
pelayanan['Biasa'] = fuzz.trimf(pelayanan.universe, [3, 5, 7])
pelayanan['Ramah'] = fuzz.trimf(pelayanan.universe, [6, 8, 10])
# Nilai restoran
nilai['Buruk'] = fuzz.trimf(nilai.universe, [0, 2, 4])
nilai['Cukup'] = fuzz.trimf(nilai.universe, [3, 5, 7])
nilai['Baik'] = fuzz.trimf(nilai.universe, [6, 8, 10])

makanan.view()
pelayanan.view()
nilai.view()
input("Tekan ENTER untuk melanjutkan")