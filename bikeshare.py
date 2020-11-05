import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday', 'all']

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
    
    city_name = ''
    
    while city_name.lower() not in CITY_DATA:
        city_name = input('Write the name of the city you want to explore')
        if city_name.lower() in  CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print('Available data only for chicago, new york city and washington')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_name = ''
    
    while month_name.lower() not in MONTH_DATA:
        month_name = input('Write the month you want to explore. Type all if you don\´t want filters')
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
        else:
            print('Available data only for months from january to june or all')
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_name = ''
    
    while day_name.lower() not in DAY_DATA:
        day_name = input('Write the day of the week you want to explore. Type all if you don\´t want filters')
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
        else:
            print('Available data only for name of days of the week')
        
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':     
       df = df[df['day'] == day.title()]   
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print(df['month'].mode()[0])

    # TO DO: display the most common day of week

    print(df['day'].mode()[0])

    # TO DO: display the most common start hour

    df['hour'] = df['Start time'].dt.hour
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station

    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    
    df['Combination'] = df['Start Station'] + "to" + df['End Station']
    print(df['Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time

    print(df['Trip Duration'].mean())
             
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    Type = df['User Type'].value_counts()
    print(Type)
                         
    # TO DO: Display counts of gender
    try:
        Gender = df['Gender'].value_counts()
        print(Gender)
    except:
        print('No Gender info for this city')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:    
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
    
        print(earliest)
        print(recent)
        print(common)
    
    except:
        print('No Birth info for this city')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 more rows of individual trip data? Enter yes or no\n')
        if view_data != 'yes':
            return
        start_loc += 5
        print(df.iloc[start_loc: start_loc + 5])
        
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
