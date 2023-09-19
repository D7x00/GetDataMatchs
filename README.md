# Match Details Scraper

This Python script is designed to scrape and extract match details from a specific website, allowing you to save the information to a CSV file. You can use this script to retrieve details about football (soccer) matches from the website . The script provides options to fetch match details for today, tomorrow, or yesterday.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed:

- Python 3.x

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```


## Usage

1. Download the script and save it as `main.py` or any other desired name.

2. Run the script using the following command:

   ```bash
   python main.py
   ```

3. The script will prompt you to choose whether you want to fetch match details for tomorrow (T), yesterday (Y), or the current day (N).

4. After selecting an option, the script will scrape the match details from the website and save them to a CSV file named `matches-details.csv`.

## Example Usage

1. To fetch match details for tomorrow, run the script and enter `T` when prompted:

   ```bash
   [*] Input Tomorrow [T] or Yesterday [Y] or Now [N]: T
   ```

2. The script will retrieve the match details for tomorrow and save them to `matches-details.csv`.

## File Structure

- `main.py`: The main Python script.
- `lib/Color.py`: A custom module for colorful console output.
- `match_details.log`: A log file that stores information about script execution.
- `matches-details.csv`: The CSV file where match details are saved.

## Logging

The script logs its activities to the `match_details.log` file, providing information about each execution, including any errors that may occur during execution.

## Customization

You can customize the script by modifying the following parts:

- The URLs in the `url_list` variable to change the source website.
- The CSV filename in the `write_match_details_to_csv` function.
- The CSS classes used to locate match details in the `extract_match_details` function if the website structure changes.

## Note

This script is designed for educational purposes and may require adjustments if the website structure or layout changes. Always ensure you have the necessary permissions to scrape data from websites, as scraping without permission may violate the website's terms of service.

Feel free to enhance or modify this script to suit your specific needs or integrate it into larger projects.
