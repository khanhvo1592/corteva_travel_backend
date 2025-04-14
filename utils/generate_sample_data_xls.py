import xlwt
from faker import Faker

# Initialize Faker for Vietnamese locale
fake = Faker('vi_VN')

# Create a new workbook
wb = xlwt.Workbook()

# Function to write data to a sheet
def write_sheet(sheet, start_index, end_index):
    # Add headers
    sheet.write(0, 0, 'ma_so')
  
    # Generate records
    for i in range(start_index, end_index):
        row = i - start_index + 1  # Adjust row number for each sheet
        ma_so = f'{str(i+1).zfill(3)}'  # Generate ma_so like MS000001, MS000002, etc.
        

        sheet.write(row, 0, ma_so)
    

        # Print progress every 1000 records
        if i % 1000 == 0:
            print(f"Generated {i} records...")

# Calculate number of sheets needed (65535 rows per sheet, leaving room for header)
records_per_sheet = 65535
num_sheets = (500 + records_per_sheet - 1) // records_per_sheet

# Generate data across multiple sheets
for sheet_num in range(num_sheets):
    sheet_name = f'Sheet{sheet_num+1}'
    sheet = wb.add_sheet(sheet_name)
    
    start_index = sheet_num * records_per_sheet
    end_index = min((sheet_num + 1) * records_per_sheet, 500)
    
    write_sheet(sheet, start_index, end_index)

# Save the workbook
filename = 'sample_data_500.xls'
wb.save(filename)
print(f"File '{filename}' has been created with 500 records across {num_sheets} sheets.")