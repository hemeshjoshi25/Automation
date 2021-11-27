
class RSOW(object):
    # Metrics Dropdown
    RSOW_DROP = ['Share of Wallet', 'Purchase Frequency', 'Spend per Trip', 'Units per Trip', 'Buying Rate']
    # Category Summary Tab Headers
    CAT_HEAD = [
        # Share of Wallet Header
        ['CATEGORY', 'BRAND', 'SHARE OF WALLET (%)(PREV)', 'SHARE OF WALLET (%)',
         'SHARE OF WALLET POINT CHANGE', 'BUYER COUNT'],
        # Purchase Frequency Header
        ['CATEGORY', 'BRAND', 'PURCHASE FREQUENCY (PREV)', 'PURCHASE FREQUENCY',
         'PURCHASE FREQUENCY CHANGE', 'BUYER COUNT'],
        # Spend per Trip Header
        ['CATEGORY', 'BRAND', 'SPEND PER TRIP (PREV)', 'SPEND PER TRIP',
         'SPEND PER TRIP CHANGE', 'BUYER COUNT'],
        # Units per Trip Header
        ['CATEGORY', 'BRAND', 'UNITS PER TRIP (PREV)', 'UNITS PER TRIP',
         'UNITS PER TRIP CHANGE', 'BUYER COUNT'],
        # Buying Rate Header
        ['CATEGORY', 'BRAND', 'BUY RATE (PREV)', 'BUY RATE',
         'BUY RATE CHANGE', 'BUYER COUNT']]
    # Competitive Tab Headers
    COMP_HEAD = [
        # Share of Wallet Header
        ['RETAILER', 'SHARE OF WALLET (%)(PREV)', 'SHARE OF WALLET (%)',
         'SHARE OF WALLET POINT CHANGE', 'BUYER COUNT'],
        # Purchase Frequency Header
        ['RETAILER', 'PURCHASE FREQUENCY (PREV)', 'PURCHASE FREQUENCY',
         'PURCHASE FREQUENCY CHANGE', 'BUYER COUNT'],
        # Spend per Trip Header
        ['RETAILER', 'SPEND PER TRIP (PREV)', 'SPEND PER TRIP',
         'SPEND PER TRIP CHANGE', 'BUYER COUNT'],
        # Units per Trip Header
        ['RETAILER', 'UNITS PER TRIP (PREV)', 'UNITS PER TRIP',
         'UNITS PER TRIP CHANGE', 'BUYER COUNT'],
        # Buying Rate Header
        ['RETAILER', 'BUY RATE (PREV)', 'BUY RATE',
         'BUY RATE CHANGE', 'BUYER COUNT']]
