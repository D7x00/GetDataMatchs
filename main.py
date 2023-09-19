import requests
from bs4 import BeautifulSoup
import csv
import logging
from lib.Color import *

# Configure the logging system
logging.basicConfig(filename='match_details.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def write_match_details_to_csv(filename, match_content):
    try:
        with open(filename, 'w', newline='') as output_file:
            fieldnames = match_content[0].keys()
            dict_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            dict_writer.writeheader()
            dict_writer.writerows(match_content)

        logging.info(f"Match details saved to '{filename}'")

    except Exception as e:
        logging.error(f"Error: {str(e)}")

    print(Color.Success(f"Match details saved to '{filename}'"))


def get_url():
    while True:
        State_Result = input(f'{Color.fore.YELLOW}[*]Input Tomorrow [T] or Yesterday [Y] or Now [N] :{Color.Reset} ')
        url_list = ["https://stad.yalla-shoots.io/go/", "https://stad.yalla-shoots.io/matches-yesterday/",
                    "https://stad.yalla-shoots.io/matches-tomorrow/"]

        if State_Result.upper() == 'T':
            url = url_list[2]
        elif State_Result.upper() == 'Y':
            url = url_list[1]
        else:
            url = url_list[0]
        if url:
            try:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                  'like Gecko) Chrome/116.0.0.0 Safari/537.36'}
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    print(Color.Success("Successfully retrieved the page"))
                    return response
                elif response.status_code == 401:
                    print(Color.Error("Unauthorized!"))
                else:
                    print(Color.Error("Failed to retrieve the page"))
            except requests.exceptions.RequestException as e:
                print(Color.Error(f"Failed to connect to the server: {e}"))
        else:
            print(Color.Error("URL cannot be empty. Please try again."))


def extract_match_details(soup):
    matches = soup.find_all('div', class_='match-container')
    match_details = []

    for match in matches:
        team_names = [team.text.strip() for team in match.find_all('div', class_='team-name')]
        match_time = match.find('div', id='match-time').text.strip()
        match_result = match.find('div', id='result').text.strip()
        match_state = match.find('div', class_='date').text.strip()

        match_details.append({
            'Team A': team_names[1],
            'Team B': team_names[0],
            'Time': match_time,
            'Result': match_result,
            'State': match_state
        })

    return match_details


def main():
    # get Responses
    response = get_url()
    soup = BeautifulSoup(response.content, 'lxml').find('div', class_='albaflex')
    # Export match details
    match_details = extract_match_details(soup)
    # Save Matches in File
    write_match_details_to_csv('matches-details.csv', match_details)


if __name__ == "__main__":
    print(f"\n{Color.fore.MAGENTA} Starting Tools .........  {Color.Reset}")
    print("\n")
    main()
