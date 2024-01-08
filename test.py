import pandas as pd

# Sample JSON data
data = {
    "Policy": {
        "in_billing_payplan_selected": "paid_in_full",
        "BrokerID": "45269912",
        "DriftedNode": {
            "DriftedNodeCol1": "1",
            "DriftedNodeCol2": "2",
            "DriftedNodeCol3": "3"
        },
        "Vehicle": [
            {
                "drc_out_rating_vehicle_bi_calculation": "BASE_RATE:294 X BASE_RELATIVITY:0_877 X PLAN_AHEAD:0_88 X ILF_DED:1_83 X TIER:0_693 X ANTI_LOCK_BRAKES:0_95 X RAPA_SYMBOLS:0_83849 X HH_COMP:0_85 X CLASS:0_917 X DRIVER_HISTORY:1_52 X MULTI_POLICY:0_95 X SAFE_DRIVER:0_99 X PAYPLAN:0_95 = MODEL_PREM (no exp fees):243 X RSF:1_067 = TOTAL_PREMIUM:259",
                "BrokerID from left table": "45269912",
                "BrokerID_VehNum": "45269912_1",
                "Coverage_Vehicle": [
                    {
                        "in_coverage_vehiclecov_code": "EIPACustomEquipmentCov_Ext",
                        "BrokerID_VehNum": "45269912_1",
                        "DriftedCovTest1": "drift1",
                        "anotherList": [
                            {
                                "f1": 1,
                                "f2": 2
                            },
                            {
                                "f1": 3,
                                "f2": 4
                            }
                        ],
                        "in_vehicle_antilock": "Y"  # Moved to this level
                    },
                    {
                        "in_coverage_vehiclecov_code": "EIPACustomEquipmentCov_Ext",
                        "in_coverage_vehicleterm_code": "EIPAExcessCustomEquipmentDescription_Ext",
                        "in_coverage_vehicle_term_value": None,
                        "BrokerID_VehNum": "45269912_1",
                        "anotherList": [
                            {
                                "f1": 7,
                                "f2": 8
                            },
                            {
                                "f1": 9,
                                "f2": 10
                            }
                        ]
                    },
                    {
                        "in_coverage_vehicle_cov_code": "EIPAGlassCov_Ext",
                        "in_coverage_vehicle_term_code": "EIPAGlassDeductibl_Ext",
                        "in_coverage_vehicle_term_value": "0_0000",
                        "BrokerID_VehNum": "45269912_1"
                    }
                ]
            },
            {
                "drc_out_rating_vehicle_bi_calculation": "BASE_RATE:294 X BASE_RELATIVITY:0_877 X PLAN_AHEAD:0_88 X ILF_DED:1_83 X TIER:0_693 X ANTI_LOCK_BRAKES:0_95 X RAPA_SYMBOLS:0_813906 X HH_COMP:0_85 X CLASS:0_893 X NEW_CAR:0_97 X MULTI_POLICY:0_95 X SAFE_DRIVER:0_99 X PAYPLAN:0_95 = MODEL_PREM (no exp fees):146 X RSF:1_067 = TOTAL_PREMIUM:156",
                "drc_out_rating_vehicle_comp_calculation": "BASE_RATE:294 X BASE_RELATIVITY:0_913 X PLAN_AHEAD:0_88 X ILF_DED:0_71 X TIER:0_78 X GLASS:1_28 X ANTI_THEFT:0_85 X RAPA_SYMBOLS:1_42136757 X CLASS:1_088 X NEW_CAR:0_97 X MULTI_POLICY:0_95 X SAFE_DRIVER:0_99 X PAYPLAN:0_95 = MODEL_PREM (no exp fees):191 X RSF:1_067 = TOTAL_PREMIUM:204",
                "in_vehicle_antilock": "Y",
                "in_vehicle_garage_zip_code_dnu": "85254-5838",
                "BrokerID from left table": "45269912",
                "BrokerID_VehNum": "45269912_2",
                "Coverage_Vehicle": [
                    {
                        "in_coverage_vehicle_cov_code": "EIPACustomEquipmentCov_Ext",
                        "in_coverage_vehicle_term_code": "EIPAExcessCustomEquipmentBase_Ext",
                        "in_coverage_vehicle_term_value": "1500",
                        "BrokerID_VehNum": "45269912_2"
                    },
                    {
                        "in_coverage_vehicle_cov_code": "EIPACustomEquipmentCov_Ext",
                        "in_coverage_vehicle_term_code": "EIPAExcessCustomEquipmentAmount_Ext",
                        "in_coverage_vehicle_term_value": None,
                        "BrokerID_VehNum": "45269912_2"
                    }
                ]
            }
        ]
    }
}

# Create a list of dictionaries for CSV conversion
csv_data = []

for vehicle in data["Policy"]["Vehicle"]:
    vehicle_data = {
        "BrokerID": data["Policy"]["BrokerID"],
        "BrokerID_VehNum": vehicle["BrokerID_VehNum"],
        "drc_out_rating_vehicle_bi_calculation": vehicle["drc_out_rating_vehicle_bi_calculation"],
        "in_vehicle_antilock": vehicle.get("in_vehicle_antilock", ""),  # Handle missing key
        "in_vehicle_garage_zip_code_dnu": vehicle.get("in_vehicle_garage_zip_code_dnu", ""),  # Handle missing key
    }
    csv_data.append(vehicle_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(csv_data)

# Save the DataFrame to a CSV file
df.to_csv("vehicle_data.csv", index=False)
