from constants.prompt_selections import BS


class BS(object):
    # Prompt Selection
    PROD = BS.PROD.value
    PROD_U = PROD.upper()
    CG_PROD = BS.CG_PROD.value
    PROD_LEV = BS.PROD_LEV.value
    CG_PROD_LEV = BS.CG_PROD_LEV.value
    CAT = BS.CAT.value
    CG_CAT = BS.CG_CAT.value
    # Summary Tab Card Titles
    CARD_TITLES = ['Repeat Rate, ' + PROD + ' vs Avg. ' + CAT, PROD + ' Top Switching Competition',
                   '% of Trips, ' + PROD + ' (Repeat)', '% of Trips, ' + PROD,
                   '% of Spend, ' + PROD, '% of Units, ' + PROD]
    # Summary Tab Card Titles [CG]
    CARD_TITLES_CG = ['Repeat Rate, ' + CG_PROD + ' vs Avg. ' + CG_CAT, CG_PROD + ' Top Switching Competition',
                      '% of Trips, ' + CG_PROD + ' (Repeat)', '% of Trips, ' + CG_PROD,
                      '% of Spend, ' + CG_PROD, '% of Units, ' + CG_PROD]
    # Switching Tab Product Dropdown
    PROD_DROP = ['All Pairs', 'Competitive', 'Product', 'Private Label']
    # Swtiching Tab Metric Dropdown
    MET_DROP = ['% of Trips', '% of Units', '% of Spend', 'Projected Trips', 'Projected Units', 'Projected Spend']
    # Switching Tab Legends
    SWITCH_LEG = [['{}, Gained by ' + PROD, '{}, Lost from ' + PROD],
                  ['{}, Gain by ' + PROD, '{}, Lost from ' + PROD]]
    # Switching Tab Legends [CG]
    SWITCH_LEG_CG = [['{}, Gained by ' + CG_PROD, '{}, Lost from ' + CG_PROD],
                     ['{}, Gain by ' + CG_PROD, '{}, Lost from ' + CG_PROD]]
    # Switching Tab Header
    SWITCH_HEAD = [PROD_LEV.upper(), '{}, GAINED BY ' + PROD.upper(), '{}, LOST FROM ' + PROD.upper(),
                   '{}, NET POINT DIFFERENCE',
                   'INDEX, {} GAINED BY ' + PROD.upper() + ' VS {} LOST FROM ' + PROD.upper(),
                   'INTERACTING BUYER COUNT']
    SWITCH_HEAD_ETC = [[PROD_LEV.upper(), '{}, GAIN BY ' + PROD.upper(), '{}, LOST FROM ' + PROD.upper(),
                        'NET TRIPS GAINED OR LOST FOR ' + PROD.upper(),
                        'INDEX, % OF TRIPS GAINED BY ' + PROD.upper()
                        + ' VS % OF TRIPS LOST FROM ' + PROD.upper(),
                        'INTERACTING BUYER COUNT'],
                       [PROD_LEV.upper(), '{}, GAINED BY ' + PROD.upper(), '{}, LOST FROM ' + PROD.upper(),
                        'NET UNITS GAINED OR LOST FOR ' + PROD.upper(),
                        'INDEX, % OF UNITS GAINED BY ' + PROD.upper()
                        + ' VS % OF UNITS LOST FROM ' + PROD.upper(),
                        'INTERACTING BUYER COUNT'],
                       [PROD_LEV.upper(), '{}, GAINED BY ' + PROD.upper(), '{}, LOST FROM ' + PROD.upper(),
                        'NET SPEND GAINED OR LOST FOR ' + PROD.upper(),
                        'INDEX, % OF SPEND GAINED BY ' + PROD.upper()
                        + ' VS % OF SPEND LOST FROM ' + PROD.upper(),
                        'INTERACTING BUYER COUNT']]
    # Switching Tab Header [CG]
    SWITCH_HEAD_CG = [CG_PROD_LEV.upper(), '{}, GAINED BY ' + CG_PROD.upper(), '{}, LOST FROM ' + CG_PROD.upper(),
                      '{}, NET POINT DIFFERENCE',
                      'INDEX, {} GAINED BY ' + CG_PROD.upper() + ' VS {} LOST FROM ' + CG_PROD.upper(),
                      'INTERACTING BUYER COUNT']
    SWITCH_HEAD_ETC_CG = [[CG_PROD_LEV.upper(), '{}, GAIN BY ' + CG_PROD.upper(), '{}, LOST FROM ' + CG_PROD.upper(),
                           'NET TRIPS GAINED OR LOST FOR ' + CG_PROD.upper(),
                           'INDEX, % OF TRIPS GAINED BY ' + CG_PROD.upper()
                           + ' VS % OF TRIPS LOST FROM ' + CG_PROD.upper(),
                           'INTERACTING BUYER COUNT'],
                          [CG_PROD_LEV.upper(), '{}, GAINED BY ' + CG_PROD.upper(), '{}, LOST FROM ' + CG_PROD.upper(),
                           'NET UNITS GAINED OR LOST FOR ' + CG_PROD.upper(),
                           'INDEX, % OF UNITS GAINED BY ' + CG_PROD.upper()
                           + ' VS % OF UNITS LOST FROM ' + CG_PROD.upper(),
                           'INTERACTING BUYER COUNT'],
                          [CG_PROD_LEV.upper(), '{}, GAINED BY ' + CG_PROD.upper(), '{}, LOST FROM ' + CG_PROD.upper(),
                           'NET SPEND GAINED OR LOST FOR ' + CG_PROD.upper(),
                           'INDEX, % OF SPEND GAINED BY ' + CG_PROD.upper()
                           + ' VS % OF SPEND LOST FROM ' + CG_PROD.upper(),
                           'INTERACTING BUYER COUNT']]
    # Switching Tab Header Format
    SWITCH_FORM = ['TRIPS', 'UNITS', 'SPEND']
    # Gains & Losses Grid Tab Legend
    GRID_LEG = ['Low Interaction', 'Back and Forth', 'Losing', 'Gaining']
    # Gains & Losses Grid Tab Header
    GRID_HEAD = [PROD_LEV.upper(), 'EVALUATION',
                 'INDEX, % OF SPEND GAINED BY ' + PROD.upper() + ' VS % OF SPEND GAINED BY OTHERS',
                 'INDEX, % OF SPEND LOST FROM ' + PROD.upper() + ' VS % OF SPEND LOST FROM OTHERS',
                 '% OF SPEND, NET POINT DIFFERENCE', 'INTERACTING BUYER COUNT, ' + PROD.upper() + ' BUYERS']
    # Gains & Losses Grid Tab Header [CG]
    GRID_HEAD_CG = [CG_PROD_LEV.upper(), 'EVALUATION',
                    'INDEX, % OF SPEND GAINED BY ' + CG_PROD.upper() + ' VS % OF SPEND GAINED BY OTHERS',
                    'INDEX, % OF SPEND LOST FROM ' + CG_PROD.upper() + ' VS % OF SPEND LOST FROM OTHERS',
                    '% OF SPEND, NET POINT DIFFERENCE', 'INTERACTING BUYER COUNT, ' + CG_PROD.upper() + ' BUYERS']
    # Share of Spend Tab Dropdown
    SHARE_DROP = ['% of Spend, Among ' + PROD + ' Buyers', '% of Spend, Among All Buyers',
                  'Index, % of Spend, Fair Share',
                  'Index, % of Spend Gained by ' + PROD + ' vs % of Spend Gained by Others',
                  'Index, % of Spend Lost from ' + PROD + ' vs % of Spend Lost from Others']
    # Share of Spend Tab Dropdown [CG]
    SHARE_DROP_CG = ['% of Spend, Among ' + CG_PROD + ' Buyers', '% of Spend, Among All Buyers',
                     'Index, % of Spend, Fair Share',
                     'Index, % of Spend Gained by ' + CG_PROD + ' vs % of Spend Gained by Others',
                     'Index, % of Spend Lost from ' + CG_PROD + ' vs % of Spend Lost from Others']
    # Share of Spend Tab Header
    SHARE_HEAD = [PROD_LEV.upper(), '% OF SPEND, AMONG ' + PROD.upper() + ' BUYERS',
                  '% OF SPEND, AMONG ALL BUYERS', 'INDEX, % OF SPEND, FAIR SHARE',
                  'INDEX, % OF SPEND GAINED BY ' + PROD.upper() + ' VS % OF SPEND GAINED BY OTHERS',
                  'INDEX, % OF SPEND LOST FROM ' + PROD.upper() + ' VS % OF SPEND LOST FROM OTHERS',
                  'BUYER COUNT, ' + PROD.upper() + ' BUYERS']
    # Share of Spend Tab Header [CG]
    SHARE_HEAD_CG = [CG_PROD_LEV.upper(), '% OF SPEND, AMONG ' + CG_PROD.upper() + ' BUYERS',
                     '% OF SPEND, AMONG ALL BUYERS', 'INDEX, % OF SPEND, FAIR SHARE',
                     'INDEX, % OF SPEND GAINED BY ' + CG_PROD.upper() + ' VS % OF SPEND GAINED BY OTHERS',
                     'INDEX, % OF SPEND LOST FROM ' + CG_PROD.upper() + ' VS % OF SPEND LOST FROM OTHERS',
                     'BUYER COUNT, ' + CG_PROD.upper() + ' BUYERS']
