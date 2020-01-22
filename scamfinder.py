import praw
import re
from datetime import datetime, timezone


def find_possible_phone_number(str):

    # Filter our words that have more than 3 consequent characters
    clean = "".join(filter(None, re.split(
        '(?:[a-zA-Z]{3,}|[\$\@()+.])+', str)))

    # Remove all special characters from string
    clean = ''.join(e for e in clean if e.isalnum())
    # Some scammers use 'I' instead of 1 and 'O' instead of 0
    clean = clean.replace("I", "1").replace("O", "0")

    # Regex for phone numbers
    phone_regex = "\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*"
    phone_numbers = re.findall(phone_regex, clean)
    if len(phone_numbers) > 0:
        return "".join(phone_numbers[0])
    return None


def get_time_filter():
    # Ask for time frame
    time_filter_input = int(
        input("Enter time filter:\n1 - Hour\n2 - Day\nChoice: "))
    time_filter = ""
    if time_filter_input is 1:
        time_filter = "hour"
    else:
        time_filter = "day"
    return time_filter


def get_sort_by():
    sort_by_input = int(
        input("What to sort by?:\n1 - new\n2 - relevance\n3 - hot\nChoice: "))
    sort_by = ""
    if sort_by_input is 1:
        sort_by = "new"
    elif sort_by_input is 2:
        sort_by = "relevance"
    else:
        sort_by = "hot"
    return sort_by


def get_max_posts_to_load():
    return int(input("Max posts to load?\nChoice: "))


def show_all():
    show_all_input = int(
        input("Show duplicate numbers?:\n1 - Yes\n2 - No\nChoice: "))
    return show_all_input is 1


# print(find_possible_phone_numbers(test))
client_secret = ""
client_id = ""
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='Bot')

numbers = []

time_filter = get_time_filter()
sort_by = get_sort_by()
limit = get_max_posts_to_load()
show_all = show_all()
all = reddit.subreddit("all")


numbers = []
for i in all.search('tech support', limit=limit, time_filter=time_filter, sort=sort_by):
    phone_nr = find_possible_phone_number(i.title)
    if phone_nr is not None:
        created_at = datetime.fromtimestamp(i.created_utc)
        now = datetime.now()
        difference = now - created_at
        age = round(difference.seconds)  # age in seconds
        numbers.append(
            [age, phone_nr, "https://reddit.com" + i.permalink, i.title])


# sort numbers by age
numbers = sorted(numbers, key=lambda x: x[0])
displayed = []
for nr in numbers:
    if nr[1] not in displayed or show_all:
        age = ""
        # More than 60 minutes ago
        if round(nr[0] / 60) > 60:
            age = "{} hours old".format(
                round(nr[0] / 60 / 60))  # Minutes to hours
        else:
            age = "{} min old".format(round(nr[0] / 60))

        print ("----------")
        print("[{}]".format(age))
        print("Title: {}".format(nr[3]))
        print("Parsed Number: {}".format(nr[1]))
        print("Link: {}".format(nr[2]))
        # print("[{}] - Possible Number: {} - {}".format(age,nr[1],nr[2]))
        displayed.append(nr[1])