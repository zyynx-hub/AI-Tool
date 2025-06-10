import pandas as pd
from modules.preprocessor import preprocess_text

def get_prepared_dataframe(file_path):
    """
    Leest het Excelbestand in, voert per cel tekstvoorbewerking uit,
    en retourneert een opgeschoonde DataFrame.
    """
    try:
        df = pd.read_excel(file_path)
        print(f"[INFO] Excelbestand '{file_path}' succesvol ingelezen.")

        # Opschonen van alle cellen in alle kolommen
        for col in df.columns:
            df[col] = df[col].astype(str).apply(preprocess_text)

        print("[INFO] Dataset is opgeschoond en klaar voor analyse.")
        return df

    except Exception as e:
        print(f"[ERROR] Probleem bij verwerken van '{file_path}': {e}")
        return None
