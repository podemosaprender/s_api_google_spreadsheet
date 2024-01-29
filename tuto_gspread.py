import gspread

gc = gspread.service_account('.svcacc.json')

SAMPLE_URL="https://docs.google.com/spreadsheets/d/1kOlZVgdqa5U2fjxjqb85tqMTVSdcO58CjLJp9cYFx3s/edit?usp=sharing"
SAMPLE_FOLDER_URL="https://drive.google.com/drive/folders/1WGUUWVlWk8LyuVBQ0vcOei2lhfwLmOeu"

sht2 = gc.open_by_url(SAMPLE_URL);
ws1 = sht2.get_worksheet(0)
rows = ws1.get_all_values()
print(f"ALL VALUES {rows}")

ws1.update([[10, 20], [30, 40]])

sht3= gc.create("xborrame", folder_id= SAMPLE_FOLDER_URL.split('/')[-1])
ws1 = sht2.get_worksheet(0)
ws1.update([[11, 21], [31, 41]])



