from datetime import datetime
import requests

def generate_log(log_data):
    """
    Writes a log file with a timestamped filename.
    
    Args:
        log_data (list): A list of log entry strings.
    
    Returns:
        str: The filename of the generated log.
    
    Raises:
        ValueError: If log_data is not a list.
    """
    # Validate input type
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list of strings")

    # Build timestamped filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write entries to file (empty list still creates an empty file)
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Confirmation message including filename
    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetches a sample post from a public API using requests."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
