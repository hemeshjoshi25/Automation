from constants.prompt_selections import PROS


class PROS(object):
    # Prompt Selections
    PROD = PROS.PROD.value
    # Promotion Details Tab Header
    PROMO_HEAD = ['PROMOTED BRAND', 'PROMOTED CATEGORY', 'PROMOTED STORE', 'CIRCULATION WEEK',
                  'PROMOTED SIZES', 'BUYER COUNT', 'LINK TO IMAGE']
    # Incrementality Tab Dropdown
    INCREMENT_DROP = ['Incrementality', 'Offer Types', 'Top Brands', 'Scale Events',
                      'Location in Circular', 'Size Dimension Name']
    MET_DROP = ['Percent', 'Projected']
    MET_FORMAT = ['% SPEND', 'PROJECTED SPEND']
    # Incrementality Tab Legends
    INCREMENT_LEG = [
        # Incrementality Dropdown
        ['Re-evaluate', 'Win-Win', 'Better for Manufacturer', 'Better for Retailer'],
        # Offer Types Dropdown
        ['NOT Additional Savings', 'Additional Savings'],
        # Top Brands Dropdown
        [PROD],
        # Scale Events Dropdown
        ['Single Brand Event', 'Manufacturer Scale Event', 'Category Scale Event'],
        # Location in Circular Dropdown
        ['Middle page', 'Front page', 'Outer Wrap', 'Back page'],
        # Size Dimension Name
        ['Pack size and Unit Size', 'Single unit size or All products']]
    # Incrementality Tab Header
    INCREMENT_HEAD = ['PROMOTED BRAND', 'PROMOTED CATEGORY', 'PROMOTED STORE', 'CIRCULATION WEEK',
                      'PROMOTED SIZES', '{} INCREMENTAL TO MANUFACTURER', '{} INCREMENTAL TO RETAILER',
                      'CLASSIFICATION', 'BUYER COUNT', 'LINK TO IMAGE']
    # Incrementality Details Tab Headers
    DETAIL_HEAD = [
        # Retailer Toggle
        ['PROMOTED BRAND', 'PROMOTED CATEGORY', 'PROMOTED STORE', 'CIRCULATION WEEK',
         'PROMOTED SIZES', '% SPEND NEW RETAILER SHOPPER', '% SPEND CATEGORY CONVERTERS',
         '% SPEND CATEGORY BRAND SWITCHER', '% SPEND REPEAT SHOPPER', 'BUYER COUNT', 'LINK TO IMAGE'],
        # Manufacturer Toggle
        ['PROMOTED BRAND', 'PROMOTED CATEGORY', 'PROMOTED STORE', 'CIRCULATION WEEK',
         'PROMOTED SIZES', '% SPEND NEW CATEGORY BUYER', '% SPEND COMPETITIVE SWITCHER',
         '% SPEND INTRA-MANUFACTURER BRAND SWITCHER', '% SPEND REPEAT BUYER', 'BUYER COUNT', 'LINK TO IMAGE']]
    # Brand Switching Summary Tab Header
    SWITCH_HEAD = ['COMPETITIVE PRODUCT SOURCED FROM', '% OF PROMOTION SPEND',
                   '% OF PROMOTION UNITS', '% OF PROMOTION TRIPS']
    # Brand Switching Detail Tab Dropdown
    SWITCH_DETAIL_DROP = ['Spend', 'Units', 'Trips']
    # Brand Switching Detail Tab Header
    SWITCH_DETAIL_HEAD = ['IMPACTED BY PROMOTION FOR', 'PROMOTED CATEGORY', 'PROMOTED STORE', 'CIRCULATION WEEK',
                          'PROMOTED SIZES', '% OF PROMOTION {}', 'BUYER COUNT']
    # Store Switching Tab Header
    STORE_HEAD = ['IMPACTED BY PROMOTION AT', 'PROMOTED BRAND', 'PROMOTED CATEGORY', 'PROMOTION WEEK',
                  'PROMOTED SIZES', '% OF PROMOTION {}', 'BUYER COUNT']
