import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Path to the processed CSV file
    file_path = os.path.join("..", "data", "processed", "heatwave_data.csv")

    # Load the CSV
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!")
        print(df.head())  # Print first few rows

        # Check if necessary columns exist before plotting
        if 'temperature' in df.columns:
            df['temperature'].plot(kind='line', title='Temperature Trend')
            plt.xlabel('Index')
            plt.ylabel('Temperature')
            plt.tight_layout()
            plt.show()
        else:
            print("⚠️ 'temperature' column not found in the dataset.")

    except FileNotFoundError:
        print("❌ CSV file not found. Please make sure it exists at the specified path.")

if __name__ == "__main__":
    main()
