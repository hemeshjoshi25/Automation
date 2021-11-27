
class MOT(object):
    # Summary Tab Card Titles
    CARD_TITLES = ['Zero Moment of Truth', None, None, 'First Moment of Truth', None, None,
                   'Second Moment of Truth', None, None, 'Third Moment of Truth', None, None]
    # Compare Moments of Truth Tab Dropdown
    MOT_DROP = ['0th - Zero Moment of Truth', '1st - First Moment of Truth',
                '2nd - Second Moment of Truth', '3rd - Third Moment of Truth']
    # Compare Moments of Truth Tab Legend
    MOT_LEG = ['Moment of Truth Metric (0-100)']
    # Compare Moments of Truth Tab Header
    MOT_HEAD = ['PRODUCT', 'MOT METRIC', '# OF RESPONSES']
    # Explore/Compare Survey Tab Dropdown
    SURVEY_DROP = ['0MOT: Planned or Impulse Purchase', '0MOT: Product Meeting the Need',
                   '1MOT: Consider Other Brands', '1MOT: Purchased On Deal',
                   '1MOT: Rating for Packaging', '1MOT: Rating for Value',
                   '2MOT: Meeting Need Rating', '2MOT: Overall Product Rating',
                   '2MOT: Product Importance to Category', '2MOT: Quality Rating',
                   '2MOT: Satisfaction if Only Product Available',
                   '3MOT: If Out Of Stock', '3MOT: Is Product Preferred',
                   '3MOT: Speed to Replenish', '3MOT: Uniqueness Rating',
                   'Misc: Willingness to purchase Online']
    # Explore/Compare Survey Tab Legend
    SURVEY_LEG = ['% of Responses']
    # Explore Survey Tab Header
    EX_HEAD = ['OPTION', '% OF RESPONSES', '# RESPONSES']
    # Compare Survey Tab Header
    COMP_HEAD = ['PRODUCT', '% OF RESPONSES', '# RESPONSES']
