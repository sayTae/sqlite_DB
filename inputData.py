import sqlite3
import os

print("\n" + "DB엔진 version: {0}"
      .format(sqlite3.sqlite_version), "\n")

## 변수 선언 ##
con, cur = None, None
data1, data2, data3, data4 = "","","",""
sql = ""

## 함수 ##
def show_Table_info(): 
    get_field(Table_Name)
    
    print('')
    print("||", field1, "||", field2, "||", field3, "||", field4,"                   table: <"+Table_Name+">")

    cur.execute(f"SELECT * FROM {Table_Name}")
    print("-------------------------------------------------------------------------------")
    
    for rows in cur.fetchall():
        for row in rows:
            print(row, end=" || ")
        print('')
    print("-------------------------------------------------------------------------------")
    
    
def SAVE_OR_NOT():
    while(True):
        res = input("\n" + "변경 사항이 맞습니까? (Y/N): ")
        print('')

        if res == "Y" or res == "y":
            con.commit()
            print(f"커밋 완료.")
            break;
    
        elif res == "N" or res == "n":
            print(f"저장하지 않음.", "\n")
            break;
 
        else:
            print("올바른 값을 입력해주세요.", "\n")
            continue;
    return 0;


def get_field(table_Name):
        global rr_dic;
        rr_dic = {}
        cnt = 0
        cur.execute(f"PRAGMA table_info({table_Name})")
        for rows in cur.fetchall():
            rr = str(rows).replace(", '', 0, None, 0)", '').replace("'", '').replace("(0, ", '').replace("(1, ", '').replace("(2, ", '').replace("(3, ", '')
            rs = rr.split(' ')
            rr_dic[cnt] = rs
            cnt +=1

        global field1; global field2; global field3; global field4;
        
        for i in range(1,5):
            globals()['field'+str(i)] = str(rr_dic[i-1][0]).replace(",", '')
        
        for i in range(1,5):
            globals()['field'+str(i)+'_type_noparsing'] = str(rr_dic[i-1][1])
            
            
        for i in range(1,5):
            if ('char' in globals()['field'+str(i)+'_type_noparsing']) or ('TEXT' in globals()['field'+str(i)+'_type_noparsing']):
                globals()['field'+str(i)+'_type'] = str
                globals()['field'+str(i)+'_type_name'] = 'str'
                
            elif ('int' in globals()['field'+str(i)+'_type_noparsing']) or ('INTEGER' in globals()['field'+str(i)+'_type_noparsing']):
                globals()['field'+str(i)+'_type'] = int
                globals()['field'+str(i)+'_type_name'] = 'int'
                

def add_row(table_Name):
    while (True):
        os.system('cls')
        show_Table_info()   # 업데이트 된 테이블 row 목록 보여주기
        
        print("추가할 내용을 입력하세요.", "(마침: 제품 코드란에 기입하지 않고 Enter)", "\n") # 인풋 받고,
        
        get_field(table_Name)

        while(True):
            data1 = input(f"{field1}({field1_type_name}) ==> ")
            data1_type = str(data1).isdigit()
            
            if data1 == '':
                input("입력이 완료되었습니다. (Enter)")
                return;
            
            if data1_type == True:
                data1_type = 'int'
            else:
                data1_type = 'str'

            if data1_type == field1_type_name:
                break;
            
            elif data1 == '':
                print("제품 입력이 완료되었습니다.", "\n")
                break;
            
            else: 
                print(f"입력: {data1_type} | 필드: {field1_type_name}")
                input("알맞은 형태의 값을 넣어주세요. (Enter)")
                continue
        
       # -------------------------------------------------------------     
        while(True):
            data2 = input(f"{field2}({field2_type_name}) ==> ")
            data2_type = str(data2).isdigit()
            
            if data2_type == True:
                data2_type = 'int'
            else:
                data2_type = 'str'

            if data2_type == field2_type_name:
                break;            
            else: 
                print(data2_type, field2_type_name)
                input("알맞은 형태의 값을 넣어주세요. (Enter)")
                continue
            
        while(True):
            data3 = input(f"{field3}({field3_type_name}) ==> ")
            data3_type = str(data3).isdigit()
            
            if data3_type == True:
                data3_type = 'int'
            else:
                data3_type = 'str'

            if data3_type == field3_type_name:
                break;            
            else: 
                print(data3_type, field3_type_name)
                input("알맞은 형태의 값을 넣어주세요. (Enter)")
                continue
            
        while(True):
            data4 = input(f"{field4}({field4_type_name}) ==> ")
            data4_type = str(data4).isdigit()
            
            if data4_type == True:
                data4_type = 'int'
            else:
                data4_type = 'str'

            if data4_type == field4_type_name:
                break;
            else: 
                print(f"입력: {data1_type}, 필드: {field4_type_name}")
                input("알맞은 형태의 값을 넣어주세요. (Enter)")
                continue
        # -------------------------------------------------------------
            
        try:
            sql = f"INSERT INTO {Table_Name} VALUES( \
                '"+ data1 +"', '"+ data2 +"', '"+ data3 +"', '"+ data4 +"')"
            cur.execute(sql)
        except:
            print("Error: 오류가 발생했습니다.")
            print(f"예상: {Table_Name} 존재하지 않을 가능성이 있습니다.")
            break;
    
