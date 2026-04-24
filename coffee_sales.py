import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CLASSE PRINCIPALE
# ==========================================
class SalesApp:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    # 1. IMPORTATION
    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("\n" + "=" * 70)
        print(f"✓ Données importées : {len(self.df)} lignes × {len(self.df.columns)} colonnes")

    # 2. APERÇU INITIAL
    def overview(self):
        print("\n" + "=" * 70)
        print("APERÇU DES DONNÉES")
        print("=" * 70)
        print(self.df.head(10))
        print(self.df.tail(10))
        print("\nTypes de données :")
        print(self.df.dtypes)
        print("\nValeurs manquantes :")
        print(self.df.isnull().sum())

    # 3. STATISTIQUES
    def summarize_data(self):
        self.df['total_price'] = self.df['transaction_qty'] * self.df['unit_price']
        print("\n--- Statistiques ---")
        print(self.df[['transaction_qty', 'unit_price', 'total_price']].describe())

    # 4. PRÉPARATION DES DONNÉES (fusion)
    def prepare_data(self):
        print("\n--- PRÉPARATION DES DONNÉES ---")

        # Convertion Date & heure
        self.df['transaction_datetime'] = pd.to_datetime(
            self.df['transaction_date'] + ' ' + self.df['transaction_time'],
            format='%d/%m/%Y %H:%M:%S',
            errors='coerce'
        )
        self.df['heure'] = self.df['transaction_datetime'].dt.hour
        self.df['jour_semaine'] = self.df['transaction_datetime'].dt.day_name()
        self.df['mois'] = self.df['transaction_datetime'].dt.month
        self.df['annee'] = self.df['transaction_datetime'].dt.year
        self.df.drop(['transaction_date', 'transaction_time'], axis=1, inplace=True)
        print("✓ Colonne 'transaction_datetime' créée")
        print("✓ Composantes extraites : heure, jour_semaine, mois, annee")

        #  Convertion Numérique
        numeric_cols = ['transaction_id', 'transaction_qty', 'unit_price',
                        'store_id', 'product_id']

        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
                print(f"✓ {col} converti en {self.df[col].dtype}")

        # Gestion des Categories

        categorical_cols = ['store_location', 'product_category',
                            'product_type', 'product_detail']

        for col in categorical_cols:
            if col in self.df.columns:
                # Remplacer les valeurs manquantes par 'Unknown'
                self.df[col] = self.df[col].astype(str).fillna('Unknown')
                unique = self.df[col].nunique()
                print(f"✓ {col} : {unique} catégories uniques")

        print("✓ Données préparées avec succès")

    # 5. NETTOYAGE DES DONNÉES (fusion)
    def clean_data(self):
        print("\n--- NETTOYAGE DES DONNÉES ---")

        avant = len(self.df)
        self.df.dropna(subset=[
            'transaction_qty',
            'unit_price',
            'transaction_datetime'
        ], inplace=True)
        print(f"✓ {avant - len(self.df)} lignes manquantes supprimées")

        avant = len(self.df)
        self.df.drop_duplicates(inplace=True)
        print(f"✓ {avant - len(self.df)} doublons supprimés")
        print("\nValeurs uniques après nettoyage :")
        for col in ['store_location', 'product_category', 'product_type']:
            print(col, "→", self.df[col].unique()[:5])

    # 6. APERÇU FINAL
    def final_overview(self):
        print("\n" + "=" * 70)
        print("DONNÉES FINALES")
        print("=" * 70)
        print(self.df.head(20))
        print(f"\nDimensions finales : {self.df.shape}")

    # 7. EXPORT
    def export_data(self, filename="data_cleanedd.csv"):
        self.df.to_csv(filename, sep=';', index=False)
        print(f"✓ Données exportées vers {filename}")

    # 8. ANALYSE DES VENTES
    def sales_analysis(self):
        self.df['total_price'] = self.df['transaction_qty'] * self.df['unit_price']

        print("\n--- Chiffre d'affaires total ---")
        print(self.df['total_price'].sum())

        print("\n--- Ventes par catégorie ---")
        print(self.df.groupby('product_category')['total_price'].sum())

    # 9. VISUALISATIONS
    def product_and_totalP_bar(self):
        # === Visualisations originales ===
        a = self.df.groupby('product_category')['total_price'].sum()
        print(a)
        d = ('orange', 'red', 'brown', 'black', 'brown', 'yellow', 'pink', 'purple', 'grey')
        a = self.df.groupby('product_category')['total_price'].sum()
        plt.bar(a.index, a, color=d)
        plt.scatter(a.index, a, color='purple', marker='o')
        plt.title('Product Category vs Total Price', fontweight='bold')
        plt.xlabel('Product Category', fontweight='bold')
        plt.ylabel('Total Price', fontweight='bold')
        plt.show()

    def sales_by_type(self):
        # --- Vente par type de produit ---
        a = self.df.groupby('product_type')['total_price'].sum()
        print(a)
        colors = [
            'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray',
            'tab:olive', 'tab:cyan',
            'blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan',
            'gold', 'teal', 'navy', 'lime', 'coral', 'indigo', 'maroon', 'darkgreen', 'darkorange'
        ]
        plt.bar(a.index, a, color=colors)
        plt.scatter(a.index, a, color='purple', marker='o', s=5)
        plt.xticks(rotation=45, ha='right')
        plt.title('Product type vs Total Price', fontweight='bold')
        plt.xlabel('Product type', fontweight='bold')
        plt.ylabel('Total Price', fontweight='bold')
        plt.show()

        # --- Vente par type et top 10 ---
        a = self.df.groupby('product_type')['total_price'].sum()
        b = self.df.groupby('product_type')['total_price'].sum().sort_values(ascending=False).head(10)
        print(a)
        plt.bar(a.index, a, color=colors)
        plt.bar(b.index, b, color='red', label="top 10 produit category")
        plt.xticks(rotation=45, ha='right')
        plt.title('Product type vs Total Price', fontweight='bold')
        plt.xlabel('Product type', fontweight='bold')
        plt.ylabel('Total Price', fontweight='bold')
        plt.legend()
        plt.show()

    def quantity_category(self):
        # --- Quantité vendue par catégorie ---
        s = self.df.groupby('product_category')['transaction_qty'].sum()
        d = ('orange', 'red', 'brown', 'black', 'brown', 'yellow', 'pink', 'purple', 'grey')
        plt.bar(s.index, s, color=d)
        plt.xlabel("category")
        plt.ylabel("quantity")
        plt.xticks(rotation=45, ha='right')
        plt.title("Quantité vendue par catégorie", fontweight='bold')
        plt.show()

    def quan_price_category(self):
        # --- Quantité vendue et prix par catégorie ---
        s = self.df.groupby('product_category')['transaction_qty'].sum()
        a = self.df.groupby('product_category')['total_price'].sum()
        plt.bar(s.index, s, color='black', label="quantity")
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("category")
        plt.ylabel("quantity/prix")
        plt.title("Quantité vendue et prix par catégorie", fontweight='bold')
        plt.bar(a.index, a, color='red', alpha=0.2, label="total price")
        plt.legend()
        plt.show()

    def sales_overview(self):
        # --- Ventes par jour ---
        s = self.df.groupby('jour_semaine')['total_price'].sum()
        plt.subplot(2, 1, 1)
        plt.bar(s.index, s)
        plt.subplot(2, 1, 2)
        plt.pie(s.values, labels=s.index, autopct='%1.1f%%')
        plt.suptitle("Ventes par jour de la semaine")
        plt.show()

        # --- Ventes par heure ---
        sales_hour = self.df.groupby('heure')['total_price'].sum()
        print(sales_hour)
        plt.plot(sales_hour.index, sales_hour, color="black", marker='*', markerfacecolor='red',
                 markeredgecolor='blue', markersize=10, label="vente par heur")
        q = self.df.groupby('heure')['transaction_qty'].sum()
        print(q)
        plt.plot(q.index, q, color="red", marker='s', markerfacecolor='yellow', markeredgecolor='green',
                 markersize=5, label="qty par heure")
        plt.title("courbes representatifes des quantités et ventes par heure", fontweight='bold')
        plt.xlabel("Heure", fontweight='bold')
        plt.ylabel("quantity/vente", fontweight='bold')
        plt.legend()
        plt.show()

        # --- Ventes par magasin ---
        p = ("pink", "red", "green")
        k = self.df.groupby('store_location')['total_price'].sum()
        plt.subplot(1, 2, 1)
        plt.bar(k.index, k, color=p)
        plt.xticks(rotation=45, ha='right')
        plt.subplot(1, 2, 2)
        plt.pie(k.values, labels=k.index, autopct='%1.1f%%')
        plt.legend(k.index, title="key")
        plt.suptitle("Ventes par magasin")
        plt.show()

