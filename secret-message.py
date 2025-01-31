#print("Script is running")

#step 1 is fetching the data from the google document url

import requests

doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

def decode_secret_message(doc_url):
    try:
        response = requests.get(doc_url)
        response.raise_for_status
        print("Data fetched successfully!")
        print("Response Text:", response.text[:500])
    except requests.exceptions.RequestException as e:
        print(f"Reguest failed: {e}")
        return

    data = response.text.strip().splitlines()
    print("Data received from document:", data)
    return data

data = decode_secret_message(doc_url)

if data:

#step 2 is parsing the data
    grid_data = []
    for line in data:
        parts = line.split(',')

        if len(parts) == 3:
            print(f"Parsing line: {line} -> Parts: {parts}")
            try:
                char = parts[0].strip()
                x = int(parts[1].strip())
                y = int(parts[2].strip())
                grid_data.append((char, x, y))
            except ValueError as ve:
                print(f"Skipping line due to error: {ve}")

        else:
            print(f"Skipping malformed line: {line}")

    print("Parsed data:", grid_data)

#step 3 is determining the grid dimensions
    if grid_data:
        max_x = max(x for _, x, _ in grid_data)
        max_y = max(y for _, _, y in grid_data)

#step 4 is creating and populating the grid
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for char, x, y in grid_data:
            grid[y][x] = char

#step 5 is printing the grid.
        print("Grid:")
        for row in grid:
            print(''.join(row))
    else:
        print("No valid data to process.")
else:
    print("Failed to fetch or parse data.")    
