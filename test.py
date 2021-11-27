from utils.parse_args import parse_args
from unittest import TestLoader, TextTestRunner, TestSuite
# Login Tests
from login.login import InsightsLogin
# Navigation Tests
from navigation.other_nav import OtherNav
from navigation.people_nav import PeopleNav
from navigation.shopper_nav import ShopperNav
from navigation.brand_nav import BrandNav
from navigation.new_item_nav import NewItemNav
from navigation.promo_nav import PromoNav
from navigation.surveys_nav import SurveysNav
from navigation.tools_nav import ToolsNav
from navigation.labs_nav import LabsNav
# Details Tests
from test_reports.test_readonly import ReadOnly
from test_reports.report_details import ReportDetails
# People Groups Tests
from groups.people_group_create import CreatePeopleGroup
from groups.people_group_share import SharePeopleGroup
from groups.people_group_details import PeopleGroupDetails
from groups.people_group_rename import RenamePeopleGroup
from groups.people_group_delete import DeletePeopleGroup
# Trip Groups Tests
from groups.trip_group_create import CreateTripGroup
from groups.trip_group_share import ShareTripGroup
from groups.trip_group_details import TripGroupDetails
from groups.trip_group_rename import RenameTripGroup
from groups.trip_group_delete import DeleteTripGroup
# Product Groups Tests
from groups.adv_group_create import CreateAdvGroup
from groups.adv_group_add import AddAdvGroup
from groups.adv_group_share import ShareAdvGroup
from groups.adv_group_rename import RenameAdvGroup
from groups.adv_group_delete import DeleteAdvGroup
# Store Groups Tests
from groups.store_group_create import CreateStoreGroup
from groups.store_group_add import AddStoreGroup
from groups.store_group_rename import RenameStoreGroup
from groups.store_group_delete import DeleteStoreGroup
# Run Reports - People Insights
from run_reports.shopper_profile import RunShopperProfile
from run_reports.basket_affinity import RunBasketAffinity
from run_reports.household_affinity import RunHouseholdAffinity
from run_reports.cross_purchase import RunCrossPurchase
from run_reports.psychographics import RunPsychographics
from run_reports.media_consumption import RunMediaConsumption
# Run Reports - Shopper Insights
from run_reports.shopper_metrics import RunShopperMetrics
from run_reports.leakage_tree import RunLeakageTree
from run_reports.shopper_histogram import RunShopperHistogram
from run_reports.trip_type_profile import RunTripTypeProfile
from run_reports.lapsed_repeat_new import RunLapsedRepeatNew
from run_reports.trip_circuits import RunTripCircuits
from run_reports.promotion_effectiveness import RunPromotionEffectiveness
from run_reports.retailer_share_wallet import RunRetailerShareWallet
from run_reports.store_diagnostics import RunStoreDiagnostics
from run_reports.store_loyalty_flow import RunStoreLoyaltyFlow
# Run Reports - Brand Insights
from run_reports.brand_diagnostics import RunBrandDiagnostics
from run_reports.data_explorer import RunDataExplorer
from run_reports.share_explorer import RunShareExplorer
from run_reports.moments_of_truth import RunMomentsOfTruth
from run_reports.bricks_clicks import RunBricksClicks
from run_reports.buyer_loyalty_flow import RunBuyerLoyaltyFlow
from run_reports.brand_switching import RunBrandSwitching
from run_reports.ebsova import RunEBSOVA
from run_reports.people_scorecard import RunPeopleScorecard
from run_reports.trended_metrics import RunTrendedMetrics
# Run Reports - New Item Insights
from run_reports.new_item_tracker import RunNewItemTracker
from run_reports.new_item_sova import RunNewItemSOVA
# Run Reports - Promo Insights
from run_reports.promotion_scorecard import RunPromotionScorecard
from run_reports.event_analysis import RunEventAnalysis
from run_reports.retailer_circular_analysis import RunRetailerCircularAnalysis
# Run Reports - Tools Module
from run_reports.product_hierarchy import RunProductHierarchy
from run_reports.store_hierarchy import RunStoreHierarchy
from run_reports.pepsi_shopper_circuits import RunPepsiShopperCircuits
# Run Reports - Labs Module
from run_reports.count_report import RunCountReport
from run_reports.user_id_fetch import RunUserIDFetch
from run_reports.high_med_low import RunHighMedLow
# RV Run Reports
from run_rv_reports.shopper_metrics_rv import RunShopperMetricsRV
from run_rv_reports.leakage_tree_rv import RunLeakageTreeRV
from run_rv_reports.shopper_histogram_rv import RunShopperHistogramRV
from run_rv_reports.trip_type_profile_rv import RunTripTypeProfileRV
from run_rv_reports.lapsed_repeat_new_rv import RunLapsedRepeatNewRV
from run_rv_reports.trip_circuits_rv import RunTripCircuitsRV
# CG Run Reports - People Insights
from run_cg_reports.shopper_profile_cg import RunShopperProfileCG
from run_cg_reports.basket_affinity_cg import RunBasketAffinityCG
from run_cg_reports.household_affinity_cg import RunHouseholdAffinityCG
from run_cg_reports.cross_purchase_cg import RunCrossPurchaseCG
# CG Run Reports - Shopper Insights
from run_cg_reports.shopper_metrics_cg import RunShopperMetricsCG
from run_cg_reports.leakage_tree_cg import RunLeakageTreeCG
from run_cg_reports.shopper_histogram_cg import RunShopperHistogramCG
from run_cg_reports.trip_type_profile_cg import RunTripTypeProfileCG
from run_cg_reports.lapsed_repeat_new_cg import RunLapsedRepeatNewCG
from run_cg_reports.trip_circuits_cg import RunTripCircuitsCG
from run_cg_reports.promotion_effectiveness_cg import RunPromotionEffectivenessCG
from run_cg_reports.retailer_share_wallet_cg import RunRetailerShareWalletCG
from run_cg_reports.store_diagnostics_cg import RunStoreDiagnosticsCG
from run_cg_reports.store_loyalty_flow_cg import RunStoreLoyaltyFlowCG
# CG Run Reports - Brand Insights
from run_cg_reports.brand_diagnostics_cg import RunBrandDiagnosticsCG
from run_cg_reports.data_explorer_cg import RunDataExplorerCG
from run_cg_reports.share_explorer_cg import RunShareExplorerCG
from run_cg_reports.bricks_clicks_cg import RunBricksClicksCG
from run_cg_reports.buyer_loyalty_flow_cg import RunBuyerLoyaltyFlowCG
from run_cg_reports.brand_switching_cg import RunBrandSwitchingCG
from run_cg_reports.ebsova_cg import RunEBSOVACG
from run_cg_reports.people_scorecard_cg import RunPeopleScorecardCG
from run_cg_reports.trended_metrics_cg import RunTrendedMetricsCG
# CG Run Reports - New Item Module
from run_cg_reports.new_item_tracker_cg import RunNewItemTrackerCG
from run_cg_reports.new_item_sova_cg import RunNewItemSOVACG
# CG Run Reports - Promo Insights
from run_cg_reports.event_analysis_cg import RunEventAnalysisCG
# CG Run Reports - Labs Module
from run_cg_reports.count_report_cg import RunCountReportCG
from run_cg_reports.high_med_low_cg import RunHighMedLowCG
# Completed Report Tests - People Insights
from test_reports.reports.shopper_profile import TestShopperProfile, TestShopperProfileCG
from test_reports.reports.basket_affinity import TestBasketAffinity, TestBasketAffinityCG
from test_reports.reports.household_affinity import TestHouseholdAffinity, TestHouseholdAffinityCG
from test_reports.reports.cross_purchase import TestCrossPurchase, TestCrossPurchaseCG
from test_reports.reports.psychographics import TestPsychographics
from test_reports.reports.media_consumption import TestMediaConsumption
# Completed Report Tests - Shopper Insights
from test_reports.reports.shopper_metrics import TestShopperMetrics, TestShopperMetricsRV, TestShopperMetricsCG
from test_reports.reports.leakage_tree import TestLeakageTree, TestLeakageTreeRV, TestLeakageTreeCG
from test_reports.reports.shopper_histogram import TestShopperHistogram, TestShopperHistogramRV, TestShopperHistogramCG
from test_reports.reports.trip_type_profile import TestTripTypeProfile, TestTripTypeProfileRV, TestTripTypeProfileCG
from test_reports.reports.lapsed_repeat_new import TestLapsedRepeatNew, TestLapsedRepeatNewRV, TestLapsedRepeatNewCG
from test_reports.reports.trip_circuits import TestTripCircuits, TestTripCircuitsRV, TestTripCircuitsCG
from test_reports.reports.promotion_effectiveness import TestPromotionEffectiveness, TestPromotionEffectivenessCG
from test_reports.reports.retailer_share_wallet import TestRetailerShareWallet, TestRetailerShareWalletCG
from test_reports.reports.store_diagnostics import TestStoreDiagnostics, TestStoreDiagnosticsCG
from test_reports.reports.store_loyalty_flow import TestStoreLoyaltyFlow, TestStoreLoyaltyFlowCG
# Completed Report Tests - Brand Insights
from test_reports.reports.brand_diagnostics import TestBrandDiagnostics, TestBrandDiagnosticsCG
from test_reports.reports.data_explorer import TestDataExplorer, TestDataExplorerCG
from test_reports.reports.share_explorer import TestShareExplorer, TestShareExplorerCG
from test_reports.reports.moments_of_truth import TestMomentsOfTruth
from test_reports.reports.bricks_clicks import TestBricksClicks, TestBricksClicksCG
from test_reports.reports.buyer_loyalty_flow import TestBuyerLoyaltyFlow, TestBuyerLoyaltyFlowCG
from test_reports.reports.brand_switching import TestBrandSwitching, TestBrandSwitchingCG
from test_reports.reports.ebsova import TestEBSOVA, TestEBSOVACG
from test_reports.reports.people_scorecard import TestPeopleScorecard, TestPeopleScorecardCG
from test_reports.reports.trended_metrics import TestTrendedMetrics, TestTrendedMetricsCG
# Completed Report Tests - New Item Insights
from test_reports.reports.new_item_tracker import TestNewItemTracker, TestNewItemTrackerCG
from test_reports.reports.new_item_sova import TestNewItemSOVA, TestNewItemSOVACG
# Completed Report Tests - Promo Module
from test_reports.reports.promotion_scorecard import TestPromotionScorecard
from test_reports.reports.event_analysis import TestEventAnalysis, TestEventAnalysisCG
from test_reports.reports.retailer_circular_analysis import TestRetailerCircularAnalysis
# Completed Report Tests - Tools Module
from test_reports.reports.product_hierarchy import TestProductHierarchy
from test_reports.reports.store_hierarchy import TestStoreHierarchy
from test_reports.reports.pepsi_shopper_circuits import TestPepsiShopperCircuits
# Completed Report Tests - Labs Module
from test_reports.reports.count_report import TestCountReport, TestCountReportCG
from test_reports.reports.user_id_fetch import TestUserIDFetch
from test_reports.reports.high_med_low import TestHighMedLow, TestHighMedLowCG

