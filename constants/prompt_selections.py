from enum import Enum
from constants.enums import PromptElements
from constants.dictionaries import RETAILER_PG, LOCATION, GEO_ATTRIBUTE, PANEL_STORE, BANNER
from utils.parse_args import parse_args
_, _, _, panel, _ = parse_args()

# People Insights Reports


class SP(Enum):  # Shopper Profile
    PG = RETAILER_PG[panel]
    COMP_PG = None
    DATE = PromptElements.LATEST_52_WEEKS.value
    PROD = 'Heinz'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Heinz'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Condiments'
    CAT_LEV = PromptElements.DEPARTMENT.value
    CAT_SEL = 'Grocery'
    CG_CAT = 'Department in Condiments'
    CG_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    STORE = None
    STORE_LEV = None
    COMP_PROD = 'Kraft'
    COMP_PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_COMP_PROD = 'Parent Brand in Kraft'
    CG_COMP_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    COMP_CAT = 'Condiments'
    COMP_CAT_LEV = PromptElements.DEPARTMENT.value
    COMP_CAT_SEL = 'Grocery'
    CG_COMP_CAT = 'Department in Condiments'
    CG_COMP_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    COMP_STORE = None
    COMP_STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class BA(Enum):  # Basket Affinity
    PROD = 'Coca-Cola'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Coca-Cola'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Soft Drinks'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CG_CAT = 'Major Category in Soft Drinks'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    CAT_SEL = 'Beverages'
    PROD_LEV_1 = PromptElements.CATEGORY.value
    PROD_LEV_2 = PromptElements.PARENT_BRAND.value
    COMP_PROD = 'Soft Drinks'
    COMP_PROD_LEV = PromptElements.MAJOR_CAT.value
    COMP_PROD_SEL = 'Beverages'
    DATE = PromptElements.LATEST_12_MONTHS.value
    PG = 'Repeat Soft Drinks Buyers'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    WEIGHT = PromptElements.DEFAULT.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class HA(Enum):  # Household Affinity
    PROD = None
    PROD_LEV = None
    CG_PROD = None
    CG_PROD_LEV = None
    CAT = 'Laundry'
    CAT_LEV = PromptElements.DEPARTMENT.value
    CAT_SEL = 'Household'
    CG_CAT = 'Department in Laundry'
    CG_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    PG = 'Tide Buyers'
    COMP_PG = None
    PROD_LEV_1 = PromptElements.BRAND.value
    PROD_LEV_2 = PromptElements.CATEGORY.value
    PROD_LEV_3 = PromptElements.PARENT_BRAND.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    STORE = None
    STORE_LEV = None
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class CP(Enum):  # Cross Purchase
    PROD = 'Beer'
    PROD_LEV = PromptElements.MAJOR_CAT.value
    PROD_SEL = 'Alcohol Beverages'
    CG_PROD = 'Major Category in Beer'
    CG_PROD_LEV = PromptElements.CG_MAJOR_CAT.value
    PROD_LEVEL = PromptElements.PARENT_BRAND.value
    COMP_PROD = 'Chips'
    COMP_PROD_LEV = PromptElements.MAJOR_CAT.value
    COMP_PROD_SEL = 'Snack'
    CG_COMP_PROD = 'Major Category in Chips'
    CG_COMP_PROD_LEV = PromptElements.CG_MAJOR_CAT.value
    COMP_PROD_LEVEL = PromptElements.PARENT_BRAND.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Beer & Chips Buyers'
    FOCUS_CAT = None
    FOCUS_CAT_LEV = None
    FOCUS_CAT_SEL = None
    FOCUS_STORE = None
    FOCUS_STORE_LEV = None
    COMP_CAT = None
    COMP_CAT_LEV = None
    COMP_CAT_SEL = None
    COMP_STORE = None
    COMP_STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class PSY(Enum):  # Psychographics
    PG = 'Vegan Shoppers'
    COMP_PG = None
    DATE = PromptElements.LATEST_52_WEEKS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class MC(Enum):  # Media Consumption
    PG = 'Vegan Shoppers'
    COMP_PG = None
    DATE = PromptElements.LATEST_52_WEEKS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value

# Groups Module


