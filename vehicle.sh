# To view premium amount
# awk -F',' '$1 == "Vehicle No" {header = $0} $1 == "1265" {print $7}' vehicles.csv

# To delete a specific row.
vehicleNo="3148"  # Replace with the specific vehicle number you want to delete
awk -F',' -v vehicleno="$vehicleNo" '$1 == "Vehicle No" || $1 != vehicleno' vehicles_copy.csv > temp.csv && mv temp.csv vehicles_copy.csv
