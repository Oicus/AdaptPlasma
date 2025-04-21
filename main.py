from src.anfis.anfis_model import AdaptivePlasmaANFIS
from src.plasma.control import PlasmaController

# Örnek veri
moisture = 30
temperature = 40

# ANFIS modeli başlat
anfis_model = AdaptivePlasmaANFIS()
anfis_model.load("models/adaptplasma_model.pt")

# Tahmin
recommended_output = anfis_model.predict(moisture, temperature)

# Plazma sistemine gönder
plasma_ctrl = PlasmaController()
plasma_ctrl.adjust_plasma(recommended_output)
