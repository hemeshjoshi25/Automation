from constants.prompt_selections import SD


class SD(object):
    # Prompt Selections
    PERIOD = SD.PERIOD.value.upper()
    PROD = SD.PROD.value
    CG_PROD = SD.CG_PROD.value
    STORE = SD.STORE.value
    # Key Performance Indicators Tab Dropdown
    KPI_DROP = ['Traffic', 'Projected Households', 'Trips per Households', '% of Loyal HHs', 'Purchase Cycle',
                'Buying Rate', 'Repeat Buyers (%)', 'Basket Size', 'Share of Trips', 'Share of Units',
                'Store Share of Product Requirement', 'Store Share of Wallet', 'Store Market Share', 'Store Conversion',
                'Product Conversion', 'Spend per Trip', 'Spend per Unit', 'Units per Trip']
    # Key Performance Indicators Legends
    KPI_LEG = ['Exclusive + Loyal HHs']
    # Key Performance Indicators Header
    KPI_STATIC_HEAD = [['BANNER', None, '% CHANGE VS. ' + PERIOD, 'INDEX VS. STORE AVG.',
                        'RANK ACROSS COMPETITIVE CHANNEL', 'BUYER COUNT'],
                       ['BANNER', None, 'POINT CHANGE VS. ' + PERIOD, 'INDEX VS. STORE AVG.',
                        'RANK ACROSS COMPETITIVE CHANNEL', 'BUYER COUNT']]
    KPI_HH_HEAD = ['BANNER', 'EXCLUSIVE + LOYAL HHS', 'EXCLUSIVE HHS (100% OF CAT. SPEND)',
                   'LOYAL HHS (70% - 99% OF CAT. SPEND)', 'OCCASIONAL HHS (30% - 69% OF CAT. SPEND)',
                   'LIGHT HHS (< 30% OF CAT. SPEND)', 'BUYER COUNT']
    # Penetration Grid Tab Card Titles
    CARDS = ['Low ' + PROD + ', High ' + STORE, 'Med ' + PROD + ', High ' + STORE, 'High ' + PROD + ', High ' + STORE,
             'Low ' + PROD + ', Med ' + STORE, 'Med ' + PROD + ', Med ' + STORE, 'High ' + PROD + ', Med ' + STORE,
             'Low ' + PROD + ', Low ' + STORE, 'Med ' + PROD + ', Low ' + STORE, 'High ' + PROD + ', Low ' + STORE,
             'Low ' + PROD + ', Non ' + STORE, 'Med ' + PROD + ', Non ' + STORE, 'High ' + PROD + ', Non ' + STORE]
    # Penetration Grid Tab Card Titles [CG]
    CARDS_CG = ['Low ' + CG_PROD + ', High ' + STORE, 'Med '
                + CG_PROD + ', High ' + STORE, 'High ' + CG_PROD + ', High ' + STORE,
                'Low ' + CG_PROD + ', Med ' + STORE, 'Med '
                + CG_PROD + ', Med ' + STORE, 'High ' + CG_PROD + ', Med ' + STORE,
                'Low ' + CG_PROD + ', Low ' + STORE, 'Med '
                + CG_PROD + ', Low ' + STORE, 'High ' + CG_PROD + ', Low ' + STORE,
                'Low ' + CG_PROD + ', Non ' + STORE, 'Med '
                + CG_PROD + ', Non ' + STORE, 'High ' + CG_PROD + ', Non ' + STORE]
