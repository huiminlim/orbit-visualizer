import requests

if __name__ == "__main__":
    r = requests.get("https://api.endurancein.space/tle")

    # Exit if HTTP request failed
    if r.status_code != 200:
        print("TLE request failed... Exiting...")
        exit(1)

    tle1 = r.json()["tle1"]
    tle2 = r.json()["tle2"]
    print(tle1, tle2)
