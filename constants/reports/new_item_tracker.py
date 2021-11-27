from constants.prompt_selections import NIT


class NIT(object):
    # Prompt Selections
    NI_1 = NIT.NI_1.value
    # Summary Tab Tree Titles
    TREE_TITLES = ['Triers', 'Repeaters', 'One-Time Triers', 'Multi-Time Repeaters']
    # Trial & Repeat Tab Dropdowns
    TIME_DROP = ['Weekly', 'Monthly']
    MET_DROP = ['% Trial', '% Repeat', 'Spend/Trip', 'Spend/Trip on Trial Purchase', 'Spend/Trip on Repeat Purchases',
                '# of Repeats made by Repeat Buyers', 'Household Count']
    # Trial & Repeat Legend
    TRIAL_LEG = NI_1 + ' - {}'
    # Trial & Repeat Tab Header
    TRIAL_HEAD = ['TIME PERIOD', NI_1.upper() + ' - {}']
    # Repeat Drivers Tab Dropdown
    REPEAT_DROP = [NI_1 + ' - Weekly', NI_1 + ' - Monthly']
    # Repeat Drivers Tab Legend
    REPEAT_LEG = ['% Driven by Trial', '% Driven by 1st Repeat', '% Driven by 2nd Repeat',
                  '% Driven by 3rd Repeat', '% Driven by Additional Repeat']
    # Repeat Drivers Tab Header
    REPEAT_HEAD = ['TIME PERIOD', '% OF SPEND DRIVEN BY TRIAL', '% OF SPEND DRIVEN BY 1ST REPEAT',
                   '% OF SPEND DRIVEN BY 2ND REPEAT', '% OF SPEND DRIVEN BY 3RD REPEAT',
                   '% OF SPEND DRIVEN BY ADDITIONAL REPEATS']
    # Retailer Drivers Tab Header
    RETAIL_HEAD = ['RETAILER', '% OF SPEND', '% OF UNITS', '% OF TRIPS']
    # Top Items Tab Dropdown
    TOP_DROP = ['Repeat', 'Trial']
    # Top Items Tab Header
    TOP_HEAD = ['ITEM', '% SPEND', '% UNITS', '% TRIPS']
