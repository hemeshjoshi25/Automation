from constants.prompt_selections import PSC


class PSC(object):
    # Prompt Selection
    PG = PSC.PG.value
    # Retailer/Channel Circuits/Substitutable Trips Tab Dropdown
    CIRCUITS_DROP = [PG, 'All Shoppers']
    # Retailer Circuits Tab Header
    RET_HEAD = ['RETAILER', 'PROJECTED TRIPS', 'PROJECTED SALES', 'BUYER COUNT', '% OF TRIPS', '% OF SPEND',
                '% OF HOUSEHOLDS', 'INDEX, PROJECTED TRIPS', 'INDEX, PROJECTED SALES', 'INDEX, BUYER COUNT']
    # Channel Circuits Tab Header
    CHAN_HEAD = ['(PEPSI) CHANNEL GROUPS WO TOTAL', 'PROJECTED TRIPS', 'PROJECTED SALES', 'BUYER COUNT',
                 '% OF TRIPS', '% OF SPEND', '% OF HOUSEHOLDS', 'INDEX, PROJECTED TRIPS',
                 'INDEX, PROJECTED SALES', 'INDEX, BUYER COUNT']
    # Pepsi/Total Edibles/Demographics Tab Dropdown
    MET_DROP = ['Trips', 'Spend', 'Households']
    # Pepsi/Total Edibles Tab Header
    PEP_HEAD = '(PEPSI) TOTAL EDIBLE CATEGORIES'
    # Demographics Tab Header
    DEMO_HEAD = 'DEMOGRAPHICS'
    # Substitutable Trips Tab Header
    SUB_HEAD = ['PEPSI COMPETITIVE RETAILER', 'PROJECTED TRIPS, COMPETITIVE', 'PROJECTED TRIPS, TOTAL',
                'BUYER COUNT, COMPETITIVE', 'BUYER COUNT, TOTAL', '% OF TRIPS, COMPETITIVE',
                'INDEX, PROJECTED TRIPS, COMPETITIVE']
