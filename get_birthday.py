from datetime import datetime, timedelta


def get_birthday_per_week(users): 

    # set up todays date
    today = datetime.today().date()



    birthday_ppl = {}


    # function itterates over each user in users list, check their birthday's date,
    # and change it to type(data).
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        

        # checks if bithday alr happend this year
        if birthday_this_year < today:
            birthday_next_year = birthday_this_year.replace(year=today.year + 1)
            delta_days = (birthday_next_year - today).days
            
        # calculate how much days left from today to the birday of the user
        else:
            delta_days = (birthday_this_year - today).days


        # checks if the birday is in less that 7 days
        if 0 < delta_days < 7:

            # if birthday is during the week day, add it to the dict{day:name}
            if birthday_this_year.weekday() <= 4:
                day_name = birthday_this_year.strftime('%A')
                if day_name not in birthday_ppl:
                    birthday_ppl[day_name] = [name]
                else:
                    birthday_ppl[day_name].append(name)

            # if birthday is on the weekend, add it to the following Monday (dict{following_monday:name})
            elif birthday_this_year.weekday() >= 5:
                days_until_monday = (7 - today.weekday()) % 7
                following_monday = today + timedelta(days=days_until_monday)
                day_name = following_monday.strftime("%A")
                if day_name not in birthday_ppl:
                    birthday_ppl[day_name] = [name]
                else:
                    birthday_ppl[day_name].append(name)


    if len(birthday_ppl) >= 1:
        for day, names in birthday_ppl.items():
            print(f"{day}: {', '.join(names)}")
    else:
        print(f"No birthdays this week")





def main():

    # list with names and birthday dates
    users = [
        {"name": "John Doe", "birthday": datetime(1985, 7, 15)},
        {"name": "Jane Smith", "birthday": datetime(1990, 5, 20)},
        {"name": "Michael Johnson", "birthday": datetime(1982, 11, 10)},
        {"name": "Emily Davis", "birthday": datetime(1988, 9, 25)},
        {"name": "James Wilson", "birthday": datetime(1979, 3, 5)},
        {"name": "Sarah Brown", "birthday": datetime(1995, 12, 30)},
        {"name": "Robert Lee", "birthday": datetime(1987, 8, 18)},
        {"name": "Jennifer Taylor", "birthday": datetime(1984, 6, 12)},
        {"name": "David Harris", "birthday": datetime(1992, 4, 8)},
        {"name": "Lisa Clark", "birthday": datetime(1981, 2, 28)},
        {"name": "Daniel Anderson", "birthday": datetime(1993, 10, 22)},
        {"name": "Jessica Baker", "birthday": datetime(1989, 1, 7)},
        {"name": "Matthew Carter", "birthday": datetime(1986, 11, 2)},
        {"name": "Laura Evans", "birthday": datetime(1980, 7, 18)},
        {"name": "Kevin Foster", "birthday": datetime(1991, 9, 12)},
        {"name": "Amanda Green", "birthday": datetime(1983, 3, 29)},
        {"name": "Jason Harris", "birthday": datetime(1987, 6, 8)},
        {"name": "Megan Johnson", "birthday": datetime(1994, 5, 13)},
        {"name": "Patrick King", "birthday": datetime(1989, 8, 24)},
        {"name": "Samantha Lee", "birthday": datetime(1985, 12, 9)},
        {"name": "Brian Mitchell", "birthday": datetime(1993, 4, 16)},
        {"name": "Jack Mit", "birthday": datetime(1992, 10, 17)},
        {"name": "Ivory Ross", "birthday": datetime(1967, 10, 20)},
        {"name": "Kally Ross", "birthday": datetime(1967, 10, 20)},
        {"name": "Brian Wang", "birthday": datetime(1997, 10, 16)}
    ]

    get_birthday_per_week(users)


if __name__ == "__main__":
    main()