# Basic Tests
login = [InsightsLogin]
navigation = [OtherNav, PeopleNav, ShopperNav, BrandNav, NewItemNav,
              PromoNav, SurveysNav, ToolsNav, LabsNav]
details = [ReadOnly, ReportDetails]
# Combine Basic Tests
basic_tests = (login + navigation + details)

# Groups Tests
people_groups = [CreatePeopleGroup, SharePeopleGroup, PeopleGroupDetails, RenamePeopleGroup, DeletePeopleGroup]
trip_groups = [CreateTripGroup, ShareTripGroup, TripGroupDetails, RenameTripGroup, DeleteTripGroup]
adv_groups = [CreateAdvGroup, AddAdvGroup, ShareAdvGroup, RenameAdvGroup, DeleteAdvGroup]
store_groups = [CreateStoreGroup, AddStoreGroup, RenameStoreGroup, DeleteStoreGroup]
# Combine Groups Tests
groups = (people_groups + trip_groups + adv_groups + store_groups)

# Run Report Tests by Module
run_people = [RunShopperProfile, RunBasketAffinity, RunHouseholdAffinity,
              RunCrossPurchase, RunPsychographics, RunMediaConsumption]
run_shopper = [RunShopperMetrics, RunLeakageTree, RunShopperHistogram,
               RunTripTypeProfile, RunLapsedRepeatNew, RunTripCircuits,
               RunPromotionEffectiveness, RunRetailerShareWallet,
               RunStoreDiagnostics, RunStoreLoyaltyFlow]
