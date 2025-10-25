import pandas as pd
import numpy as np
import os

csv_path = os.path.join("..", "data", "ker450_tbm_raw_daily", "combined.csv")
#df = pd.read_csv(r'C:\Users\Ismail Güner\OneDrive - Heitkamp Construction Swiss GmbH\Desktop\00_Github_Projects\construction-data-lab\tbm_intel_mvp\data\ker450_tbm_raw_daily\combined.csv')

print("Lese Datei ein:", csv_path)

#CSV einlesen (automatische Komma- oder Semikolon-Erkennung)
df = pd.read_csv(csv_path, sep=",", encoding="utf-8-sig", nrows=100000)

print("\n Daten erfolgreich geladen!\n")

#=== GRUNDLEGENDER ÜBERBLICK ===
print(" Erste 5 Zeilen:")
print(df.head(),"\n")

print("Dimensionen:")
print(f"->Zeilen: {df.shape[0]:,}")
print(f"->Spalten: {df.shape[1]:,}")

print("Spaltennamen:")
print(df.columns.tolist(), "\n")

#=== DATENTYPEN UND FEHLWERTE ===
print("Datentypen und fehlende Werte:")
print(df.info(), "\n")

missing = df.isna().sum()
missing_percent =(missing / len(df)) * 100
missing_summary = pd.DataFrame({
    'missing_count': missing,
    'missing_percent': missing_percent
}). sort_values(by='missing_percent', ascending=False)

print("Fehlende Werte (Top 10):")
print(missing_summary.head(10), "\n")

#=== DUBLIKATE ===
duplicates = df.duplicated().sum()
print(f"Doppelte Zeilen: {duplicates} \n")

#=== GRUNDLEGENDER STATISTISCHER ÜBERBLICK ===
print(" Numerische Übersicht:")
print(df.describe().T, "\n")

#=== KATEGORISCHE SPALTEN ===
categorical_cols= df.select_dtypes(include=['object']).columns
print("kategorische Spalten:")
print(list(categorical_cols))
print(f"Anzahl: {len(categorical_cols)}\n")

#=== SPEZIAL FÜR SCHNELLE KORRELATIONEN ===
numeric_cols = df.select_dtypes(include=np.number).columns
if len(numeric_cols) > 1:
    print("Korrelationsmatrix (Auszug):")
    print(df[numeric_cols].corr().round(2).head())
else:
    print("Keine nuemrischen Spalten für Korrelationen gefunden.")

print("\n Übersicht abgeschlossen.")