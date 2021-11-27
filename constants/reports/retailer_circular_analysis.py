from constants.prompt_selections import RCA


class RCA(object):
    # Prompt Selections
    BANNER = RCA.BANNER.value.upper()
    COMP_BANNER = RCA.COMP_BANNER.value.upper()
    # Main Tab Dropdown
    MET_DROP = ['Penetration (% of Country Households)', 'Reach (% of Shoppers during Week)', 'Market Share (Spend)',
                'Market Share (Units)', 'Market Share (Trips)', 'Share of Wallet amongst Retailer Shoppers (Spend)',
                'Share of Wallet amongst Retailer Shoppers (Units)',
                'Share of Wallet amongst Retailer Shoppers (Trips)', 'Purchase Frequency', 'Spend per Trip',
                'Unit Price Point', 'Penetration - Index', 'Reach - Index', 'Market Share (Spend) - Index',
                'Market Share (Units) - Index', 'Market Share (Trips) - Index', 'Share of Wallet (Spend) - Index',
                'Share of Wallet (Units) - Index', 'Share of Wallet (Trips) - Index', 'Purchase Frequency - Index',
                'Spend per Trip - Index', 'Unit Price Point - Index']
    RCA_HEAD = ['YEAR WEEK', BANNER + ' CIRCULAR WEEK', BANNER + ' NON-CIRCULAR WEEK',
                COMP_BANNER + ' CIRCULAR WEEK', COMP_BANNER + ' NON-CIRCULAR WEEK',
                'REST OF MARKET', BANNER + ' BUYER COUNT', COMP_BANNER + ' BUYER COUNT']
