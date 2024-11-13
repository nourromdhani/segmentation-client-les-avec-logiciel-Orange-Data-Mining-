import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score

# Simuler des donn�es
# Admettons que 'id_client' est l'identifiant unique du client
data = pd.DataFrame({
    'id_client': range(1, 101),  # 100 clients
    'order_details': np.random.rand(100)  # D�tails fictifs des commandes
})

# Nombre de clusters d�sir�
k = 5

# Assigner al�atoirement un cluster � chaque client
np.random.seed(42)  # Pour la reproductibilit�
data['cluster'] = np.random.randint(1, k + 1, size=len(data))

# Calcul du score de silhouette
score = silhouette_score(np.array(data['id_client']).reshape(-1, 1), data['cluster'])

print(f"Score de silhouette pour le clustering al�atoire: {score}")

# Afficher quelques donn�es pour visualiser
print(data.head())