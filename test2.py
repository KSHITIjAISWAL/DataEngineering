import json
import csv


json_file_path = 'sample.json'

# Open the JSON file in read mode
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)


# Extract 'Vehicle' data into separate CSV files
for index, vehicle in enumerate(data['Policy']['Vehicle']):
    # Create a separate CSV file for each vehicle
    csv_filename = f'vehicle_{index + 1}.csv'

    # Extract data from the vehicle dictionary
    drc_out_rating_vehicle_bi_calculation = vehicle['drc_out_rating_vehicle_bi_calculation']
    broker_id_veh_num = vehicle['BrokerID_VehNum']

    # Create a CSV file and write the data
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header
        csv_writer.writerow(['drc_out_rating_vehicle_bi_calculation', 'BrokerID_VehNum'])

        # Write vehicle data
        csv_writer.writerow([drc_out_rating_vehicle_bi_calculation, broker_id_veh_num])

print("CSV files created successfully.")

