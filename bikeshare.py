import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_NAMES = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
WEEK_DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    city = ""
    while city not in CITY_DATA:
        city = input("Please enter chicago, new york city or washington\n").lower()
        if city not in CITY_DATA:
            print("sorry we are unable to analize data for city: {}.\n".format(city))

    city = CITY_DATA[city]

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while month not in MONTH_NAMES:
        month = input("Please enter january, february, march, april, may, june or all\n").lower()
        if month not in MONTH_NAMES:
            print("Sorry we are unable to analize data for month: {}.\n".format(month))
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in WEEK_DAYS:
        day = input("Please enter monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all\n").lower()
        if day not in WEEK_DAYS:
            print("sorry we are unable to analize data for day: {}.\n".format(day))
    
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

    df = pd.read_csv(city)
    #convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day to create a new column in order to filter.
                    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['weekday'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    #Filter by month
    if month != 'all':
        month = MONTH_NAMES.index(month)
        df = df[df['month'] == month]

    #Filter by day
    if day != 'all':
        day = WEEK_DAYS.index(day) - 1
        df = df[df['weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    usual_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(MONTH_NAMES[usual_month]))
                  
    # TO DO: display the most common day of week
    usual_day_of_week = df['weekday'].mode()[0]
    print('The most common day of the week is: {}'.format(WEEK_DAYS[usual_day_of_week + 1]))

    # TO DO: display the most common start hour
    usual_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(usual_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(commonly_start_station))

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(commonly_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination_stations = df['Start Station'] + ' to ' + df['End Station']
    
    frequent_combination_stations = combination_stations.mode()[0]
    print('The most frequent combination of start station and end station is: {}'.format(frequent_combination_stations))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_traveltime = df['Trip Duration'].sum()

    #convert seconds in minutes
    minutes, seconds = divmod(total_traveltime, 60)
    #convert minutes in hours
    hours, minutes = divmod(minutes, 60)
    print("The total travel time is: {} hours, {} minutes and {} seconds".format(hours, minutes, seconds))
          
     # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    minutes_m, seconds_m = divmod(average_duration, 60)
    hours_m, minutes_m = divmod(minutes_m, 60)
    print("The mean travel time is: {} hours, {} minutes and {} seconds".format(hours_m, minutes_m, seconds_m))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()
    print('The number of different user types are:\n{}\n'.format(count_users))
       
    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Sorry, Gender data not available for this city')
    else:
       gender_counts = df['Gender'].value_counts()
       print('The genders are:\n{}\n'.format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth year data not available')
    else:
        earliest_birthyear = df['Birth Year'].min()
        print('The earliest birth year is: {}'.format(earliest_birthyear))

        mostrecent_birthyear = df['Birth Year'].max()
        print('The most recent bith year is: {}'.format(mostrecent_birthyear))

        mostcommon_birthyear = df['Birth Year'].mode()[0]
        print('The most common year of birth is: {}'.format(mostcommon_birthyear))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Asks user if wants to show raw data 5 lines at a time"""
    row = 0
    end_row = 0
    max_row = len(df.index)

    show_raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no please.\n').lower()
    while show_raw_data == 'yes' and end_row < max_row: 
        end_row = row + 5
        if end_row > max_row:
            end_row = max_row

        print(df.iloc[row:end_row])
        row = end_row
        show_raw_data = input('\nWould you like to see the next 5 lines of raw data? Enter yes or no please.\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no please.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