class PG(Enum):  # People Group
    STORE = PromptElements.FMCG.value
    STORE_LEV = PromptElements.PARENT_CHANNEL.value
    PRODUCT = 'Red Bull'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CATEGORY = 'Energy Drinks'
    CAT_LEV = PromptElements.CATEGORY.value
    CAT_SELECT = 'Sports & Energy Drinks'
    AGE = '18-20'
    AGE_FOLDER = PromptElements.AGE_BRACKETS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CUSTOM_FILTER = PromptElements.TOTAL_TRIP_COUNT.value
    FILTER_VALUE = '1'
    FIXED_FILTER = PromptElements.TWO_TRIPS.value


class TG(Enum):  # Trip Group
    GENDER = 'Female Adult Only'
    GENDER_FOLDER = PromptElements.ADULT_GENDERS.value
    KIDS = 'No Kids'
    KID_FOLDER = PromptElements.KIDS.value
    DAY = 'Friday'
    DAY_FOLDER = (PromptElements.DAY_OF_WEEK.value)


class ADVG(Enum):  # Advanced Group
    PROD_LEV_1 = PromptElements.MAJOR_CAT.value
    PROD_LEV_OP_1 = PromptElements.IN.value
    MAJOR_CAT = 'Chips'
    CLOSE = PromptElements.CLOSE_STATEMENT.value
    CLOSED = PromptElements.CLOSED_CONDITION.value
    CONJ_OP = PromptElements.AND.value
    PROD_LEV_2 = PromptElements.PARENT_BRAND.value
    PROD_LEV_OP_2 = PromptElements.IN.value
    PARENT_BRAND = 'Doritos'


class ADVADD(Enum):  # Added Advanced Group
    PROD_LEV_1 = PromptElements.MAJOR_CAT.value
    PROD_LEV_OP_1 = PromptElements.IN.value
    CLOSE = PromptElements.CLOSE_STATEMENT.value
    CLOSED = PromptElements.CLOSED_CONDITION.value
    CONJ_OP = PromptElements.AND.value
    PROD_LEV_2 = PromptElements.PARENT_BRAND.value
    PROD_LEV_OP_2 = PromptElements.IN.value
    MAJOR_CAT = 'Puffed Snacks'
    PARENT_BRAND = 'Cheetos'


class STGR(Enum):   # Store Group
    STORE_LEV = PromptElements.PARENT_CHANNEL.value
    PROD_LEV_OP_1 = PromptElements.IN.value
    PROD_LEV_OP_2 = PromptElements.NOT_IN.value
    STORE = PromptElements.FMCG.value
    STORE_2 = PromptElements.ECOMMERCE.value
    CLOSE = PromptElements.CLOSE_STATEMENT.value
    CLOSED = PromptElements.CLOSED_CONDITION.value
    CONJ_OP = PromptElements.AND.value


class STGRADD(Enum):  # Added Store Group
    STORE_LEV = PromptElements.PARENT_CHANNEL.value
    PROD_LEV_OP_1 = PromptElements.IN.value
    PROD_LEV_OP_2 = PromptElements.NOT_IN.value
    STORE = PromptElements.FMCG.value
    STORE_2 = PromptElements.ECOMMERCE.value
    CLOSE = PromptElements.CLOSE_STATEMENT.value
    CLOSED = PromptElements.CLOSED_CONDITION.value
    CONJ_OP = PromptElements.AND.value

# Shopper Module


class SM(Enum):  # Shopper Metrics
    PROD = 'Doritos'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Doritos'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Chips'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Snack'
    CG_CAT = 'Major Category in Chips'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    LEV = PromptElements.BANNER.value
    LEV_LEV = PromptElements.STORE_ATTR.value
    STORE = None
    STORE_LEV = None
    RV_STORE = PANEL_STORE[panel]
    RV_STORE_LEV = PromptElements.RETAILER.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Beer & Chips Buyers'
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class LT(Enum):  # Leakage Tree
    PROD = 'Corona'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Corona'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Beer'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Alcohol Beverages'
    CG_CAT = 'Major Category in Beer'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    STORE = PANEL_STORE[panel]
    STORE_LEV = PromptElements.RETAILER.value
    RV_STORE = BANNER[panel]
    RV_STORE_LEV = PromptElements.RETAILER.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Beer & Chips Buyers'
    STORE_LEVEL = None
    BENCHMARK = PromptElements.TOP_STORES.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    STAT = PromptElements.BRICK_MORTAR.value


