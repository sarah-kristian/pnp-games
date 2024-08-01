
# Description: Age Facts
       # Calculates the age of a person in years, months, and days based on their birthdate.
       # Provides a random statistic based on their age. 
       # Program outputs in French and English


# Author:      Sarah Perry with Study Group 5 (Keyin College)
# Date:        2024-06-15 to 2024-06-19




# import libraries

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser

import random
import requests

# define messages in English and French

AGEFACTS_MESSAGES_EN= {
    "language" : "EN",
    "HEADER" : "\n-------------- Age Facts ----------------",
    "msg_10000_future": "You will be 10,000 days old in {days_till_10000} days.",
    "msg_10000_past": "You were 10,000 days old {days_till_10000} days ago.",
    "msg_10000_present": "You're 10,000 days old today!",
    "msg_skeleton_percentage": "{regen_amt} of your skeleton has been replaced!",
    "msg_skeleton_replacements": "Your skeleton has been replaced {regen_amt} times!",
    "msg_insect": "The amount of insects you have eaten is probably equal to {insect_amt} loaves of bread.",
    "RANDOM_STAT": "Here's a random statistic: {random_stat}",
    "STATUS_ERROR": "Sorry! This time didn't work. Please try again. See status code: {response_status_code}",
    "BIRTHDATE": "\nWhen were you born (YYYY-MM-DD)? ",
    "ERROR_MSG": "This program is not yet set up for time travellers. Please enter a date before tomorrow to continue.",
    "AGE_MSG": "\nYou are {years} years, {months} months, and {days} days old.",
    "MONTHS_MSG": "Your age in months: {age_in_months}",
    "WEEKS_MSG": "Your age in weeks: {age_in_weeks}",
    "DAYS_MSG": "Your age in days: {age_in_days}\n",
    "HISTORICAL_MSG": "\nHere is a historical event that happened on your birthdate:\n    {event_on_birthdate}.\n",
    "TRY_AGAIN_MSG": "Would you like to try another birthdate?  ",
    "SALUTATION": "\nTill next time!\n"
}


AGEFACTS_MESSAGES_FR = {
    "language" : "FR",
    "HEADER" : "\n-------------- faits sur l'âge ----------------",
    "msg_10000_future": "Tu auras 10 000 jours dans {days_till_10000} jours.",
    "msg_10000_past": "Vous aviez 10 000 jours il y a {days_till_10000} jours.",
    "msg_10000_present": "Vous avez 10 000 jours aujourd'hui !",
    "msg_skeleton_percentage": "{regen_amt}% de votre squelette a été remplacé !",
    "msg_skeleton_replacements": "Votre squelette a été remplacé {regen_amt} fois !",
    "msg_insect": "La quantité d'insectes que vous avez mangés équivaut à environ {insect_amt} pains.",
    "RANDOM_STAT": "Voici une statistique aléatoire : {random_stat}.",
    "STATUS_ERROR": "Cette fois-ci n'a pas fonctionné. Veuillez réessayer. Voir le code d'état : {response_status_code}",
    "BIRTHDATE": "\nDate de naissance (YYYY-MM-DD)? ",
    "ERROR_MSG": "Ce programme n'est pas encore configuré pour les voyageurs temporels. Veuillez saisir une date antérieure à demain pour continuer.",
    "AGE_MSG": "\nVous avez {years} ans, {months} mois et {days} jours.",
    "MONTHS_MSG": "Votre âge en mois : {age_in_months}",
    "WEEKS_MSG": "Votre âge en semaines : {age_in_weeks}",
    "DAYS_MSG": "Votre âge en jours : {age_in_days}\n",
    "HISTORICAL_MSG": "\nVoici un événement historique qui s'est produit à votre date de naissance :\n    {event_on_birthdate}.\n",
    "TRY_AGAIN_MSG": "Voulez-vous essayer une autre date de naissance ? ",
    "SALUTATION": "\nÀ la prochaine fois !\n"
}


# define functions

def get_messages_agefacts():
    while True:
        language = input("Language (FR / EN) : ").upper()
        if language == "EN":
            agefacts_messages = AGEFACTS_MESSAGES_EN
            return agefacts_messages
        elif language == "FR":
            agefacts_messages = AGEFACTS_MESSAGES_FR
            return agefacts_messages
        else:
            pass

def get_time_since_birthday(today, birthdate):

    # Calculates age using relativedelta
        # Example: 
        #    today: 2024-06-17
        #    birthdate: 1984-12-02
        #    difference: relativedelta(years=+39, months=+6, days=+15)

    difference = relativedelta(today, birthdate)
    
    # Extract difference of years, months, and days
    years = difference.years       
    months = difference.months
    days = difference.days

    age_in_days = (today - birthdate).days            # total days
    age_in_weeks = age_in_days // 7                   # total weeks
    age_in_months = difference.months + (years * 12)  # total months

    return{
        "years" : years, 
        "months" : months, 
        "days" : days, 
        "age_in_days" : age_in_days, 
        "age_in_weeks": age_in_weeks,
        "age_in_months" : age_in_months}



