import botometer
import csv
import itertools
from itertools import zip_longest


def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


def attach(filename, results):

    fields = ['astroturf', 'fake_follower', 'financial',
              'other', 'overall', 'self_declared', 'spammer']
    filename = filename

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writerows(results)


def cap_attach(filename, results):

    fields = ['english', 'universal']
    filename = filename

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writerows(results)


def user_attach(user):

    rows = []
    rows.append(user)
    rows = zip_longest(*rows, fillvalue="")
    filename = "users.csv"
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)


rapidapi_key = "YOUR_RAPIDAPI_KEY"
twitter_app_auth = {
    'consumer_key': 'YOUR_TWITTER_CONSUMER_KEY',
    'consumer_secret': 'YOUR_TWITTER_CONSUMER_SECERET',
    'access_token': 'YOUR_TWITTER_ACCESS_TOKEN',
    'access_token_secret': 'YOUR_TWITTER_ACCESS_TOKEN_SECERET',
}


def main(filename):

    filename = filename

    rows = []
    usernames = []
    count = 0

    with open(filename, 'r', encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            rows.append(row)

        for row in rows:
            for col in row:
                usernames.append(col.strip())

    list_chunks = chunked_iterable(usernames, 100)
    for i in list_chunks:
        fetch_botometer(i)
        count += 100

        print(f"Completed {count}")


def data_manipulation(i, user):

    rs_eng = list()
    rs_uni = list()
    ds_eng = list()
    ds_uni = list()
    user_list = list()
    cap = list()

    if "error" in i:
        err = {'astroturf': "-", 'fake_follower': "-", 'financial': "-",
               'other': "-", 'overall': "-", 'self_declared': "-", 'spammer': "-"}

        rs_uni.append(err)
        rs_eng.append(err)
        ds_eng.append(err)
        ds_uni.append(err)
        user_list.append(user)
        cap.append({
            "english": "-",
            "universal": "-"})

    else:

        user_list.append(user)
        rs_uni.append(i["raw_scores"]["universal"])
        rs_eng.append(i["raw_scores"]["english"])
        ds_uni.append(i["display_scores"]["universal"])
        ds_eng.append(i["display_scores"]["english"])
        cap.append(i["cap"])

    attach(filename="rs_eng.csv", results=rs_eng)
    attach(filename="rs_uni.csv", results=rs_uni)
    attach(filename="ds_eng.csv", results=ds_eng)
    attach(filename="ds_uni.csv", results=ds_uni)
    user_attach(user_list)
    cap_attach(filename="cap.csv", results=cap)


def fetch_botometer(screen_names):

    bom = botometer.Botometer(wait_on_ratelimit=True,
                              rapidapi_key=rapidapi_key,
                              **twitter_app_auth)
    screen_names = [sn.encode("utf-8") for sn in screen_names]
    accounts = screen_names

    for screen_name, result in bom.check_accounts_in(accounts):
        data_manipulation(result, screen_name)


main(filename="mixnew.csv")
