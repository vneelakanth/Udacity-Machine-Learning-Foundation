import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months_Data = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
Week_day = ['monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday', 'sunday', 'all']
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
    status = 1
    while status == 1:
                    
            city = input("Select one of these cities: chicago, new york city, washington:\n").lower()
            for key in CITY_DATA:
                if key == city:                    
                    
                    status = 2
            if status != 2:
                print("Enter the name of the city properly")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    status = 1
    while status == 1:
        month = input("Enter the month or just enter all to explore data for all months:\n").lower()
        for month_data in Months_Data:
            if month_data == month:
                
                status = 2
        if status != 2:
            print("Enter the month properly")
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    status = 1
    while status == 1:
        day = input("Enter the day or just enter all to explore data for all days:\n").lower()
        for week_data in Week_day:
            if week_data == day:
                
                status = 2
        if status != 2:
            print("Enter the Weekday properly")     

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month = Months_Data.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    print(df)
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        freq_month = df['month'].mode()[0]
        print("most common month")
        print(Months_Data[freq_month-1])
        print("\n")
    else:
        print("You have selected {} month and data is filtered by this month\n".format(month))

    # TO DO: display the most common day of week
    if day == 'all':
        freq_day = df['day_of_week'].mode()[0]
        print("most common day of week")
        print(freq_day)
        print("\n")
    else:
        print("You have selected {} and data is filtered by this day".format(day))
        print("\n")
        

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    freq_hour = df['hour'].mode()[0]
    print("most common start hour")
    print(freq_hour)
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    freq_start_station = df['Start Station'].mode()[0]
    print("Most common start station")
    
    print(freq_start_station)
    print("\n")

    # TO DO: display most commonly used end station
    freq_end_station = df['End Station'].mode()[0]
    
    print("Most common end station")
    print(freq_end_station)
    print("\n")
    # TO DO: display most frequent combination of start station and end station trip
    df['comb_station'] = df['Start Station'] + '_' + df['End Station']
    
    print("Most common Combination of Start Station and End Station separated by _")
    print(df['comb_station'].mode()[0])
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Duration")
    print("{} Seconds".format(df['Trip Duration'].sum()))
    print("\n")

    # TO DO: display mean travel time
    print("Mean Travel Time")
    print("{} Seconds".format(df['Trip Duration'].mean()))
    print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print("Count of different user types")
    user_types = df['User Type'].value_counts()
    print(user_types)
    print("\n")

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("Count of Gender types")
        gender_types = df['Gender'].value_counts()
        print(gender_types)
        print("\n")
    
    else:
        print("Gender Column does not exist for the city you selected")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print("Displaying earliest, most recent, and most common year of birth")
        print("\nEarliest Birth Year: {}\n Most Recent Birth Year: {}\n Most Common Birth Year: {}\n".format(earliest,recent,common))
    else:
        print("Birth Year column does not exist for the city you selected")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
