import pandas as pd

# Load the CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Analyze the data
def analyze_data(data):
    # Display basic statistics
    print("\nBasic Statistics:")
    print(data.describe())

    # Count unique values in a specific column (e.g., 'Category')
    if 'Category' in data.columns:
        unique_categories = data['Category'].nunique()
        print(f"\nNumber of unique categories: {unique_categories}")

# Main function
def main():
    file_path = 'data.csv'  # Replace with your CSV file path
    data = load_data(file_path)
    
    if data is not None:
        analyze_data(data)

if __name__ == "__main__":
    main()