class SH(Enum):  # Shopper Histogram
    PROD = 'Barilla'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Barilla'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Pasta'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Pasta & Noodles'
    CG_CAT = 'Major Category in Pasta'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    DATE = PromptElements.LATEST_12_WEEKS.value
    OUT = PromptElements.REMOVE_OUTLIERS.value
    OUT_LEV = PromptElements.INCLUDE_OUTLIERS.value
    PG = 'Pasta & Noodles Buyers'
    BIN_1 = PromptElements.BIN_AVG_SPEND.value
    BIN_2 = PromptElements.BIN_TOTAL_SPEND.value
    BIN_3 = PromptElements.BIN_SPEND_UNIT_TRIP.value
    WIDTH = 1
    LOWER = 5
    UPPER = 15
    STORE = PANEL_STORE[panel]
    STORE_LEV = PromptElements.RETAILER.value
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class TTP(Enum):  # Trip Type Profile
    CAT = 'Bath Tissue'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Paper & Plastic'
    CG_CAT = 'Major Category in Bath Tissue'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    PROD_LEV = PromptElements.PARENT_BRAND.value
    RV_PROD_LEV = PromptElements.DEPARTMENT.value
    STORE = None
    STORE_LEV = None
    RV_STORE = PANEL_STORE[panel]
    RV_STORE_LEV = PromptElements.RETAILER.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Millennial Shoppers'
    STORE_LEVEL = PromptElements.BANNER.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class LRN(Enum):  # Lapsed, Repeat, New
    PROD = 'Sargento'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Sargento'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Cheese'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Dairy'
    CG_CAT = 'Major Category in Cheese'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    STORE = None
    STORE_LEV = None
    RV_STORE = PANEL_STORE[panel]
    RV_STORE_LEV = PromptElements.BANNER.value
    DATE = PromptElements.LATEST_12_MONTHS.value
    PERIOD = PromptElements.PRIOR_PERIOD.value
    PERIOD_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    PROD_LEVEL = None
    STORE_LEVEL = None
    PG = 'Millennial Shoppers'
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class TC(Enum):  # Trip Circuits
    TYPE_LEV = PromptElements.TRIP_CIRCUIT_TYPE.value
    TYPE = PromptElements.SAME_WEEK_CIRCUIT.value
    PROD = None
    PROD_LEV = None
    CG_PROD = None
    CG_PROD_LEV = None
    CAT = 'Cold Cereal'
    CAT_LEV = PromptElements.CATEGORY.value
    CAT_SEL = 'Breakfast Cereal'
    CG_CAT = 'Category in Cold Cereal'
    CG_CAT_LEV = PromptElements.CG_CAT.value
    STORE = 'Walmart'
    STORE_LEV = PromptElements.BANNER.value
    RV_STORE = PANEL_STORE[panel]
    RV_STORE_LEV = PromptElements.RETAILER.value
    PG = 'Millennial Shoppers'
    TG = 'Fri-Sun Shoppers'
    PROD_LEV_PROMPT = None
    GROUP_PROD_LEV = None
    STORE_LEVEL = None
    DATE = PromptElements.LATEST_52_WEEKS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class PE(Enum):  # Promotion Effectiveness
    PROD = 'Neutrogena'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Neutrogena'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Skin Care'
    CAT_LEV = PromptElements.DEPARTMENT.value
    CAT_SEL = 'Health & Beauty'
    CG_CAT = 'Department in Skin Care'
    CG_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    STORE = PANEL_STORE[panel]
    STORE_LEV = PromptElements.RETAILER.value
    START = '04/29/2018'
    END = '06/02/2018'
    PORT = None
    PORT_LEV = None
    PRE = PromptElements.WEEKS_26.value
    PRE_LEV = PromptElements.NUM_WEEKS_BEFORE.value
    POST = PromptElements.WEEKS_13.value
    POST_LEV = PromptElements.NUM_WEEKS_AFTER.value
    PG = 'Gen X - Seniors'
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class RSOW(Enum):  # Retailer Share of Wallet
    PROD_LEV_1 = PromptElements.BRAND.value
    PROD_LEV_2 = PromptElements.CATEGORY.value
    CAT = 'Wine'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Alcohol Beverages'
    CG_CAT = 'Major Category in Wine'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    STORE = PANEL_STORE[panel]
    STORE_LEV = PromptElements.RETAILER.value
    DATE = PromptElements.LATEST_12_MONTHS.value
    PG = 'Millennial Shoppers'
    PRIOR = PromptElements.PRIOR_PERIOD.value
    PRIOR_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    STORE_LEVEL = None
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class SD(Enum):  # Store Diagnostics
    PROD = 'Oscar Mayer Lunchables'
    PROD_LEV = PromptElements.BRAND.value
    CG_PROD = 'Brand in Oscar Mayer Lunchables'
    CG_PROD_LEV = PromptElements.CG_BRAND.value
    STORE = BANNER[panel]
    STORE_LEV = PromptElements.BANNER.value
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    PG = 'Parents'
    DATE = PromptElements.LATEST_12_MONTHS.value
    PERIOD = PromptElements.YEAR_AGO.value
    PERIOD_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    STORE_LEVEL = None
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class SLF(Enum):  # Store Loyalty Flow
    PROD = 'Dasani'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Dasani'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    STORE = PANEL_STORE[panel]
    STORE_LEV = PromptElements.RETAILER.value
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    PG = 'Water Buyers'
    DATE = PromptElements.LATEST_12_MONTHS.value
    PERIOD = PromptElements.YEAR_AGO.value
    PERIOD_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value

