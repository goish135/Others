import sys
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
GDriveJSON = 'PythonUpload.json'
GSpreadSheet = 'https://docs.google.com/spreadsheets/d/1mhlkATF_YoVrV1ne-Z-qNgx2JCVOUpOn42bFjuxFpG4/edit'
WaitSecond = 5
print('將資料記錄在試算表' ,GSpreadSheet , '每' ,WaitSecond ,'秒')
print('按下 Ctrl-C中斷執行')
count = 1
while True:
	try:
		#scope = ['https://spreadsheets.google.com/feeds']
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
		#scope = ['https://docs.google.com/spreadsheets/']
		
		key = SAC.from_json_keyfile_name(GDriveJSON, scope)
		gc = gspread.authorize(key)
		worksheet = gc.open_by_url(GSpreadSheet).worksheet('工作表3')
	except Exception as ex:
		print('無法連線Google試算表', ex)
		sys.exit(1)
	worksheet.append_row([str(datetime.datetime.now()), count])
	count = count+1
	print('新增一列資料到試算表' ,GSpreadSheet)
	time.sleep(WaitSecond)
