import requests

API_KEY = "321214ff-1753-45e9-8944-e491a0b7e288"
URL = "https://api.cricapi.com/v1/currentMatches"

def show_recent_matches():
    print("The current cricket scores are: \n")

    try:
        response = requests.get(URL, params={"apikey": API_KEY})
        if response.status_code != 200:
            print("Error:", response.status_code)
            return
    except Exception as e:
        print("sorry, there's an error :", e)
        return

    data = response.json().get("data")

    if not data:
        print("sorry, no recent matches are to be found.")
        return

    count = 1
    for match in data:
        if count > 10:
            break

        print("Match", count, ":", match.get("name", "N/A"))

        teams = match.get("teams", [])
        if len(teams) == 2:
            print("Teams:", teams[0], "vs", teams[1])
        else:
            print("sorry, the teams information is not available.")

        scores = match.get("score", [])
        if scores:
            for s in scores:
                inning = s.get("inning", "-")
                runs = s.get("r", "-")
                wickets = s.get("w", "-")
                overs = s.get("o", "-")
                print(" ", inning, ":", runs, "/", wickets, "(", overs, "overs )")
        else:
            print("sorry, no scores are available")

        print("Status:", match.get("status", "Unknown"))
        print("----------------------------------------")

        count += 1

show_recent_matches()