# Brand Module


class BD(Enum):  # Brand Diagnostics
    PROD = 'Crest'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Crest'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Toothpaste'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Oral Hygiene'
    CG_CAT = 'Major Category in Toothpaste'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Toothpaste Buyers'
    PROD_LEVEL = PromptElements.CATEGORY.value
    PERIOD = PromptElements.YEAR_AGO.value
    PERIOD_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = None
    GEO_LEV = None
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class DE(Enum):  # Data Explorer
    MET_1 = PromptElements.PROJ_HH.value
    MET_1_LEV = PromptElements.PROJ_METRICS.value
    MET_2 = PromptElements.SHARE_CAT_UNITS.value
    MET_2_LEV = PromptElements.LOYALTY_METRICS.value
    MET_3 = PromptElements.SHARE_WALLET.value
    MET_3_LEV = PromptElements.LEAKAGE_METRICS.value
    MET_4 = PromptElements.SPEND_TRIP.value
    MET_4_LEV = PromptElements.CORE_METRICS.value
    LEV_1 = PromptElements.PARENT_BRAND.value
    LEV_1_LEV = PromptElements.PROD_ATTR.value
    LEV_2 = PromptElements.BRAND.value
    LEV_2_LEV = PromptElements.PROD_ATTR.value
    LEV_3 = PromptElements.SUBCAT.value
    LEV_3_LEV = PromptElements.PROD_ATTR.value
    LEV_4 = PromptElements.SECTOR.value
    LEV_4_LEV = PromptElements.PROD_ATTR.value
    LEV_5 = PromptElements.DEPARTMENT.value
    LEV_5_LEV = PromptElements.PROD_ATTR.value
    LEV_6 = PromptElements.MAJOR_CAT.value
    LEV_6_LEV = PromptElements.PROD_ATTR.value
    LEV_7 = PromptElements.CATEGORY.value
    LEV_7_LEV = PromptElements.PROD_ATTR.value
    LEV_8 = PromptElements.PARENT_CHANNEL.value
    LEV_8_LEV = PromptElements.STORE_ATTR.value
    PROD = 'Yoplait'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Yoplait'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Yogurt'
    CAT_LEV = PromptElements.CATEGORY.value
    CAT_SEL = 'Yogurt & Yogurt Drinks'
    CG_CAT = 'Category in Yogurt'
    CG_CAT_LEV = PromptElements.CG_CAT.value
    DATE = PromptElements.LATEST_12_MONTHS.value
    PG = 'Millennial Shoppers'
    PERIOD = None
    PERIOD_LEV = None
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    CUSTOM = None
    CUSTOM_LEV = None
    ADJUST = PromptElements.TCC_TENURE.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class SE(Enum):  # Share Explorer
    PROD = "Kellogg's"
    PROD_LEV = PromptElements.BRAND.value
    CG_PROD = "Brand in Kellogg's"
    CG_PROD_LEV = PromptElements.CG_BRAND.value
    CAT = 'Cold Cereal'
    CAT_LEV = PromptElements.CATEGORY.value
    CAT_SEL = 'Breakfast Cereal'
    CG_CAT = 'Category in Cold Cereal'
    CG_CAT_LEV = PromptElements.CG_CAT.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    SPLIT = PromptElements.FROM_PRIOR_PERIOD.value
    SPLIT_LEV = PromptElements.SPLIT_OPTIONS.value
    LEV = PromptElements.BRAND.value
    LEV_LEV = PromptElements.PROD_ATTR.value
    PG = 'Millennial Shoppers'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class MOT(Enum):  # Moments of Truth
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CAT = 'Dog Food & Treats'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Pet Food & Treats'
    PG = 'Pet (Sector) Buyers'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class BC(Enum):  # Bricks and Clicks
    CAT = 'Baking Mixes'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Baking & Cooking'
    CG_CAT = 'Major Category in Baking Mixes'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    PROD = 'Ghirardelli'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Ghirardelli'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    PG = 'Millennial Shoppers'
    DATE = PromptElements.LATEST_12_MONTHS.value
    PERIOD = PromptElements.YEAR_AGO.value
    PERIOD_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class BLF(Enum):  # Buyer Loyalty Flow
    PROD = "Hershey's"
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = "Parent Brand in Hershey's"
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Candy (Snacks)'
    CAT_LEV = PromptElements.DEPARTMENT.value
    CAT_SEL = 'Grocery'
    CG_CAT = 'Department in Candy (Snacks)'
    CG_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    DATE = PromptElements.LATEST_12_MONTHS.value
    PERIOD = PromptElements.YEAR_AGO.value
    PERIOD_LEV = PromptElements.PREV_PERIOD_OPTIONS.value
    PG = 'Parents'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    PROD_LEVEL = PromptElements.BRAND.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class BS(Enum):  # Brand Switching
    PROD = 'Coors'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Coors'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Beer'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Alcohol Beverages'
    CG_CAT = 'Major Category in Beer'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PROD_LEVEL = None
    PORT = None
    PORT_LEV = None
    PG = 'Parents'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class EBSOVA(Enum):  # Existing Brand Source of Volume
    PROD = 'Gain'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Gain'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Fabric Softener'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Laundry'
    CG_CAT = 'Major Category in Fabric Softener'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    STORE = None
    STORE_LEV = None
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Gain Buyers'
    PERIOD = PromptElements.YEAR_AGO.value
    PROD_LEVEL = PromptElements.MAJOR_CAT.value
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    WEIGHT = PromptElements.DEFAULT.value
    STAT = PromptElements.BRICK_MORTAR.value


