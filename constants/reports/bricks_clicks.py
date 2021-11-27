from constants.prompt_selections import BC


class BC(object):
    # Prompt Selection
    CAT = BC.CAT.value
    CG_CAT = BC.CG_CAT.value
    PROD = BC.PROD.value
    CG_PROD = BC.CG_PROD.value
    PROD_LEV = BC.PROD_LEV.value
    CG_PROD_LEV = BC.CG_PROD_LEV.value
    # Summary Tab Tree Titles
    TREE_TITLES = [CAT + ' Buyers', 'Have Not Bought ' + CAT + ' Online', 'Have Bought ' + CAT + ' Online',
                   'Have Not Bought Anything Else Online', 'Have Bought ' + CAT + ' Online Only 1 Time',
                   'Have Bought Something Else Online', 'Have Bought ' + CAT + ' Online 2 or More Times']
    # Summary Tab Tree Titles [CG]
    TREE_TITLES_CG = [CG_CAT + ' Buyers', 'Have Not Bought ' + CG_CAT + ' Online', 'Have Bought ' + CG_CAT + ' Online',
                      'Have Not Bought Anything Else Online', 'Have Bought ' + CG_CAT + ' Online Only 1 Time',
                      'Have Bought Something Else Online', 'Have Bought ' + CG_CAT + ' Online 2 or More Times']
    # Channel/Brand Shift Tab Dropdown
    BUYER_DROP = [CAT + ' Buyers, when buying Category', PROD + ' Buyers, when buying Category']
    # Channel/Brand Shift Tab Dropdown [CG]
    BUYER_DROP_CG = [CG_CAT + ' Buyers, when buying Category', CG_PROD + ' Buyers, when buying Category']
    # Channel/Brand Shift Tab Metric Toggle
    MET_TOG = ['% of Spend', '% of Units', '% of Trips']
    # Channel Shift Tab Legend
    CHAN_LEG = ['{}, Pre-Period', '{}, Post-Period']
    # Channel Shift Tab Header
    CHAN_HEAD = ['CHANNEL', '{}, PRE-PERIOD', '{}, POST-PERIOD', 'INDEX, {}',
                 'BUYER COUNT, PRE-PERIOD', 'BUYER COUNT, POST-PERIOD']
    # Brand Shift Tab Legend
    BRAND_LEG = ['{}, Offline', '{}, Online']
    # Brand Shift Tab Header
    BRAND_HEAD = [PROD_LEV.upper(), '{}, OFFLINE', '{}, OFFLINE, PRE-PERIOD', '{}, ONLINE',
                  '{}, ONLINE, PRE-PERIOD', 'BUYER COUNT, OFFLINE', 'BUYER COUNT, ONLINE']
    # Brand Shift Tab Header [CG]
    BRAND_HEAD_CG = [CG_PROD_LEV.upper(), '{}, OFFLINE', '{}, OFFLINE, PRE-PERIOD', '{}, ONLINE',
                     '{}, ONLINE, PRE-PERIOD', 'BUYER COUNT, OFFLINE', 'BUYER COUNT, ONLINE']
