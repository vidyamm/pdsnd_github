import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data and see some analysis!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_name = input(print("\nEnter which city (Chicago, New York, Washington), you want to see: \n" ))
        city = city_name.lower()
        #if (city in ['chicago','new york','washington']):
        if city in CITY_DATA.keys():

            #print("Thanks for selecting: {} city\n".format(city))
            break
        else:
            print("Please enter: Chicago, New York or Washington! ")
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        month_name = input(print("\nEnter which month (all, january, february, march, april, may, june), you want to see: \n" ))
        month = month_name.lower()
        if (month in ['all','january','february', 'march', 'april', 'may', 'june']):
            #print("\nThanks for selecting: {}\n".format(month))
            break
        else:
            print("\nPlease enter: all, january, february, march, april, may, june!\n")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_name = input(print("Enter which day (all, monday, tuesday,..), you want to see: " ))
        day = day_name.lower()
        if (day in ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']):
            #print("\nThanks for selecting: {}\n".format(day))
            break
        else:
            print("\nPlease enter: all, monday, tuesday, ... sunday!\n")
            continue

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month]

    # filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode().loc[0]
    print("\nThe most common or popular month for travel is: ", popular_month)


    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_week = df['day_of_week'].mode().loc[0]
    print("\nThe most common day of week for traveling is: ", most_common_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().loc[0]
    print("\nThe most common or popular hour for traveling is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode().loc[0]
    print("\nPopular start station: ", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode().loc[0]
    print("\nPopular end station: ", popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print ("\nPopular start and end stations are: {} and {} ".format(popular_start_end_station[0], popular_start_end_station[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nTotal travel time in hours: {}".format((total_travel_time)/3600))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nMean Travel time in seconds: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nUser Type Counts: \n", user_types)


    # Display counts of gender
    if 'Gender' not in df:
        print("\nNo gender available in this data!")
    else:
         # Display counts of gender
        gender = df['Gender'].value_counts()
        print("\nGender Counts: \n", gender)

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode().loc[0]
        print("\nEarliest_birth_year : ", earliest_birth_year)
        print("\nMost recent_birth_year : ", recent_birth_year)
        print("\nMost common_birth_year : ", most_common_birth_year)

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