class PS(Enum):  # People Scorecard
    CAT = 'Fruit Juice'
    CAT_LEV = PromptElements.CATEGORY.value
    CAT_SEL = 'Juices'
    CG_CAT = 'Category in Fruit Juice'
    CG_CAT_LEV = PromptElements.CG_CAT.value
    PEOPLE_LEV_1 = PromptElements.AGE_GEN.value
    PEOPLE_LEV_LEV_1 = PromptElements.DEMO_ATTR.value
    PEOPLE_LEV_2 = GEO_ATTRIBUTE[panel]
    PEOPLE_LEV_LEV_2 = PromptElements.GEO_ATTR.value
    PROD_LEV = PromptElements.PARENT_BRAND.value
    PROD_LEV_LEV = PromptElements.PROD_ATTR.value
    MET_1 = PromptElements.PERCENT_TRIPS.value
    MET_1_LEV = PromptElements.SHARE_TOTAL_METRICS.value
    MET_2 = PromptElements.PROJ_HH.value
    MET_2_LEV = PromptElements.PROJ_METRICS.value
    MET_3 = PromptElements.SHARE_CAT_UNITS.value
    MET_3_LEV = PromptElements.LOYALTY_METRICS.value
    MET_4 = PromptElements.SPEND_TRIP.value
    MET_4_LEV = PromptElements.CORE_METRICS.value
    DATE = PromptElements.LATEST_52_WEEKS.value
    PG = 'Parents'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    BENCH = PromptElements.AVG_SELECTION.value
    BENCH_LEV = PromptElements.BENCHMARK.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    CUSTOM = None
    CUSTOM_LEV = None
    ADJUST = PromptElements.TCC_TENURE.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class TM(Enum):  # Trended Metrics
    CAT = 'Household Cleaners'
    CAT_LEV = PromptElements.DEPARTMENT.value
    CAT_SEL = 'Household'
    CG_CAT = 'Department in Household Cleaners'
    CG_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    LEV_1 = PromptElements.PARENT_BRAND.value
    LEV_1_LEV = PromptElements.PROD_ATTR.value
    LEV_2 = PromptElements.BRAND.value
    LEV_2_LEV = PromptElements.PROD_ATTR.value
    LEV_3 = PromptElements.MAJOR_CAT.value
    LEV_3_LEV = PromptElements.PROD_ATTR.value
    LEV_4 = PromptElements.CATEGORY.value
    LEV_4_LEV = PromptElements.PROD_ATTR.value
    LEV_5 = PromptElements.SUBCAT.value
    LEV_5_LEV = PromptElements.PROD_ATTR.value
    MET_1 = PromptElements.PERCENT_TRIPS.value
    MET_1_LEV = PromptElements.SHARE_TOTAL_METRICS.value
    MET_2 = PromptElements.PROJ_HH.value
    MET_2_LEV = PromptElements.PROJ_METRICS.value
    MET_3 = PromptElements.SHARE_CAT_UNITS.value
    MET_3_LEV = PromptElements.LOYALTY_METRICS.value
    MET_4 = PromptElements.SPEND_TRIP.value
    MET_4_LEV = PromptElements.CORE_METRICS.value
    TIME = PromptElements.ROLL_12_QUARTER.value
    DATE = PromptElements.LATEST_12_MONTHS.value
    PG = 'Parents'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    TG = 'Fri-Sun Shoppers'
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    CUSTOM = None
    CUSTOM_LEV = None
    ADJUST = PromptElements.TCC_TENURE.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value

