# TODO:
import pandas as pd
from client.api_client import fetch_data
from utils.validators import validate_items
# In the main function:
#   - fetch items from the API using the fetch_data function
#   - validate the received items using the validate_items function, which returns True if the items are valid, otherwise raises a ValueError with an appropriate message
#   - write the valid items to a dataframe using pandas, and then save the dataframe to a JSON file named "data/posts.json"

def main():

    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Fetching paginated data…")
    # Fetch items
    items = fetch_data(api_url)
    if items is None:
        return

    print("Validating items…")
    # Validate items
    try:
        validate_items(items)
    except ValueError as e:
        print(f"Validation error: {e}")
        return

    json_file_path = "data/posts.json"
    # Save JSON data into the file
    df = pd.DataFrame(items)
    df.to_json(json_file_path)

if __name__ == "__main__":
    main()