def get_days_till_10000(age_in_days, msgs):
    # determines when you will turn / did turn 10,000 days old
    days_till_10000 = 10000 - age_in_days
    if days_till_10000 > 0:
        msg_10000 = msgs["msg_10000_future"].format(days_till_10000=f"{days_till_10000}")
    elif days_till_10000 < 0:
        msg_10000 = msgs["msg_10000_past"].format(days_till_10000=f"{abs(days_till_10000)}")
    else:
        msg_10000 = msgs["msg_10000_past"]
    return msg_10000


def get_regen_amt(years, days, msgs):
    # get amount of skeleton that has regenerated based on your age
    # source: https://book.bionumbers.org/how-quickly-do-different-cells-in-the-body-replace-themselves/ 
    REGEN_RATE = .10 #per year
    regen_amt = (years * REGEN_RATE) + (days / 365 *REGEN_RATE)  
    if years < 10:
        msg_skeleton = msgs["msg_skeleton_percentage"].format(regen_amt=f"{regen_amt:%}")
    else: 
        msg_skeleton = msgs["msg_skeleton_replacements"].format(regen_amt=f"{regen_amt:.2f}")
    return msg_skeleton


def get_insect_amt(years, days, msgs):
    # determines how many insects you probably ate based on your age
    INSECT_RATE = 450 #grams per year
    insect_amt =  int((years * INSECT_RATE) + (days/365 *INSECT_RATE))
    msg_insect = msgs["msg_insect"].format(insect_amt=insect_amt)
    return msg_insect


def print_random_stat(years, days, age_in_days, msgs):
    # randomly selects a message to display
    msg_10000 = get_days_till_10000(age_in_days, msgs)
    msg_regen = get_regen_amt(years, days, msgs)
    msg_insect = get_insect_amt(years, days, msgs)

    stats_list = [msg_10000, msg_regen, msg_insect]
    random_stat = random.choice(stats_list)
    random_stat_msg = msgs["RANDOM_STAT"].format(random_stat=random_stat)
    print(random_stat_msg)



def get_historical_events(birthdate, language, msgs):
    # gets historical information about your birthdate from English or French Wikipedia

    date = birthdate.strftime('%m/%d')

    if language == "FR":
        url = 'https://api.wikimedia.org/feed/v1/wikipedia/fr/onthisday/all/' + date
    elif language == "EN":
        url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + date
    response = requests.get(url)
    if response.status_code == 200:
        events = response.json()
        
        # Extract titles or headers from events
        headline = []
        for event in events['events']:     # 'events' is the key containing the event data
            headline.append(event['text'])  # 'text' is the key where the title or header is stored
            return headline
    else:
        status_error_msg = msgs["STATUS_ERROR"].format(response_status_code=f"{str(response.status_code)}")
        return status_error_msg


# Main program starts here

def main():
    print()
    agefacts_messages = get_messages_agefacts()
    language = agefacts_messages["language"]
    today = datetime.now()

    # Introduction  
    print()   
    print(agefacts_messages["HEADER"])
    print()

    play_again = True
    while play_again == True:
        # input
        while True:
            birthdate_input = input(agefacts_messages["BIRTHDATE"])
            try:
                birthdate = parser.parse(birthdate_input)  # Parse the date string into a datetime object
                if birthdate > today:
                    error_msg = agefacts_messages["ERROR_MSG"]
                    print(error_msg)
                else:
                    break
            except ValueError:
              print("   Data Entry Error - Date is not in a valid format. Please enter year, month, day.")

        # calculations 
        time_since_birthdate = get_time_since_birthday(today, birthdate)
        years = time_since_birthdate["years"]
        months = time_since_birthdate["months"]
        days = time_since_birthdate["days"]
        age_in_days = time_since_birthdate["age_in_days"]
        age_in_weeks = time_since_birthdate["age_in_weeks"]
        age_in_months = time_since_birthdate["age_in_months"]
        event_on_birthdate = get_historical_events(birthdate, language, agefacts_messages)

        # format display
        age_msg = agefacts_messages["AGE_MSG"].format(years=years, months=months, days=days)
        months_msg = agefacts_messages["MONTHS_MSG"].format(age_in_months=age_in_months)
        weeks_msg = agefacts_messages["WEEKS_MSG"].format(age_in_weeks=age_in_weeks)
        days_msg = agefacts_messages["DAYS_MSG"].format(age_in_days=age_in_days)
        historical_msg = agefacts_messages["HISTORICAL_MSG"].format(event_on_birthdate=event_on_birthdate)

        # display
        print(age_msg)
        print(months_msg)
        print(weeks_msg)
        print(days_msg)
        print_random_stat(years, days, age_in_days, agefacts_messages)
        print(historical_msg)

        # housekeeping

        try_again = input(agefacts_messages["TRY_AGAIN_MSG"]).lower()
        if try_again in ["no", "non", "n"]:
            play_again = False
            print(agefacts_messages["SALUTATION"])


if __name__ == '__main__':
    main()
