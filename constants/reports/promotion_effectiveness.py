
class PE(object):
    # Promotion Summary Tab Dropdown
    PROMO_DROP = ['Manufacturer', 'Retailer']
    # Promotion Summary Legends
    PROMO_LEG = [
        # Manufacturer Legend
        ['Repeat Buyer', 'Intra-Manufacturer Brand Switcher', 'Incremental Switchers', 'New Category Buyer'],
        # Retailer Legend
        ['Repeat Shopper', 'Category Brand Switcher', 'Category Converts', 'New Retailer Shopper']]
    # Promotion Summary Tab Toggle
    PROMO_TOG = ['Households (%)', 'Spend (%)', 'Trips (%)', 'Units (%)']
    # Promotion Summary Tab Headers
    PROMO_STATIC_HEAD = ['TIME PERIOD', 'BUYER TYPE', None, 'BUYER COUNT']
    PROMO_HEAD = ['% OF HOUSEHOLDS', '% OF SPEND', '% OF TRIPS', '% OF UNITS']
    # Conversion Tab Tree Titles
    CONV_TREE = ['All Promotion Buyers', 'New Buyers', 'Existing Buyers', 'Converted', 'Incremental',
                 'Not Converted', 'Subsidized', 'Existing and Not Returned Buyers']