# New Item Module


class NIT(Enum):  # New Item Tracker
    NI_1 = 'Budweiser Reserve Copper Lager (Sep 2018)'
    NI_2 = 'Dannon Oikos Triple Zero'
    NI_3 = 'Clif Nut Butter Filled (May 2016)'
    NI_4 = 'Dannon Oikos Crunch'
    NI_5 = 'Caffe Monster Mocha (Feb 2018)'
    PG = 'Beer Buyers'
    STORE = None
    STORE_LEV = None
    LOCATION = None
    GEO_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class NISOVA(Enum):  # New Item Source of Volume
    NI_1 = 'Budweiser Reserve Copper Lager (Sep 2018)'
    NI_2 = 'Caffe Monster Mocha (Feb 2018)'
    NI_3 = 'Clif Nut Butter Filled (May 2016)'
    NI_4 = 'Dannon Oikos Crunch'
    NI_5 = 'Dannon Oikos Triple Zero'
    CAT = 'Yogurt'
    CAT_LEV = PromptElements.CATEGORY.value
    CAT_SEL = 'Yogurt & Yogurt Drinks'
    CG_CAT = 'Category in Yogurt'
    CG_CAT_LEV = PromptElements.CG_CAT.value
    PORT = None
    PORT_LEV = None
    PERIOD = PromptElements.WEEKS_52.value
    PERIOD_LEV = PromptElements.NUM_WEEKS_BEFORE.value
    PG = 'Yogurt Buyers'
    STORE = None
    STORE_LEV = None
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value

# Promo Insights


class PROS(Enum):  # Promotion Scorecard
    PROD = 'Pepsi'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CAT = 'Soft Drinks'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Beverages'
    STORE = None
    STORE_LEV = None
    START = '01/01/2019'
    END = '01/01/2020'


class EA(Enum):  # Event Analysis
    PROD = 'Nabisco'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Nabisco'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'Crackers'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Snack'
    CG_CAT = 'Major Category in Crackers'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    STORE = PANEL_STORE[panel]
    STORE_LEV = PromptElements.RETAILER.value
    START = '04/27/2018'
    END = '05/13/2018'
    PROMO = None
    PORT = None
    PORT_LEV = None
    PRE = PromptElements.WEEKS_26.value
    PRE_LEV = PromptElements.NUM_WEEKS_BEFORE.value
    POST = PromptElements.WEEKS_13.value
    POST_LEV = PromptElements.NUM_WEEKS_AFTER.value
    PG = 'Crackers Buyers'
    LOCATION = LOCATION[panel]
    GEO_LEV = GEO_ATTRIBUTE[panel]
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class RCA(Enum):  # Retailer Circular Analysis
    BANNER = BANNER[panel]
    COMP_BANNER = PANEL_STORE[panel]
    START = '01/01/2018'
    END = '01/01/2019'
    PG = None
    CAT = None
    CAT_LEV = None
    CAT_SEL = None

