from src.anfis.anfis_model import AdaptivePlasmaANFIS

# ANFIS modeli başlat
anfis_model = AdaptivePlasmaANFIS()
anfis_model.load("models/adaptplasma_model.pt")

# Girdi verileri
moisture = 30
temperature = 40

# Tahmin
output = anfis_model.predict(moisture, temperature)
print(f"Plazma kontrol çıktısı: {output}")
