import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! My name is Python.Js and i\'m delighted to be your acquaintance  to walk through some US bikeshare data with you!')
    print()
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Now, Bikeshare Data is only available for New York, Chicago And Washington. Enter city here: ').lower()
    while city not in CITY_DATA:
        city = input('Invalid city name. Try Again?: ').lower()

    print()
    # get user input for month (all, january, february, ... , june)
    month = input('Again, Bikeshare Data is only available from January to June. \nSelect the month you want to explore or enter "all" \nto explore all the months simultaneously here: ')
    MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in MONTHS:
        month = input('Invalid month name entered. Try Again?: ').title()

    print()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a specific day of the week or \nenter "all" to explore all days of the week simultaneously: ').lower()
    DAYS = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
    while day not in DAYS:
        day = input('Invalid day name! Try Again?: ').lower()

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create month column
    df['month'] = df['Start Time'].dt.month

    #create weekdays column
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name

    #create Time column
    df['Hour'] = df['Start Time'].dt.hour


    #create a dataframe filtered with only a specified month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_the_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

     # create a month column
    df['month'] = df['Start Time'].dt.month

    # display the most common month
    MONTHS = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    Most_common_month = df['month'].value_counts().idxmax()
    print('Most common month for Travelling is: ', Most_common_month)

     #create weekdays column
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name

    # display the most common day of week
    DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
    Most_common_day_of_the_week = df['day_of_the_week'].mode()[0]
    print('The most common day of the week for Travelling is: ', Most_common_day_of_the_week)


    #create Time column
    df['Hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    Most_preferred_hour = df['Hour'].mode()[0]
    print('The most preferred time for traveling is: ', Most_preferred_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Most_preferred_start_station = df['Start Station'].value_counts().idxmax()
    print('The most preferred Start Station is: ', Most_preferred_start_station)

    # display most commonly used end station
    Most_preferred_end_station = df['End Station'].value_counts().idxmax()
    print('The most preferred End Station is: ', Most_preferred_end_station)


    # display most frequent combination of start station and end station trip
    Most_preferred_Start_End_Trip = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most preferred Start-End Trip is from {} to {}.'.format(Most_preferred_Start_End_Trip[0], Most_preferred_Start_End_Trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_time_travel = df['Trip Duration'].sum()
    print('Total time travel is {} seconds.'.format(Total_time_travel))


    # display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('Average Total Trip duration is {} seconds.'.format(Mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('categories of users: ''\n', User_Types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Total gender counts = \n', gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        Earliest_birth_year = df['Birth Year'].min()
        Recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('Earliest birth year is {}, Recent birth year {} and common birth year is {}.'.format(Earliest_birth_year, Recent_birth_year, common_birth_year))


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