def del_row(del_row_name):
    while(True):
        if del_row_name != '':
            del_select = f"DELETE FROM {Table_Name} WHERE {field1} = '"+ del_row_name +"' "
            cur.execute(del_select)
            os.system('cls')
            show_Table_info()  
            input(f"{del_row_name}: 삭제가 완료되었습니다! (Enter)")
            break;

        # elif del_Num == "all kill":
        #     cur.execute(f"DELETE FROM {Table_Name}")
        #     print("테이블 전체 삭제가 완료되었습니다.")
        #     break;
              
        else:
            input("Error: row 이름을 찾지 못하였습니다.. (Enter)")
        
def add_table(table_Name):
    
    make_field_dic = {}
    
    for n in range(4):
        os.system('cls')
        print("\n" + "  INTEGER-[1]  TEXT-[2]", "\n")
        field_name = input(f"{n+1}번째 필드 이름 ==> ")
        field_type = input(f"{n+1}번째 필드 type ==> ")
        print('')
  
        if field_type == '1':
            field_type = 'INTEGER'
        elif field_type == '2':
            field_type = 'TEXT'
        
        make_field_dic[n] = field_name +' '+ field_type
    
    for i in range(4):
        globals()['var' +str(i+1)] = make_field_dic[i]
    
    try:
        sql = f"CREATE TABLE {table_Name} ("+ var1 +", "+ var2 +", "+ var3 +", "+ var4 +")"
        cur.execute(sql)
        
        # dummy = "dummy"
        # sql = f"INSERT INTO {table_Name} VALUES( \
        #         '"+dummy+"','"+dummy+"','"+dummy+"','"+dummy+"')"
        # cur.execute(sql)
        
    except:
        print("Error: 오류가 발생했습니다.")

def del_table(table_Name):
    sql = f'DROP TABLE {table_Name}'
    con.execute(sql)
    
    # select data, typeof(data) from table_Name;


## 메인 코드 ##
while(True):
    DB_path = "C:/sqlite/DB_Name"
    print(f"({DB_path})")
    
    DB_Name = input("접근할 DB를 입력하세요: ")
    
    try:
        if (os.path.exists(DB_Name)):
            con = sqlite3.connect(f"C:/sqlite/{DB_Name}")
            cur = con.cursor()
            break;
        
        else:
            print("\n" +"존재하지 않는 DB입니다.")
            YESorNO = input("새로 생성 하시겠습니까? (Y/N): ")
            
            if YESorNO == 'Y' or YESorNO == 'y':
                con = sqlite3.connect(f"C:/sqlite/{DB_Name}")
                cur = con.cursor()
            else:
                input("다시 입력해주세요. (Enter)" + "\n")
                continue;
            
    except: 
        continue;

