from constants.prompt_selections import EBSOVA


class EBSOVA(object):
    PROD = EBSOVA.PROD.value
    CG_PROD = EBSOVA.CG_PROD.value
    # Summary Tab Dropdown
    SUMMARY_DROP = ['Spend', 'Units']
    # Summary Tab Tree Titles
    TREE_TITLES = ['Total Change in {}', 'Due to Category Churn',
                   'Due to Category Expansion/Contraction', 'Due to Brand Shifting']
    # Source of Volume Tab Legend
    SOV_LEG = ['Impact to {}, Pre Period', 'Gains', 'Losses', 'Post Period']
    # Source of Volume Header
    SOV_HEAD = ['SOURCE OF VOLUME', 'IMPACT ON {}']
    # Category Churn Dropdown
    CAT_DROP = ['Channel', 'Retailer', 'Banner']
    # Category Churn Legend
    CAT_LEG = ['Gains to ' + PROD, 'Losses, due to Category Churn', 'Net Change']
    # Category Churn Legend [CG]
    CAT_LEG_CG = ['Gains to ' + CG_PROD, 'Losses, due to Category Churn', 'Net Change']
    # Category Churn Header
    CAT_HEAD = [None, 'GAINS TO ' + PROD.upper(), 'LOSSES FROM ' + PROD.upper(), 'NET CHANGE',
                'TOTAL SHIFTING {}', 'SHARE OF SHIFTING {} (%)', 'FAIR SHARE (%)', 'INTERACTION INDEX']
    # Category Churn Header [CG]
    CAT_HEAD_CG = [None, 'GAINS TO ' + CG_PROD.upper(), 'LOSSES FROM ' + CG_PROD.upper(), 'NET CHANGE',
                   'TOTAL SHIFTING {}', 'SHARE OF SHIFTING {} (%)', 'FAIR SHARE (%)', 'INTERACTION INDEX']
    # Category Expansion & Contraction Legend
    EXP_CON_LEG = ['Gains to ' + PROD, 'Losses, due to Category Expansion/Contraction', 'Net Change']
    # Category Expansion & Contraction Legend [CG]
    EXP_CON_LEG_CG = ['Gains to ' + CG_PROD, 'Losses, due to Category Expansion/Contraction', 'Net Change']
    # Brand Shifting Tab Dropdown
    SHIFT_DROP = ['Product Only', 'Product at Channel', 'Product at Retailer', 'Product at Banner']
    # Brand Shifting Tab Legend
    SHIFT_LEG = ['Gains', 'Losses, from Brand Shifting', 'Net Change']
    # Brand Shifting Header Format
    SHIFT_FORM = ['Product', 'Product at Channel', 'Product at Retailer', 'Product at Banner']
