import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'C:\Users\Compumundo\Desktop\Data Science\FreeCODECAMP\boilerplate demographic\adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').count()['age'].sort_values(ascending=0)

    # What is the average age of men?
    average_age_men = round(df.groupby(df.sex).mean().loc['Male','age'],1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.groupby(df.education).count().loc['Bachelors','age']/df.count()[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = round(df[(df.salary == '>50K') &  ((df.education == 'Bachelors') | (df.education == 'Doctorate') | (df.education == 'Masters'))].count()[0]/\
df[((df.education == 'Bachelors') | (df.education == 'Doctorate') | (df.education == 'Masters'))].count()[0]*100,1)

    lower_education = round(df[(df.salary == '>50K') &  ~((df.education == 'Bachelors') | (df.education == 'Doctorate') | (df.education == 'Masters'))].count()[0]/\
df[~((df.education == 'Bachelors') | (df.education == 'Doctorate') | (df.education == 'Masters'))].count()[0]*100,1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
  
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    rich_percentage = int(df[(df['hours-per-week'] == df['hours-per-week'].min()) & (df.salary == '>50K')].count()[0]\
    / df[df['hours-per-week'] == df['hours-per-week'].min()].count()[0]*100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[(df.salary == '>50K')].groupby('native-country').count()/\
    df.groupby('native-country').count()).sort_values(by='age',ascending=0).index[0]
    highest_earning_country_percentage = round((df[(df.salary == '>50K')].groupby('native-country').count()/\
    df.groupby('native-country').count()).sort_values(by='age',ascending=0).iloc[0,0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df.salary == '>50K') & (df['native-country'] == 'India')].groupby('occupation').count().sort_values(by='age',ascending=0).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
