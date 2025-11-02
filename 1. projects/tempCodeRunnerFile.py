# import requests

# API_KEY = "321214ff-1753-45e9-8944-e491a0b7e288"
# BASE_URL = "https://api.cricapi.com/v1"

# def get_recent_matches():
#     print("Fetching recent matches...\n")
#     response = requests.get(f"{BASE_URL}/currentMatches", params={"apikey": API_KEY})

#     if response.status_code != 200:
#         print("Error:", response.status_code, response.text)
#         return

#     data = response.json().get("data", [])

#     if not data:
#         print("No matches found.")
#         return

#     for match in data[:10]:
#         name = match.get("name", "N/A")
#         status = match.get("status", "Unknown")
#         teams = match.get("teams", [])
#         score = match.get("score", [])
#         print(f"🏆 {name}")
#         print(f"🆚 {' vs '.join(teams)}")
#         for s in score:
#             print(f"   {s.get('inning')}: {s.get('r')}/{s.get('w')} ({s.get('o')} ov)")
#         print(f"📅 Status: {status}")
#         print("-" * 60)

# get_recent_matches()


# import requests

# API_KEY = "321214ff-1753-45e9-8944-e491a0b7e288"
# BASE_URL = "https://api.cricapi.com/v1"

# def get_recent_matches():
#     print("we are fetching the recent matches...\n")
    
#     response = requests.get(
#         BASE_URL + "/currentMatches",
#         params={"apikey": API_KEY}
#     )

#     if response.status_code != 200:
#         print("this is an error code:", response.status_code, response.text)
#         return

#     matches = response.json().get("data", [])

#     if not matches:
#         print("sorry! no matches are found to be displayed.")
#         return

#     for match in matches[:10]:
#         name = match.get("name", "N/A")
#         status = match.get("status", "Unknown")
#         teams = match.get("teams", [])
#         scores = match.get("score", [])

#         print(name)
#         print(" vs ".join(teams))
        
#         for s in scores:
#             inning = s.get("inning", "N/A")
#             runs = s.get("r", "-")
#             wickets = s.get("w", "-")
#             overs = s.get("o", "-")
#             print("   {}: {}/{} ({} ov)".format(inning, runs, wickets, overs))

#         print("Status: " + status)
#         print("-" * 60)

# get_recent_matches()


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
            print("No score data available.")

        print("Status:", match.get("status", "Unknown"))
        print("----------------------------------------")

        count += 1

show_recent_matches()
