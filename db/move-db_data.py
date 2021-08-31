import pymysql
import sys
sys.path.insert(0, 'C:/Users/BLUE/Desktop/hjh/data')
import connection_info as myInfo

def checkInsert(table):
    try:
        sql = "select count(*) from {0}".format(table)
        
        cursor_receive.execute(sql)
        cursor.execute(sql)

        if cursor_receive.fetchone()[0] == cursor.fetchone()[0]:
            return False
        else :
            return True
        
    except Exception as e:
        print("'{0}'테이블 select함수 예외 발생 - {1}".format(table, e))
        return False

def insert(table):
    try:
        cursor_receive.execute("TRUNCATE {0}".format(table))
        cursor.execute("select * from {0}".format(table))
        result = cursor.fetchall();
        
        values = "%s"
        for i in range(1, len(result[0])):
            values += ", %s"
            
        insert_sql = "insert into `{0}` values ({1})".format(table, values)
        cursor_receive.executemany(insert_sql, result)
        
        conn_receive.commit()
        print("'{0}'테이블 insert성공".format(table))
        
        if table == "tb_user_m":
            cursor_receive.execute("update {0} set password = NULL".format(table))
            conn_receive.commit()
        
    except Exception as e:
        print("'{0}'테이블 insert함수 예외 발생 - \n {1}".format(table, e))




# Open database connection
# ,autocommit=True
conn_receive = pymysql.connect(
    host=myInfo.sos['host'],
    user=myInfo.sos['user'], 
    passwd=myInfo.sos['passwd'], 
    db=myInfo.sos['db'],
    charset=myInfo.sos['charset']
)
conn = pymysql.connect(
    host=myInfo.eobuba['host'],
    user=myInfo.eobuba['user'],
    passwd=myInfo.eobuba['passwd'], 
    db=myInfo.eobuba['db'],
    charset=myInfo.eobuba['charset']
)
 
# prepare a cursor object using cursor() method
cursor_receive = conn_receive.cursor()
cursor = conn.cursor()

# 테이블명 리스트
arrTable = [
    'tb_album_m',
    'tb_apply_m',
    'tb_area_m',
    'tb_attendance_book_m',
    'tb_attendance_house',
    'tb_auth_m',
    'tb_beacon_m',
    'tb_car_m',
    'tb_car_station',
    'tb_car_station_d',
    'tb_confirm_d',
    'tb_cost_setting_type',
    'tb_diary_file',
    'tb_dtg_push_log',
    'tb_educational_plan_m',
    'tb_eobuba_question',
    'tb_face_kids_img_tb',
    'tb_fcm',
    'tb_get_off_log_down',
    'tb_get_off_log_up',
    'tb_get_on_log_down',
    'tb_get_on_log_up',
    'tb_home_request_m',
    'tb_kids_d',
    'tb_kids_diary',
    'tb_kids_station_d',
    'tb_kindergarden_class_d',
    'tb_kindergarden_cost_setting',
    'tb_kindergarden_cost_write',
    'tb_kindergarden_cost_write_detail',
    'tb_kindergarden_m',
    'tb_medication_request_m',
    'tb_menu_management_m',
    'tb_news_m',
    'tb_nfc_m',
    'tb_nfc_speak_m',
    'tb_not_ride',
    'tb_notice_m',
    'tb_read_board_yn_d',
    'tb_reply_alrambook_m',
    'tb_reply_m',
    'tb_schedule_management_m',
    'tb_survey_m',
    'tb_survey_vote_d',
    'tb_survey_vote_item_d',
    'tb_take_bus_m',
    'tb_title_d',
    'tb_user_card',
    'tb_user_m',
    'tb_user_statistics_tb',
    'tb_version_m'
]

for table in arrTable:
# 테이블 행 수가 다를시 insert
# 테이블 데이터 삭제 후 insert할 시 checkInsert 미실행
    if checkInsert(table):
        insert(table)

 
# disconnect from server
conn_receive.close()
conn.close()