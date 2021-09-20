import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
months = {"january": 1, "february": 2, "march": 3, 'april': 4, 'may': 5, 'june': 6}
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(
            input("Which city would you like to see data for: Chicago, New York, or Washington?\n")).lower().strip()
        if city == "chicago" or city == "new york" or city == "washington":
            break
        else:
            print("Invalid city, please try again")

    while True:
        date_filter = str(input('Do want to filter the data by month, day, both, or none\n')).lower().strip()
        if date_filter == "month" or date_filter == "day" or date_filter == "both" or date_filter == "none":
            break
        else:
            print("Invalid input, please try again")

    # get user input for month (all, january, february, ... , june)
    if date_filter == "month" or date_filter == "both":
        while True:
            month = str(
                input("Enter the name of the month: january, february, march, april, may, june\n")).lower().strip()
            if month in months:
                break
            else:
                print("Invalid input, please try again")
    else:
        month = "all"
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if date_filter == "day" or date_filter == "both":
        while True:
            day = str(input("Enter the name of the day:\n")).lower().strip()
            if day in days:
                break
            else:
                print("Invalid input, please try again")
    else:
        day = "all"
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday

    if month != "all":
        month = months[month]
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == days.index(day)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
     Args:
        (DataFrame) df - Pandas DataFrame containing city data"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = int(df["month"].mode()[0])
    for key, value in months.items():
        if value == common_month:
            common_month = key
            break
    print("The most popular month is:\n" + common_month.title())
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()

    # display the most common day of week
    common_day = days[df["day_of_week"].mode()[0]]
    print("The most popular day of the week is:\n" + common_day.title())
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()

    # display the most common start hour
    common_hour = df["Start Time"].dt.hour.mode()[0]
    print("The most popular hour of the day is:\n" + str(common_hour))
    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40 + "\n")


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The most popular start station is:\n" + common_start_station)
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()
    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("The most popular end station is:\n" + common_end_station)
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()

    # display most frequent combination of start station and end station trip
    common_start_end_combination = ("Start: " + df["Start Station"] + "\nEnd: " + df["End Station"]).mode()[0]
    print("The most popular combination of start station and end station is:\n" + common_start_end_combination)
    print("This took %s seconds.\n" % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_time = df["Trip Duration"].sum()
    print("The total travel time is:\n" + str(total_time))
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()
    # display mean travel time
    avg_time = df["Trip Duration"].mean()
    print("The average travel time is:\n" + str(avg_time))
    print("This took %s seconds.\n" % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The count of each user type is: \n" + str(user_types))
    print("This took %s seconds.\n" % (time.time() - start_time))

    if city == "washington":
        return
    start_time = time.time()
    # Display counts of gender
    gender_counts = df["Gender"].value_counts()
    print("The count of each gender is: \n" + str(gender_counts))
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()

    # Display earliest, most recent, and most common year of birth
    min_year = int(df["Birth Year"].min())
    print("The earliest year of birth is: \n" + str(min_year))
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()

    max_year = int(df["Birth Year"].max())
    print("The most recent year of birth is: \n" + str(max_year))
    print("This took %s seconds.\n" % (time.time() - start_time))
    start_time = time.time()

    common_year = int(df["Birth Year"].mode())
    print("The most common year of birth is: \n" + str(common_year))
    print("This took %s seconds.\n" % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """Display some row data on user request
    Args:
        (DataFrame) df - Pandas DataFrame containing city data"""

    valid_ans = ["yes", "no"]
    nxt = 0
    while True:
        x = str(input("Do you want to print data about some trips? Enter yes or no.\n")).lower().strip()
        if x not in valid_ans:
            print("Invalid input, please try again")
            continue
        elif x == "no":
            break
        elif x == "yes":
            print(df.iloc[nxt:nxt + 5])
            nxt += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
