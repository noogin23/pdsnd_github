import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'csv/chicago.csv',
              'new york city': 'csv/new_york_city.csv',
              'washington': 'csv/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please input a city to anaylyze (i.e. chicago, new york city, washington): ").lower()
    city_list = ["all","chicago","new york city","washington"]
    while city not in city_list:
        city = input("Please input a correct city (i.e. chicago, new york city, washington): ").lower()
    print('-'*40)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which of the month between january and jure are you interested in (i.e. all, january, february, ..., june): ").lower()
    month_list = ["all", "january", "february", "march", "april", "may", "june"]
    while month not in month_list:
        month = input("Please input a correct month (i.e. all, january, february, ..., june): ").lower()
    print('-'*40)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week are you interested in (i.e. all, monday, tuesday, ..., sunday): ").lower()
    day_list = ["all","monday","tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
    while day not in day_list:
        day = input("Please input a correct day (i.e. all, monday, tuesday, ..., sunday): ").lower()
    print('-'*40)
    print("city: {}, month: {}, day: {}".format(city,month,day))
    print('-'*40)
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print (common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print (common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print (common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print ('Most Commonly used Start Station:',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print ('Most Commonly used End Station: ',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df.insert(5,'Frequent Trip', df['Start Station'].astype(str) + " + " + df['End Station'].astype(str))
    frequent_trip = df['Frequent Trip'].mode()[0]
    print ('Most frequent trip:',frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time (sec): ',total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean Travel Time (sec): ',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_types)
    except KeyError:
        print('\nNo Gender Data Available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print ('Earliest birth year: ', int(df['Birth Year'].min()))
        print ('Most Recent birth year: ',int(df['Birth Year'].max()))
        print ('Most Common birth year: ', int(df['Birth Year'].mode()[0]))
    except KeyError:
        print('\nNo Birth Data Available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displaying filtered raw data"""

    #Code to display raw filtered data 5 rows at a time
    n = 0 #inititating row variable
    view_data = input('\nWould you like to see the raw data? Enter Yes or No.\n').lower()
    while view_data == 'yes':
        print(df.loc[n:n+4])
        view_data = input('\nWould you like to see more data? Enter Yes or No.\n').lower()
        if view_data == 'yes':
            n += 5

    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