## 어쩔 수 없이 안에 만든 함수 ##
def show_Table_names(): # 테이블 목록 보여주는 함수
    cur.execute("SELECT tbl_name FROM sqlite_master")
    global r_dic
    r_dic = {}
    cnt = 0
    print('--------------------------------------------------')
    for r in cur.fetchall():
        cnt +=1
        r_ = str(r).replace('(', '').replace(',)', '').replace("'", '')
        print("||", r_)
        r_dic[cnt] = r_
    print('--------------------------------------------------')
    print('')

## 어쩔 수 없이 안에 만든 함수_2 ##
def show_Table_names_select():  # 테이블 목록 보여주는 함수 (+인덱싱)
    cur.execute("SELECT tbl_name FROM sqlite_master")
    global r_di
    r_dic = {}
    cnt = 0
    print('--------------------------------------------------')
    for r in cur.fetchall():
        cnt +=1
        r_ = str(r).replace('(', '').replace(',)', '').replace("'", '')
        print("||", r_, f'[{cnt}]')
        r_dic[cnt] = r_
    print('--------------------------------------------------')
    print("                                          뒤로 [0]", "\n")
    
while(True):    # 프로그램이 끝날 때까지 계속 반복
    os.system('cls')
    print("                    <작업 선택>", "\n")
    show_Table_names()  # 테이블 이름 보여주고,
    print("[1] table 추가/삭제" +' | '+ "[2] row 추가/삭제" +' | '+ "[0] 종료", "\n")   # 목록에서 선택 유도
    tesk = input("접근할 번호를 입력해주세요: ")    # 인풋 받고,

    ### table ###
    if tesk == '1': # 만약 1번 tesk라면,
        
        #  while(True):계속 반복
            os.system("cls")
            print("                 <Table 추가/삭제>", "\n")
            show_Table_names()  # 테이블 보여주기
            print("[1] table 추가" +' | '+ "[2] table 삭제" +' | '+ "[0] 이전으로", "\n")   # 목록에서 선택 유도
            tesk_Num = input("접근할 번호를 입력해주세요: ")    # 인풋 받기
            print('')
        
            ## table 추가 ##
            if tesk_Num == '1': # 1번 tesk에서 1번 작업이라면,
                while(True): # 계속 반복
                    os.system("cls")
                    print("                    <Table 추가>", "\n")
                    show_Table_names()
                    print("                                          뒤로 [0]", "\n")
                    print("|| Table 추가 시도중...", "\n")# 테이블 목록 보여주고
                    Name = input("추가할 테이블 이름을 입력하세요: ") # 테이블 이름 입력 받기
                    
                    if Name != '0':
                        try:
                            type = Name.isdigit()
                            type2 = list(Name)[0].isdigit()
                            
                            if (type == False) and (type2 == False):    
                                add_table(Name) # 테이블 만드는 함수
                                print("<Table 추가 완료!>")
                                show_Table_names()  # 업데이트 된 테이블 보여주기
                                print(f"table: [{Name}] 이 추가 되었습니다", "\n")  # 추가 된 테이블 이름 출력
                                
                            else:
                                input("테이블 이름을 문자열(str)로 입력해주세요. (Enter)")
                                continue;
                            
                        except:
                            print("테이블을 찾을 수 없습니다.", "\n")   # 오류 메시지
                    else:
                        break;
                    
            ## table 삭제 ##
            if tesk_Num == '2': # 1번 tesk에서 2번 작업이라면,
                while(True): # 계속 반복
                    os.system('cls')
                    print("                    <Table 삭제>", "\n")
                    show_Table_names_select()   # 테이블 목록 보여주고 (+인덱싱),
                    
                    Table_Num = int(input("삭제할 Table 번호를 입력하세요: "))  # 인풋 받기
                    
                    if Table_Num != 0:
                        try:
                            Table_Name = r_dic[Table_Num]   # 인풋을, 변수에 테이블 이름으로 저장
                        except:
                            input("다시 입력해주세요. (Enter)")
                            continue;
                            
                        while(True):
                            YESorNO = input(f"'{Table_Name}'을(를) 삭제 하시겠습니까? <Y/N>: ")
                            print('')
                                
                            if YESorNO == "Y" or YESorNO == 'y':  
                                try:
                                    del_table(Table_Name)   # 테이블 삭제하는 함수
                                    show_Table_names()  # 업데이트 된 테이블 이름을 보여줌
                                    input(f"table: [{Table_Name}] 이 삭제 되었습니다", "\n")  # 삭제 된 테이블 이름 출력
                                    break;
                                except:
                                    print("테이블을 찾을 수 없습니다.", "\n")   # 오류 메시지
                                    break;
                            
                            elif YESorNO == "N" or YESorNO == 'n':
                                input("삭제가 취소되었습니다. (Enter)")
                                break;
                            
                            else:
                                continue;
                                      
                    else:
                        break;
                              
                ## 예외 처리 ##
                if tesk_Num == '0':  # 만약 인풋이 0이라면,
                    break;  # 탈출
            else:
                continue;
        
    ### row ###
    elif tesk == '2': # 만약 2번 tesk라면,
        while(True):
            os.system('cls')
            print("                    <Table 선택>", "\n")
            show_Table_names_select()   # 테이블 목록 보여주기 (+인덱싱)
            Table_Num = int(input("접근할 Table 번호를 입력하세요: "))  # 인풋 받고,
            
            if Table_Num == 0:
                break;
            
            try:
                Table_Name = r_dic[Table_Num]   # 인풋을, 변수에 테이블 이름으로 저장
            except:
                input("다시 입력해주세요. (Enter)")
                continue;
                
            while(True): # 무한 반복
                os.system('cls')
                show_Table_info()   # 테이블 row 목록 보여주고,
                print("[1] row 추가" +' | '+ "[2] row 삭제" +' | '+ "[0] 이전으로", "\n")   # 목록에서 선택 유도
                tesk_Num = input("접근할 번호를 입력해주세요: ")    # 인풋 받고,
                print('')
                
                ## row 추가 ##
                if tesk_Num == '1': # 만약 인풋이 1이라면,
                    while(True):
                        try:
                            get_field(Table_Name)
                            add_row(Table_Name)   # row 추가 함수   
                              
                        except:
                            input("Error: 오류가 발생했습니다.")    # 오류 메시지
                        else:
                            break;

                ## row 삭제 ##
                elif tesk_Num == '2':   # 만약 인풋이 2라면,
                    while(True): # 무한 반복
                        os.system('cls')
                        print("                    <삭제할 row 선택>", "\n")
                        show_Table_info()
                        print("                                          뒤로 [0]", "\n")
                        get_field(Table_Name)
                        del_row_name = input(f"삭제할 [{field1}] 값을(를) 입력해주세요: ")
                        
                        if del_row_name != '0':
                            
                            while(True):
                                YESorNO = input(f"'{del_row_name}'을(를) 삭제 하시겠습니까? <Y/N>: ")
                                print('')
                                
                                if YESorNO == "Y" or YESorNO == 'y':
                                    try:
                                        del_row(del_row_name)   # row 삭제 함수
                                        break;
                                    except:
                                        print("Error: 오류가 발생했습니다.", "\n")  # 오류 메시지
                                        break;
                                    
                                elif YESorNO == "N" or YESorNO == 'n':
                                    input("삭제가 취소되었습니다. (Enter)")
                                    break;    
                                      
                                else:
                                    continue;
                                
                        else:
                            break;
                        
                ## 예외 처리 ##
                elif tesk_Num == '0': # 만약 인풋이 0이라면,
                    break; # 루프 종료
                
                else:
                    print("Warning: 작업할 인덱스를 다시 입력해주세요")
                    continue;
            
            ## 예외 처리 ##    
            if Table_Num == '0':
                break;
            else:
                print("Warning: 작업할 인덱스를 다시 입력해주세요")
    
    ### End ###
    elif tesk == '0': # 만약 3번 tesk라면,        
        SAVE_OR_NOT()   # 저장 할건지 말건지 함수
        
        print("모든 것을 마치고 종료합니다.")   # "모든 것을 마치고 종료한다" 알림
        con.close() # 종료함. 
        break;
        
    ### Re ###    
    else:
        input("Warning: 작업 인덱스를 다시 입력해주세요.")
        continue;