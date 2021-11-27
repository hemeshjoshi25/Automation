from constants.prompt_selections import PSY


class PSY(object):
    # Prompt Selections
    PG = PSY.PG.value.upper() if PSY.PG.value else 'ALL SHOPPERS'
    COMP_PG = PSY.COMP_PG.value.upper() if PSY.COMP_PG.value else 'ALL SHOPPERS'
    # Psychograhpics Tab Headers
    PSY_HEAD = ['{}', '% ' + PG, '% ' + COMP_PG, 'INDEX']
    # Advertising Tab Headers & Tables
    ADV_HEAD = ['EXPOSED TOUCHPOINTS', 'MOST INFLUENTIAL TOUCHPOINTS', 'ADVERTISING ASSOCIATIONS']
    ADV_TABLE = [
        # Exposed Touchpoints
        'Television', 'Print media', 'Online Web', 'Online Mobile Device', 'Radio', 'Outdoor advertising',
        'In-Store', 'Social media', 'Special events', 'Promotional emails / texts', 'Catalogs / Brochures',
        # Most Influential Touchpoints
        'Television', 'Print media', 'Online Web', 'Online Mobile Device', 'Radio', 'Outdoor advertising',
        'In-Store', 'Social media', 'Special events', 'Promotional emails / texts', 'Catalogs / Brochures',
        # Advertising Associations
        'Keeps me up-to-date', 'Doubts advertising claims', 'Advertising is manipulative',
        'Advertising is entertaining', 'Advertising is annoying', 'Trusts advertised brands',
        'Avoids ads', 'Seeks relevance']
    # Eating Tab Headers & Tables
    EAT_HEAD = ['DIETS IN THE HOUSEHOLD', 'ALLERGIES IN THE HOUSEHOLD', 'DINING IN, COOKING RESPONSIBILITIES',
                'DINING IN, COOKING ATTITUDES', 'DINING IN, SHOPPING ATTITUDES', 'DINING OUT, FREQUENCY',
                'DINING OUT, REASONS', 'DINING OUT, PREFERENCES']
    EAT_TABLE = [
        # Diets in the Household
        'Vegan', 'Vegetarian (w/Eggs)', 'Vegetarian (w/Dairy)', 'Vegetarian (w/Eggs, Dairy)',
        'Pescatarian', 'Gluten-free', 'Lactose-free', 'None of the above',
        # Allergies in the Household
        'Peanuts', 'Tree nuts', 'Milk', 'Eggs', 'Wheat', 'Soy', 'Fish', 'Shellfish', 'None of the above',
        # Dining In, Cooking Responsibilities
        'Primary cook / meal maker', 'Shares responsibilities', 'Rarely involved',
        # Dining In, Cooking Attitudes
        'Seeks recipes', 'Cooks from scratch', 'Cooks different types of food', 'Sticks to cooking comfort zone',
        'Does not enjoy cooking', 'Picky eaters at home', 'Creative cook', 'None of the above',
        # Dining In, Shopping Attitudes
        'Seeks quick-and-easy solutions', 'Seeks natural / organic foods', 'Needs help in the kitchen',
        'Reviews labels / ingredients', 'Seeks local produce / products', 'Guilt-ridden when not cooking',
        'Meal planner', 'None of the above',
        # Dining Out, Frequency
        '6+ times per week', '4-5 times per week', '2-3 times per week', 'Once per week', 'Less than once per week',
        # Dining Out, Reasons
        'Satisfy a craving', 'Try new things', 'Spend time with others', 'Change of scenery', 'Save time',
        'Eat on-the-run', 'Treat myself', 'Treat my family', 'Too busy to cook', 'Travelling / Not at home',
        'Get food for child(ren)', 'None of the above',
        # Dining Out, Preferences
        'Prefer local / independent', 'Will pay for convenience', 'Wants natural / organic items',
        'Fast food is last resort', 'Does not think about food much', 'Budget-focused', 'Some favorites are chains',
        'Mealtime is family time', 'Adventurous eater', 'None of the above']
    # Health & Sustainability Headers & Tables
    HEALTH_HEAD = ['ORGANIC COMMITMENT', 'ORGANIC PRICE PREMIUMS', 'ORGANIC ASSOCIATIONS', 'DO YOU RECYCLE?',
                   'CONCERN FOR THE ENVIRONMENT', 'GREEN PRICE PREMIUMS', 'ACTIVITY LEVEL',
                   'EATING HEALTHY, LEVEL OF CONCERN', 'HEALTH & WELLNESS ATTITUDES']
    HEALTH_TABLE = [
        # Organic Commitment
        'Very committed', 'Committed', 'Somewhat committed', 'Slightly committed', 'Not at all committed',
        # Organic Price Premiums
        'Would pay any price', 'Would pay slight premium', 'Would buy at price parity',
        'Would buy if on sale / cheap', 'Would not buy',
        # Organic Associations
        'Better regulated', 'Healthier', 'Taste better', 'Fresher', 'Safer', 'Better for the environment',
        'To support organic movement', 'For social / peer approval', 'Rarely considers organics',
        # Do You Recycle?
        'Almost always', 'Usually', 'Occasionally', 'Not usually', 'Almost never',
        # Concern for the Environment
        'Extremely concerned', 'Moderately concerned', 'Somewhat concerned',
        'Slightly concerned', 'Not at all concerned',
        # Green Price Premiums
        'Would pay any price', 'Would pay slight premium', 'Would buy at price parity',
        'Would buy if lowest price', 'Would not buy',
        # Activity Level
        'Very active', 'Active', 'Somewhat active', 'Slightly active', 'Not at all active',
        # Eating Healthy, Level of Concern
        'Very concerned', 'Concerned', 'Somewhat concerned', 'Slightly concerned', 'Not at all concerned',
        # Health & Wellness Attitudes
        'Stays updated on health trends', 'Reviews nutrition labels', 'Uses homeopathic remedies',
        'Exercises regularly', 'No time to take care of self', 'Takes vitamins / supplements', 'Watches weight',
        'Physically fit', 'Carefree eater / drinker', 'Watches diet', 'Family needs trump self', 'None of the above']
    # Household Headers & Tables
    HH_HEAD = ['FINANCIAL SITUATION (LAST YEAR)', 'FINANCIAL SITUATION (THIS YEAR)', 'FINANCIAL ATTITUDES',
               'OWNERSHIP, HOME APPLIANCES', 'OWNERSHIP, KITCHEN APPLIANCES (LARGE)',
               'OWNERSHIP, KITCHEN APPLIANCES (SMALL)', 'HOUSING STRUCTURE', 'OWN OR RENT', 'LENGTH OF RESIDENCE',
               'TRANSPORTATION MODES', 'NO. OF VEHICLES', 'VEHICLE FUEL TYPES']
    HH_TABLE = [
        # Financial Situation (Last Year)
        'Better than the year before', 'Same as the year before', 'Worse than the year before',
        # Financial Situation (This Year)
        'Better than last year', 'Same as last year', 'Worse than last year',
        # Financial Attitudes
        "Is a 'spender' not a 'saver'", 'Puts money aside into savings', 'Tends to buy care-free',
        'Saves first for large expenses', 'Puts off savings for now', 'Comfortable buying on credit',
        'Keeps close eye on budget', 'Uncomfortable with debt', 'Overwhelmed with burdens',
        'Important to plan for future', 'None of the above',
        # Ownership, Home Appliances
        'Washer', 'Dryer', 'Clothes iron', 'Clothes steamer', 'Humidifier', 'Vacuum cleaner (upright)',
        'Vacuum cleaner (handheld)', 'Vacuum cleaner (robot)', 'None of the above',
        # Ownership, Kitchen Appliances (Large)
        'Dishwasher', 'Kegerator / Draft beer system', 'Wine fridge', 'Mini-fridge', 'Fridge / Freezer (Garage)',
        'Fridge / Freezer (Basement)', 'Fridge / Freezer (Other)', 'Outdoor grill (charcoal)',
        'Outdoor grill (gas or propane)', 'None of the above',
        # Ownership, Kitchen Appliances (Small)
        'Blender / Juicer', 'Bread Maker', 'Coffee maker (drip)', 'Coffee pod machine', 'Deep fryer', 'Electric grill',
        'Food processor', 'Homebrewing system', 'Mixer (handheld)', 'Mixer (stand)', 'Pressure cooker', 'Rice cooker',
        'Slow cooker', 'Soda machine', 'Toaster / Toaster oven', 'Waffle iron', 'None of the above',
        # Housing Structure
        'Single-family home', '2 - 4 unit complex', '5+ unit complex', 'Mobile home', 'Dorm / shared living', 'Other',
        # Own or Rent
        'Own', 'Rent', 'Other',
        # Length of Residence
        'Less than 12 months', '12-24 months', '2 to 4 years', '5 to 9 years',
        '10 to 19 years', '20 to 29 years', '30+ years',
        # Transportation Modes
        'Auto', 'Motorcycle / Scooter', 'Taxi / Ride share', 'Bus / Streetcar',
        'Train / Subway', 'Walking or Biking', 'Other',
        # No. of Vehicles
        'Zero', '1', '2', '3', '4 or more',
        # Vehicle Fuel Types
        'Gasoline', 'Diesel', 'Hybrid', 'Electric', 'None of the above']
    # Shopping Headers & Tables
    SHOP_HEAD = ['ONLINE ORDER FREQUENCY', 'DEVICES USED TO SHOP ONLINE', 'HOLIDAY SHOPPING (PAST YEAR)',
                 'PRIVATE LABEL VALUE PERCEPTION', 'PRIVATE LABEL QUALITY PERCEPTION',
                 'PRIVATE LABEL GENERAL PERCEPTIONS', 'SHOPPING ROLE', 'SHOPPING ATTITUDES', 'SHOPPING BEHAVIOR',
                 'ONLINE SHOPPING IS…', 'ONLINE RESEARCH FREQUENCY', 'ONLINE SHOPPING ATTITUDES']
    SHOP_TABLE = [
        # Online Order Frequency
        'Weekly', 'Several times a month', 'Once a month', 'Several times a year',
        'Once a year', 'Less often than once a year', 'Never',
        # Devices Used to Shop Online
        'Smartphone', 'Tablet', 'In-Store Kiosks', 'Computer / Other',
        # Holiday Shopping (Past Year)
        'Super Bowl', 'Valentines Day', "St. Patrick's Day", 'Passover', 'Easter', 'Cinco de Mayo',
        "Mother's Day", 'Memorial Day', "Father's Day", 'Fourth of July', 'Back to School', 'Labor Day',
        'Halloween', 'Thanksgiving', 'Hanukkah', 'Christmas', "New Year's Eve", 'None of the above',
        # Private Label Value Perception
        'Excellent', 'Above average', 'Average', 'Below average', 'Very Poor',
        # Private Label Quality Perception
        'Excellent', 'Very good', 'Average', 'Below average', 'Very poor',
        # Private Label General Perceptions
        'PL quality has improved', 'I rarely consider PL', 'I purchase PL to save money',
        'I prefer popular brand names', 'I am savvy when I buy PL', 'Brand name indicates quality',
        "I'll switch to PL if on sale", 'Private label is just as good', 'Price trumps brand names',
        # Shopping Role
        'Primary shopper', 'Secondary shopper', 'Non-shopper',
        # Shopping Attitudes
        'Grocery shopping is a chore', 'Budget-driven', 'Price-driven', 'Quick in-and-out',
        'Status-driven', 'Quality-driven', 'Values-driven', 'None of the above',
        # Shopping Behavior
        'List maker', 'Creature of habit', 'Ad checker', 'Display browser', 'Deal-focused, brand switcher',
        'Coupon clipper', 'Impulse buyer', 'Tries new things', 'Deal-focused, brand loyalist', 'None of the above',
        # Online Shopping Is...
        'Very enjoyable', 'Enjoyable', 'Somewhat enjoyable', 'Not enjoyable', 'Not at all enjoyable',
        # Online Research Frequency
        'Regularly', 'Often', 'Occasionally', 'Rarely', 'Never',
        # Online Shopping Attitudes
        'Saves me time', 'Saves me money', 'Dislikes sharing credit card', 'Prefers physical stores',
        'Distrusts fresh foods online', 'Buys in bulk online', 'Buys hard to find items online',
        'Online deals are sub-par', 'Deliveries are convenient', 'Does not shop online']
    # Sports Fandom Tables & Headers
    SPORTS_HEAD = ['SPORTS WATCHED, LAST 12 MONTHS', 'SPORTS ATTENDED, LAST 12 MONTHS', 'SPORTS FANDOM']
    SPORTS_TABLE = [
        # Sports Watched
        'NFL', 'NBA', 'MLB', 'NHL', 'MLS', "Int'l Soccer", 'Golf', 'Auto Racing',
        'College Basketball', 'College Football', 'Combat Sports', 'None of the above',
        # Sports Attended
        'NFL', 'NBA', 'MLB', 'NHL', 'MLS', "Int'l Soccer", 'Golf', 'Auto Racing',
        'College Basketball', 'College Football', 'Combat Sports', 'None of the above',
        # Sports Fandom
        'Avid Fan', 'Committed', 'Average', 'Casual', 'Non-fan']