run_brand = [RunBrandDiagnostics, RunDataExplorer, RunShareExplorer,
             RunMomentsOfTruth, RunBricksClicks, RunBuyerLoyaltyFlow,
             RunBrandSwitching, RunEBSOVA, RunPeopleScorecard,
             RunTrendedMetrics]
run_new_item = [RunNewItemTracker, RunNewItemSOVA]
run_promo = [RunPromotionScorecard, RunEventAnalysis, RunRetailerCircularAnalysis]
run_tools = [RunProductHierarchy, RunStoreHierarchy, RunPepsiShopperCircuits]
run_labs = [RunCountReport, RunUserIDFetch, RunHighMedLow]
# Combine Run Report Tests
run_reports = (run_people + run_shopper + run_brand + run_new_item
               + run_promo + run_tools + run_labs)

# Run RV Reports Tests (Retailer View)
run_rv_reports = [RunShopperMetricsRV, RunLeakageTreeRV, RunShopperHistogramRV,
                  RunTripTypeProfileRV, RunLapsedRepeatNewRV, RunTripCircuitsRV]

# Run CG Reports Tests by Module (Custom Groups)
run_people_cg = [RunShopperProfileCG, RunBasketAffinityCG, RunHouseholdAffinityCG,
                 RunCrossPurchaseCG]
