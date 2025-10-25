# 🏭 Condition Monitoring of Hydraulic Systems (Demo)

Dieses Repository zeigt, wie man **industrielle Maschinendaten** (Zeitreihen) analysieren und für **Predictive Maintenance** oder **Zustandsüberwachung** nutzt – am Beispiel des [UCI Hydraulic System Dataset](https://archive.ics.uci.edu/ml/datasets/Condition+monitoring+of+hydraulic+systems).

---

## 📘 Projektziel
Demonstration einer datengetriebenen Pipeline zur Analyse von Maschinenzeitreihen:
- Explorative Datenanalyse (EDA)
- Feature Engineering (z. B. Mittelwerte, Gradienten)
- Klassifikation der Zustände (Cooler, Valve, Pump, Accumulator)
- Visualisierung und Dashboard

---

## 📂 Datenbeschreibung

**Quelle:**  
ZeMA gGmbH, Eschberger Weg 46, 66121 Saarbrücken  
Kontakt: t.schneider@zema.de  

**Publikationen:**  
1. N. Helwig, E. Pignanelli, A. Schütze (2015): *Condition Monitoring of a Complex Hydraulic System Using Multivariate Statistics*, IEEE I2MTC, Pisa, Italy.  
2. N. Helwig, A. Schütze (2015): *Detecting and compensating sensor faults in a hydraulic condition monitoring system*, SENSOR 2015, Nürnberg, Germany.  
3. T. Schneider, N. Helwig, A. Schütze (2017): *Automatic feature extraction and selection for classification of cyclical time series data*, *tm - Technisches Messen* 84(3).

**Datensatz-Details:**
- 2205 Zyklen (60 s pro Zyklus)
- 17 Sensoren (43680 Attribute pro Zyklus)
- Samplingraten: 100 Hz / 10 Hz / 1 Hz  
- Keine fehlenden Werte

**Zielvariablen (profile.txt):**
| Komponente | Werte | Bedeutung |
|-------------|--------|------------|
| Cooler | 3, 20, 100 | Ausfall – reduziert – optimal |
| Valve | 73, 80, 90, 100 | Ausfall → optimal |
| Pump Leakage | 0, 1, 2 | Kein – schwach – stark |
| Accumulator | 90, 100, 115, 130 | Druckverlust → optimal |
| Stable Flag | 0, 1 | stabil / instabil |

---

## ⚙️ Projektaufbau

| Notebook | Beschreibung |
|-----------|---------------|
| `01_data_exploration.ipynb` | Daten laden, Sensoren analysieren, Visualisierungen |
| `02_feature_engineering.ipynb` | Feature-Berechnung (Mittelwerte, Peaks, FFT, Statistiken) |
| `03_model_training.ipynb` | Klassifikationsmodelle (z. B. RandomForest, XGBoost, CNN) |
| `04_visualization_dashboard.ipynb` | Plotly- oder Streamlit-Dashboard |

---

## 🚀 Setup

```bash
git clone https://github.com/<dein-user>/industrial-time-series-demo.git
cd industrial-time-series-demo
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

