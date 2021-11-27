from constants.prompt_selections import SP


class SP(object):
    # Prompt Selections
    PG = SP.PG.value if SP.PG.value else 'All Shoppers'
    PG_U = PG.upper()
    COMP_PG = SP.COMP_PG.value if SP.COMP_PG.value else 'All Shoppers'
    COMP_PG_U = COMP_PG.upper()
    # Demographics Tab Table Headers
    DEMO_STATIC_HEAD = [None, '% ' + PG_U + ', FOCUS', '% ' + COMP_PG_U + ', BENCHMARK', 'INDEX']
    # Traditional Demographics Dropdown
    DEMO_DROP = ['Traditional Demographics', 'Amazon Prime Focused', 'Latino/Hispanic Focused',
                 'Children Focused', 'Trip Focused', 'Lifestages/Lifestyles']
    # Traditional Demographics Headers and Tables
    DEMO_HEAD = [
        # Traditional Demographics Header
        ['AGE (GENERATION)', 'AGE (BRACKETS)', 'INCOME BUCKET', 'INCOME $', 'ETHNICITY', 'GENDER (APP OWNER)',
         'EDUCATION', 'EMPLOYMENT', 'HOUSEHOLD SIZE', 'MARITAL STATUS', 'URBANICITY', 'CENSUS DIVISION'],
        # Amazon Header
        ['AMAZON PRIME'],
        # Latino/Hispanic Header
        ['HISPANIC ACCULTURATION', 'HISPANIC IDENTIFICATION',
         'LANGUAGE PREFERENCE (SPOKEN)', 'LANGUAGE PREFERENCE (TV)'],
        # Children Header
        ['HAS CHILDREN', 'HAS CHILDREN (AGES 0-5)', 'HAS CHILDREN (AGES 6-12)', 'HAS CHILDREN (AGES 13-17)'],
        # Trip Header
        ['ADULT GENDERS ON TRIP', 'KIDS PRESENT ON TRIP'],
        # Lifestages/Lifestyles Header
        ['LIFESTAGE', 'LIFESTYLE']]
    # Traditional Demographics Tables
    DEMO_TABLE = [
        # Traditional Demographcis Table
        ['Gen Z [> 1996]', 'Millennials [1982-1995]', 'Gen X [1965-1981]', 'Boomers [1945-1964]', 'Seniors [< 1945]',
         '18-20', '21-24', '25-34', '35-44', '45-54', '55-64', '65+',
         'Low Income (Under $40k)', 'Middle Income ($40k-$80k)', 'High Income (Over $80k)',
         '- $20k', '$20k-40k', '$40k-60k', '$60k-80k', '$80k-100k', '$100k-125k', '$125k +',
         'White/Caucasian', 'Black or African American', 'Hispanic/Latino', 'Asian', 'Other',
         'Female', 'Male', 'Other',
         'Less than high school', 'High School/GED', 'Some College or university', '2 year College Degree',
         '4 year College Degree', 'Some Graduate School', 'Graduate Degree', 'Trade/Technical Degree',
         'Employed Full-Time', 'Employed Part-Time', 'Self Employed', 'Active Military',
         'Retired', 'Homemaker', 'Student', 'Disabled', 'Unemployed',
         '1', '2', '3', '4', '5', '6', '7+',
         'Married', 'Living with partner', 'Separated', 'Widower', 'Divorced', 'Never married',
         'Rural', 'Suburban', 'Urban',
         'East North Central', 'East South Central', 'Mid-Atlantic', 'Mountain', 'New England',
         'Pacific', 'South Atlantic', 'West North Central', 'West South Central'],
        # Amazon Table
        ['Prime', 'Prime Student', 'Prime Video', 'Secondary'],
        # Latino/Hispanic Table
        ['Acculturated', 'Semi-Acculturated', 'Unacculturated',
         'American', 'Both', 'Hispanic / Latino',
         'Bilingual', 'English-Preferred', 'Spanish-Preferred',
         'Bilingual', 'English-Preferred', 'Spanish-Preferred'],
        # Children Table
        ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
        # Trip Table
        ['Female Adult Only', 'Male Adult Only', 'Male and Female Adult on trip',
         'Kids Present', 'No Kids'],
        # Lifestages/Lifestyles Table
        ['New Family', 'Small Family', 'Large Younger Family', 'Large Older Family', 'Young Singles', 'Young Couples',
         'Adult Singles', 'Adult Couples', 'Senior Singles', 'Senior Couples', 'Unclassified',
         'Urban Affluent', 'Urban Middle Class', 'Urban Struggling', 'Suburban Affluent', 'Suburban Middle Class',
         'Suburban Struggling', 'Rural Affluent', 'Rural Middle Class', 'Rural Struggling']]
    # Basic Metrics Tab Headers and Table
    METRIC_HEAD = ['METRIC', PG_U + ', FOCUS', COMP_PG_U + ', BENCHMARK', 'INDEX']
    METRIC_TABLE = ['Household Penetration', 'Projected Sales', 'Purchase Frequency',
                    'Spend Per Trip', 'Buy Rate', 'Avg Basket Spend', 'Avg Basket Units']
    # Top Stores Dropdowns
    STORES_DROP = ['Banner', 'Channel', 'Retailer']
    # Top Stores Tab Legends
    STORES_LEG = [
        # Spend Legend
        ['% of Focus Spend', '% of Benchmark Spend'],
        # Household Legend
        ['% of Focus Households', '% of Benchmark Households']]
    # Top Stores Tab Spend Header
    STORES_HEAD = [
        # Spend Header
        ['STORE', '% OF ' + PG_U + ' SPENDING, FOCUS',
         '% OF ' + COMP_PG_U + ' SPENDING, BENCHMARK', 'INDEX (% SPEND)'],
        # Household Header
        ['STORE', '% OF ' + PG_U + ' HHS, FOCUS', '% OF ' + COMP_PG_U + ' HHS, BENCHMARK', 'INDEX (% HHS)']]
    # Payment Tab Dropdowns
    PAY_DROP = ['ALL CHANNELS', 'Club', 'Dollar', 'Food', 'Mass']
    # Payment Tab Legends
    PAY_LEG = [
        # Percent Legend
        [PG, COMP_PG],
        # Index Legend
        [PG + ' vs ' + COMP_PG]]
    # Payment Tab Header
    PAY_HEAD = ['PAYMENT METHOD', '% OF ' + PG_U + ' TRIPS, FOCUS',
                '% OF ' + COMP_PG_U + ' TRIPS, BENCHMARK', 'INDEX (% TRIPS)']
    # Payment Tab Table
    PAY_TABLE = ['CREDIT', 'DEBIT', 'CASH', 'SNAP', 'GIFTCARD', 'WIC']
    # Timing Tab Headers
    TIME_STATIC_HEAD = [None, '% ' + PG_U + ' SPENDING, FOCUS', '% ' + COMP_PG_U + ' SPENDING, BENCHMARK',
                        'INDEX (% SPENDING)', '% ' + PG_U + ' TRIPS, FOCUS',
                        '% ' + COMP_PG_U + ' TRIPS, BENCHMARK', 'INDEX (% TRIPS)']
    # Timing Tab Dropdowns
    TIME_DROP = ['Day of Week', 'Day of Month', 'Week of Month', 'Month', 'Quarter']
    # Timing Tab Legends
    TIME_LEG = [
        # Percent Legend
        [PG, COMP_PG],
        # Index Legend
        [PG + ' vs ' + COMP_PG]]
    # Timing Tab Headers
    TIME_HEAD = ['DAY OF WEEK', 'DAY OF MONTH', 'WEEK OF MONTH', 'MONTH', 'QUARTER']
    TIME_TABLE = [
        # Day of Week
        ['Friday', 'Saturday', 'Sunday'],
        # Day of Month
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
         '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        # Week of Month
        ['1st', '2nd', '3rd', '4th', '5th (Partial)'],
        # Month
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        # Quarter
        ['1', '2', '3', '4']]
    # Trip Type Tab Dropdowns
    TRIP_DROP = ['Trips', 'Spend']
    # Trip Type Tab Legends
    TRIP_LEG = [
        # Percent Legend
        [PG, COMP_PG],
        # Index Legend
        [PG + ' vs ' + COMP_PG]]
    # Trip Type Tab Headers
    TRIP_HEAD = [
        # Trips Header
        ['TRIP TYPE', '% TRIPS ' + PG_U + ', FOCUS', '% TRIPS ' + COMP_PG_U + ', BENCHMARK', 'TRIP INDEX'],
        # Spend Header
        ['TRIP TYPE', '% SPEND ' + PG_U + ', FOCUS', '% SPEND ' + COMP_PG_U + ', BENCHMARK', 'SPEND INDEX']]
    # Trip Type Tab Table
    TRIP_TABLE = ['Urgent Need (1-2 Items)', 'Express Lane (3-10 Items)',
                  'Fill Up (11-20 Items)', 'Pantry Stocking (21+ Items)']
