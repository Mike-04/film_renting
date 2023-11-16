import json

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            movies = json.load(file)
        print(f'Data successfully loaded from {filename}')
        return movies
    except Exception as e:
        print(f'Error loading data from {filename}: {e}')
        return None
    
def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        print(f'Data successfully saved to {filename}')
    except Exception as e:
        print(f'Error saving data to {filename}: {e}')