# Tools Module


class PH(Enum):  # Product Hierarchy
    PROD = 'Beverages'
    PROD_LEV = PromptElements.DEPARTMENT.value
    PROD_SEL = 'Grocery'


class STH(Enum):  # Store Hierarchy
    STORE = PromptElements.DRUG.value
    STORE_LEV = PromptElements.CHANNEL.value


class PSC(Enum):  # Pepsi Shopper Circuits
    RETAILER = 'Whole Foods'
    RETAILER_LEV = PromptElements.RETAILER.value
    STORE = PromptElements.PEPSI_WHOLE_FOODS.value
    CAT = 'Soft Drinks'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Beverages'
    AREA = LOCATION[panel]
    AREA_LEV = GEO_ATTRIBUTE[panel]
    PG = 'Pepsi Buyers'
    DATE = PromptElements.LATEST_52_WEEKS.value
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    WEIGHT = PromptElements.DEFAULT.value
    WEIGHT_LEV = PromptElements.CHANNEL_WEIGHTS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value

# Labs Module


class CR(Enum):  # Count Report
    PROD = None
    PROD_LEV = None
    CG_PROD = None
    CG_PROD_LEV = None
    CAT = 'Candy (Snacks)'
    CAT_LEV = PromptElements.DEPARTMENT.value
    CAT_SEL = 'Grocery'
    CG_CAT = 'Department in Candy (Snacks)'
    CG_CAT_LEV = PromptElements.CG_DEPARTMENT.value
    STORE = None
    STORE_LEV = None
    LEV_1 = PromptElements.BRAND.value
    LEV_1_LEV = PromptElements.PROD_ATTR.value
    LEV_2 = PromptElements.PARENT_BRAND.value
    LEV_2_LEV = PromptElements.PROD_ATTR.value
    LEV_3 = PromptElements.MAJOR_CAT.value
    LEV_3_LEV = PromptElements.PROD_ATTR.value
    LEV_4 = PromptElements.CATEGORY.value
    LEV_4_LEV = PromptElements.PROD_ATTR.value
    LEV_5 = PromptElements.SUBCAT.value
    LEV_5_LEV = PromptElements.PROD_ATTR.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value
    PG = 'Candy Buyers'
    DATE = PromptElements.LATEST_12_MONTHS.value
    LOCATION = None  # Dictionary
    GEO_LEV = None  # Dictionary
    TG = 'Fri-Sun Shoppers'
    CHAN = PromptElements.FMCG.value
    CHAN_LEV = PromptElements.PARENT_CHANNEL.value
    TRANS = PromptElements.FULL.value
    TRANS_LEV = PromptElements.TRANSCRIPTION_LEVEL.value


class UIDF(Enum):  # User ID Fetch
    PG = 'Vegan Shoppers'
    DATE = PromptElements.LATEST_52_WEEKS.value
    STAT = PromptElements.BRICK_MORTAR.value
    STAT_LEV = PromptElements.STATIC_OPTIONS.value


class HML(Enum):  # High, Medium, Low
    PROD = 'Windex'
    PROD_LEV = PromptElements.PARENT_BRAND.value
    CG_PROD = 'Parent Brand in Windex'
    CG_PROD_LEV = PromptElements.CG_PARENT_BRAND.value
    CAT = 'All-Purpose Cleaners'
    CAT_LEV = PromptElements.MAJOR_CAT.value
    CAT_SEL = 'Household Cleaners'
    CG_CAT = 'Major Category in All-Purpose Cleaners'
    CG_CAT_LEV = PromptElements.CG_MAJOR_CAT.value
    STORE = None
    STORE_LEV = None
    METRIC = PromptElements.BIN_ITEM_SPEND_HH.value
    HIGH = '25'
    MED = '50'
    LOW = '25'
    DATE = PromptElements.LATEST_52_WEEKS.value
    CHAN = PromptElements.FMCG.value
    PG = 'Household Cleaners Buyers'
    STORE_LEVEL = PromptElements.PARENT_CHANNEL.value
    PROD_LEVEL = PromptElements.MAJOR_CAT.value
    BENCH_PG = None
    LOCATION = None
    GEO_LEV = None
    WEIGHT = PromptElements.DEFAULT.value
    STAT = PromptElements.BRICK_MORTAR.value