run_shopper_cg = [RunShopperMetricsCG, RunLeakageTreeCG, RunShopperHistogramCG,
                  RunTripTypeProfileCG, RunLapsedRepeatNewCG, RunTripCircuitsCG,
                  RunPromotionEffectivenessCG, RunRetailerShareWalletCG,
                  RunStoreDiagnosticsCG, RunStoreLoyaltyFlowCG]
run_brand_cg = [RunBrandDiagnosticsCG, RunDataExplorerCG, RunShareExplorerCG,
                RunBricksClicksCG, RunBuyerLoyaltyFlowCG, RunBrandSwitchingCG,
                RunEBSOVACG, RunPeopleScorecardCG, RunTrendedMetricsCG]
run_new_item_cg = [RunNewItemTrackerCG, RunNewItemSOVACG]
run_promo_cg = [RunEventAnalysisCG]
run_labs_cg = [RunCountReportCG, RunHighMedLowCG]
# Combine CG Reports Tests
run_cg_reports = (run_people_cg + run_shopper_cg + run_brand_cg
                  + run_new_item_cg + run_promo_cg + run_labs_cg)

# Completed Report Tests by Module
test_people = [TestShopperProfile, TestBasketAffinity, TestHouseholdAffinity,
               TestCrossPurchase, TestPsychographics, TestMediaConsumption]
test_shopper = [TestShopperMetrics, TestLeakageTree, TestShopperHistogram,
                TestTripTypeProfile, TestLapsedRepeatNew, TestTripCircuits,
                TestPromotionEffectiveness, TestRetailerShareWallet,
                TestStoreDiagnostics, TestStoreLoyaltyFlow]
test_brand = [TestBrandDiagnostics, TestDataExplorer, TestShareExplorer,
              TestMomentsOfTruth, TestBricksClicks, TestBuyerLoyaltyFlow,
              TestBrandSwitching, TestEBSOVA, TestPeopleScorecard,
              TestTrendedMetrics]
test_new_item = [TestNewItemTracker, TestNewItemSOVA]
test_promo = [TestPromotionScorecard, TestEventAnalysis, TestRetailerCircularAnalysis]
test_tools = [TestProductHierarchy, TestStoreHierarchy, TestPepsiShopperCircuits]
test_labs = [TestCountReport, TestUserIDFetch, TestHighMedLow]
# Combine Completed Report Tests
completed_reports = (test_people + test_shopper + test_brand + test_new_item
                     + test_promo + test_tools + test_labs)

# Completed RV Reports Tests
completed_rv_reports = [TestShopperMetricsRV, TestLeakageTreeRV, TestShopperHistogramRV,
                        TestTripTypeProfileRV, TestLapsedRepeatNewRV, TestTripCircuitsRV]

