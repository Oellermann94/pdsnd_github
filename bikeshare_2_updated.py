import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    month = "all"
    day = "all"
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # obtain city input 
    while True:
        
        city = input("\n""Which city would you like to see data for: Washington, Chicago or New York?\n")
       
        if city.strip().lower() == 'chicago':
            city = 'chicago'
            break
        
        elif city.strip().lower() == 'new york':
            city = 'new york'
            break
    
        elif city.strip().lower() == 'washington':
            city = 'washington'
            break
#            
        else:
            print('\n''The name that you have entered is invalid.  Please enter a valid city name')
                
    print("\n""It looks like you want to view data for {}. If that's not true, restart the program now!".format(city))           
     
   
    # esablish whether the user wants to filter data by day, month or not at all
    while True:
        
        day_month_fill = input("\n""Would you like to filter the data by month, day or not at all? Type 'none' for no time filter.""\n")
        day_month_fill = day_month_fill.strip().lower()
        if day_month_fill == 'month':
            break
        if day_month_fill == 'day':
            break
        if day_month_fill == 'none':
            break
        else:      
            print("\n""Please enter a valid answer")
            
    #if the user wants to filter data by month, establish by which month the user wants to filter 
    while True:
        if day_month_fill == 'month':
            month = input("\n""Which month? January, February, March, April, May or June? Please input an integer (January = 1, February = 2 etc)""\n")
            month = month.strip().lower()
            if month == "1" or month == "2" or month == "3" or month == "4" or month == "5" or month == "6":
                break
            else:
                print("\n""Please enter a valid month. Remember to use an integer")
        break
            
    #if the user wants to filter data by week day, establish by which weekday the user wants to filter 
    while True:    
        if day_month_fill == 'day':
        
            day = input("\n""Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Please enter an integer (Monday = 1, Tuesday = 2 etc)""\n")
        
            if day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6" or day == "7":
                break
            else:
                print("\n""Please enter a valid day. Remember to input an integer")    
                
        else:
            break
    
    # if the user wants no filter to run, this code will run    
    if day_month_fill == 'none':
        day = 'all'
        month = 'all'
      


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
#    if city == "new york":
#        city = "new_york_city"
             
    
    if month == "all" and day == "all":
 
        
        df = pd.read_csv(CITY_DATA[city])

    #if the user elected to filter by month, this code runs:    
    elif month != "all":   
        
        df = pd.read_csv(CITY_DATA[city])
        df1 = df["Start Time"]
        # convert sting datetime to datetime format
        month1 = pd.to_datetime(df1)
        # extract month from date time
        month_extracted = month1.dt.month
        
        # get a row of booleans where month_extracted = the month input by the user
        month_boolean = month_extracted[:] == int(month)
        # create a new dataframe with only the selected month (ie the dataframe filtered for the relevant month)
        df_month = df[month_boolean] 
        df = df_month

    #if the user elected to filter by day, this code runs:
    elif day != "all":
        df = pd.read_csv(CITY_DATA[city])
        df1 = df["Start Time"]
        # convert sting datetime to datetime format
        day1 = pd.to_datetime(df1)
        # extract day from date time
        day_extracted = day1.dt.dayofweek
        
        # get a row of booleans where day_extracted= the day input by the user
        day_boolean = day_extracted[:] == int(day)
        # create a new dataframe with only the selected day (ie the dataframe filtered for the relevant day)
        df_day = df[day_boolean]  
        df = df_day   
      
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    try:
        months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June"}
        df2 = df["Start Time"]
        # convert sting datetime to datetime format
        month2 = pd.to_datetime(df2)
        # extract month from date time
        month_extracted2 = month2.dt.month
        common_month = month_extracted2.mode()
        common_month2 = months[common_month[0]]
        print("The most common month of travel is {}.".format(common_month2))
    except:
        print("\n""There is no data for the selected month")

    # display the most common day of week
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    try:  
        common_day = month2.dt.dayofweek.mode()
        common_day2 = common_day[0]
        day_name = days[common_day2]
        print("\n""The most common day of the week is {}.".format(day_name))
    except:
        print("\n""There is no data for the selected day")
    
    # display the most common start hour
    common_hour = month2.dt.hour.mode()
    print("\n""The most common start hour is {}.".format(common_hour[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()
    print("\n""The most commonly used start station is {}.".format(common_start_station[0]))

    # display most commonly used end station
    common_end_station = df["End Station"].mode()
    print("\n""The most commonly used end station is {}.".format(common_end_station[0]))
    

    # display most frequent combination of start station and end station trip
    
    df["Combined"] = df["Start Station"] + ' ' + 'and' + ' ' + df["End Station"]
    df3 = df["Combined"]
    c_combination = df3.mode()
    print("\n""The most frequent combination(s) of start station and end station is/are: {}.".format(c_combination[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    trip_duration = df["Trip Duration"].sum()
    print("\n""The total trip duation is {}.".format(trip_duration))
    
    # display mean travel time
    avg_travel_time = df["Trip Duration"].mean()
    print("\n""The average trip travel time is {}.".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_types = df["User Type"]
    user_types_grouped = user_types.value_counts()
    print("This was the count of user types:""\n")
    print(user_types_grouped)


    # Display counts of gender
    
    try:
        gender_type = df["Gender"]
        gender_grouped = gender_type.value_counts()
        print("\n""This was the count of genders:""\n")
        print(gender_grouped)
    except:
        print("\n""There is no gender data for the selected city")

    # Display earliest, most recent, and most common year of birth
    
    try:
        b_year = df["Birth Year"]
        e_year = int(b_year.min())
        r_year = int(b_year.max())
        c_year = int(b_year.mode())
    
        print("\n""The earliest year of birth of a user is {}".format(e_year))
        print("\n""The most recent year of birth of a user is {}".format(r_year))
        print("\n""The most common year of birth of users is {}".format(c_year))
    except:
        print("\n""There is no birth year data for the selected city")
    

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
        
        #ask the user whether he/she wants to see the raw data and how many rows of the raw data
        while True:
            raw_data = input("\n""Would you like to view the raw data? Please answer 'yes' or 'no'""\n")  

            if raw_data.strip().lower() == 'yes':    
                while True:
                    try:
                        raw_input = int(input("How many rows of data would you want to view? Please input an integer""\n"))
                        break
                    except:
                        print("Please input an integer")
       
                raw_input_int = raw_input
                df4 = df.head(raw_input_int)
                print(df4)
                break
            
            elif raw_data.strip().lower() == 'no':
                break
            
            elif raw_data.strip().lower() != 'no' or raw_data.strip().lower() != 'yes':
                print("\n""Please enter a valid answer. You must answer 'yes' or 'no'.")
            
    
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
