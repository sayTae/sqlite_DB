import sqlite3
import os

print("DB엔진 version: {0}"
      .format(sqlite3.sqlite_version), "\n")

## 변수 선언 ##
con, cur = None, None
data1, data2, data3, data4 = "","","",""
sql = ""

## 함수 ##
def show_Table_info():
    os.system("cls")
    cur.execute(f"SELECT * FROM {Table_Name}")
    print("pCode   pName    price   amount")
    print("--------------------------------")
    for rows in cur.fetchall():
        for row in rows:
            print(row, end=" || ")
        print('')
    print('')
    
    
def SAVE_OR_NOT():
    while(True):
        res = input("변경 사항이 맞습니까? (Y/N): ")
        print('')

        if res == "Y" or res == "y":
            con.commit()
            print(f"커밋 완료", "\n")
            con.close()
            break;
    
        elif res == "N" or res == "n":
            print(f"저장하지 않음", "\n")
            con.close()
            break;
 
        else:
            print("올바른 값을 입력해주세요.", "\n")
            continue;


def add_row():
    while (True):
        data1 = input("제품 코드 ==> ")
    
        if data1 == '':
            print("제품 입력이 완료되었습니다.", "\n")
            break;
    
        data2 = input("제품명 ==> ")
        data3 = input("가격 ==> ")
        data4 = input("제품 개수 ==> ")
        try:
            sql = f"INSERT INTO {Table_Name} VALUES( \
                '"+ data1 +"', '"+ data2 +"', '"+ data3 +"', '"+ data4 +"')"
            cur.execute(sql)
        except:
            print("Error: 오류가 발생했습니다.")
            print(f"예상: {Table_Name} 존재하지 않을 가능성이 있습니다.")
            break;
        
    show_Table_info()

    
def del_row(del_Num):
    while(True):
        print('')
        
        if del_Num != '':
            del_select = f"DELETE FROM {Table_Name} WHERE pCode = '"+ del_Num +"' "
            cur.execute(del_select)
            
            show_Table_info()  

        elif del_Num == "all kill":
            cur.execute(f"DELETE FROM {Table_Name}")
            print("테이블 전체 삭제가 완료되었습니다.")
            break;
              
        else:
            break;
        
def add_table(table_Name):
    os.system('cls')
    field_dic = {}
    print("NULL-[0]  INTEGER-[1]  TEXT-[2]  BLOB-[3]", "\n")
    for n in range(4):
        field_name = input(f"{n+1}번째 필드 이름 ==> ")
        field_type = input(f"{n+1}번째 필드 type ==> ")
        print('')
    
        if field_type == '0':
            field_type = 'NULL'
        elif field_type == '1':
            field_type = 'INTEGER'
        elif field_type == '2':
            field_type = 'TEXT'
        elif field_type == '3':
            field_type = 'BLOB'
        
        field_dic[n] = field_name +' '+ field_type
    
    var1 = field_dic[0]
    var2 = field_dic[1]
    var3 = field_dic[2]
    var4 = field_dic[3]
    
    try:
        sql = f"CREATE TABLE {table_Name}( \
            '"+ var1 +"', '"+ var2 +"', '"+ var3 +"', '"+ var4 +"')"
        cur.execute(sql)
    except:
        print("Error: 오류가 발생했습니다.")

def del_table(table_Name):
    sql = f'DROP TABLE {table_Name}'
    con.execute(sql)


## 메인 코드 ##
con = sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor()

def show_Table_names():
    os.system('cls')
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    global r_dic
    r_dic = {}
    cnt = 0
    for r in cur.fetchall():
        cnt +=1
        r_ = str(r).replace('(', '').replace(',)', '').replace("'", '')
        print("||", r_, f'[{cnt}]')
        r_dic[cnt] = r_
    print('')
    
show_Table_names()

print("[1] table 추가/삭제" +'  '+ "[2] row 추가/삭제")
tesk_num = input("접근할 번호를 입력해주세요: ")

if tesk_num == '1':
    show_Table_names()
    print("[1] table 추가" +'  '+ "[2] table 삭제")
    tesk_Num = input("접근할 번호를 입력해주세요: ")
    print('')
    
    if tesk_Num == '1':
        show_Table_names()
        Name = input("\n"+"추가할 테이블 이름을 입력하세요: ")
        add_table(Name)
        
        print(f"table: [{Name}] 이 추가 되었습니다", "\n")
        SAVE_OR_NOT()
    
    while(True):
        if tesk_Num == '2':
            show_Table_names()
            Table_Num = int(input("삭제할 Table 번호를 입력하세요: "))
            Table_Name = r_dic[Table_Num]
            try:
                del_table(Table_Name)
                SAVE_OR_NOT()
            except:
                print("테이블을 찾을 수 없습니다.", "\n")

if tesk_num == '2':
    show_Table_names()
    Table_Num = int(input("접근할 Table 번호를 입력하세요: "))
    Table_Name = r_dic[Table_Num]

    while(True):
        show_Table_info()
        print("[1] row 추가" +'  '+ "[2] row 삭제")
        tesk_Num = input("접근할 번호를 입력해주세요: ")
        print('')

        if tesk_Num == '1':
            show_Table_info()
            print("추가할 내용을 입력하세요.", "(마침: 제품 코드란에 기입하지 않고 Enter)", "\n")
            add_row()
            SAVE_OR_NOT()

        elif tesk_Num == '2':
            del_Num = input("삭제할 모델 번호를 입력해주세요: ")
            del_row(del_Num)
            SAVE_OR_NOT()