# Completed CG Reports Tests
test_people_cg = [TestShopperProfileCG, TestBasketAffinityCG, TestHouseholdAffinityCG,
                  TestCrossPurchaseCG]
test_shopper_cg = [TestShopperMetricsCG, TestLeakageTreeCG, TestShopperHistogramCG,
                   TestTripTypeProfileCG, TestLapsedRepeatNewCG, TestTripCircuitsCG,
                   TestPromotionEffectivenessCG, TestRetailerShareWalletCG,
                   TestStoreDiagnosticsCG, TestStoreLoyaltyFlowCG]
test_brand_cg = [TestBrandDiagnosticsCG, TestDataExplorerCG, TestShareExplorerCG,
                 TestBricksClicksCG, TestBuyerLoyaltyFlowCG, TestBrandSwitchingCG,
                 TestEBSOVACG, TestPeopleScorecardCG, TestTrendedMetricsCG]
test_new_item_cg = [TestNewItemTrackerCG, TestNewItemSOVACG]
test_promo_cg = [TestEventAnalysisCG]
test_labs_cg = [TestCountReportCG, TestHighMedLowCG]
# Combine Completed CG Tests
completed_cg_reports = (test_people_cg + test_shopper_cg + test_brand_cg
                        + test_new_item_cg + test_promo_cg + test_labs_cg)

# Combine All Test Classes
test_classes = (basic_tests + groups + run_reports + run_rv_reports + run_cg_reports
                + completed_reports + completed_rv_reports + completed_cg_reports)

# Module Test Text
module_text = ['Login', 'Navigation', 'Details', 'BasicTests',
               'PeopleGroups', 'TripGroups', 'AdvancedGroups', 'StoreGroups', 'Groups',
               'RunPeople', 'RunShopper', 'RunBrand', 'RunNewItem',
               'RunPromo', 'RunTools', 'RunLabs', 'RunReports',
               'RunRVReports',
               'RunPeopleCG', 'RunShopperCG', 'RunBrandCG',
               'RunNewItemCG', 'RunPromoCG', 'RunLabsCG',
               'RunCGReports',
               'TestPeople', 'TestShopper', 'TestBrand', 'TestNewItem',
               'TestPromo', 'TestTools', 'TestLabsModule',
               'CompletedReports', 'CompletedRVReports',
               'TestPeopleCG', 'TestShopperCG', 'TestBrandCG',
               'TestNewItemCG', 'TestPromoCG', 'TestLabsModuleCG',
               'CompletedCGReports']
# Module Test Classes
test_modules = [login, navigation, details, basic_tests,
                people_groups, trip_groups, adv_groups, store_groups, groups,
                run_people, run_shopper, run_brand, run_new_item,
                run_promo, run_tools, run_labs, run_reports,
                run_rv_reports,
                run_people_cg, run_shopper_cg, run_brand_cg,
                run_new_item_cg, run_promo_cg, run_labs_cg,
                run_cg_reports,
                test_people, test_shopper, test_brand, test_new_item,
                test_promo, test_tools, test_labs,
                completed_reports, completed_rv_reports,
                test_people_cg, test_shopper_cg, test_brand_cg,
                test_new_item_cg, test_promo_cg, test_labs_cg,
                completed_cg_reports]

_, _, _, _, test = parse_args()

if __name__ == '__main__':
    # Initialize Test Objects
    loader = TestLoader()
    # TODO: https://docs.python.org/3.3/library/unittest.html#unittest.Test Result tell cbt pass/fail
    runner = TextTestRunner(failfast=True)
    # Create Loaded Test Instances
    suites_list = []
    num_tests = 0
    if test == ['ALL']:
        for tc in test_classes:
            suites_list.append(loader.loadTestsFromTestCase(tc))
    else:
        for t in test:
            for tc in test_classes:
                if t == tc.__name__:
                    suites_list.append(loader.loadTestsFromTestCase(tc))
                    num_tests += 1
                    continue
            for m, mod in enumerate(module_text):
                if t == mod:
                    num_tests += 1
                    for tm in test_modules[m]:
                        suites_list.append(loader.loadTestsFromTestCase(tm))
                        continue
        if num_tests != len(test):
            raise Exception('No test(s) selected, or test not found')
    allSuites = TestSuite(suites_list)
    # Execute Test(s)
    runner.run(allSuites)