# ==========================================
# MAIN
# ==========================================
def main():
    app = SalesApp("datasett_.csv")

    while True:
        print("\n" + "=" * 60)
        print("MENU - ANALYSE DES VENTES")
        print("=" * 60)
        print("1. Charger les données")
        print("2. Aperçu initial")
        print("3. Statistiques")
        print("4. Préparer les données")
        print("5. Nettoyer les données")
        print("6. Aperçu final")
        print("7. Exporter les données")
        print("8. Analyse des ventes")
        print("9. Product Category vs Total Price")
        print("10. Product Type vs Total Price")
        print("11. Quantité vendue par catégorie")
        print("12. Quantité et prix par catégorie")
        print("13. Ventes par jour")
        print("0. Quitter")

        choix = input("Votre choix : ")

        try:
            if choix == "1":
                app.load_data()
            elif app.df is None:
                print("❌ Veuillez charger les données d'abord")
            elif choix == "2":
                app.overview()
            elif choix == "3":
                app.summarize_data()
            elif choix == "4":
                app.prepare_data()
            elif choix == "5":
                app.clean_data()
            elif choix == "6":
                app.final_overview()
            elif choix == "7":
                app.export_data()
            elif choix == "8":
                app.sales_analysis()
            elif choix == "9":
                app.product_and_totalP_bar()
            elif choix == "10":
                app.sales_by_type()
            elif choix == "11":
                app.quantity_category()
            elif choix == "12":
                app.quan_price_category()
            elif choix == "13":
                app.sales_overview()
            elif choix == "0":
                print("✓ Fin du programme")
                break
            else:
                print("❌ Choix invalide")
        except Exception as e:
            print("⚠️ Erreur :", e)


if __name__ == "__main__":
    main()











