
class BD(object):
    # Key Penetration Indicators Tab Dropdown
    KPI_DROP = ['Household Penetration (%)', 'Purchase Frequency', 'Spend per Trip', 'Share of Category Requirements',
                '% of Loyal HHs', 'Category Segmentation', 'Purchase Cycle', 'Buying Rate', 'Repeat Buyers (%)']
    # Key Penetration Indicators Tab Alternate Legend
    KPI_LEG = [None, None, None, 'Share of Category Requirements',
               'Exclusive + Loyal HHs', 'Category Segmentation']
    # Key Penetration Indicators Tab Static Header
    KPI_STATIC_HEAD = ['CATEGORY', None, 'INDEX VS. PRODUCT AVG', 'BUYER COUNT']
    # Key Penetration Indicators Tab Alternate Headers
    KPI_ALT_HEAD = [
        None, None, None,
        # Share of Category Requirements Header
        ['CATEGORY', 'SHARE OF CATEGORY REQ. (SPEND)', 'BUYER COUNT'],
        # % of Loyal HHs Header
        ['CATEGORY', 'EXCLUSIVE + LOYAL HHS', 'EXCLUSIVE HHS (100% OF CAT. SPEND)',
         'LOYAL HHS (70% - 99% OF CAT. SPEND)', 'OCCASIONAL HHS (30% - 69% OF CAT. SPEND)',
         'LIGHT HHS (< 30% OF CAT. SPEND)', 'BUYER COUNT'],
        # Category Segmentation
        ['CATEGORY', 'HIGH CATEGORY BUYERS', 'MEDIUM CATEGORY BUYERS', 'LOW CATEGORY BUYERS', 'BUYER COUNT']]
    # Brand Tree Titles
    TREE_TITLES = ['Projected Sales', 'Household Penetration', 'Buying Rate', 'Purchase Frequency',
                   'Spend per Trip', 'Units per Trip', 'Spend per Unit']
    # Penetration Grid Tab Card Titles
    CARD_TITLES = ['High Cat., Non Brand Purchaser', 'Med. Cat., Non Brand Purchaser', 'Low Cat., Non Brand Purchaser',
                   'High Cat., Low Brand', 'Med Cat., Low Brand', 'Low Cat., Low Brand',
                   'High Cat., Med. Brand', 'Med. Cat., Med. Brand', 'Low Cat., Med. Brand',
                   'High Cat., High Brand', 'Med. Cat., High Brand', 'Low Cat., High Brand']
