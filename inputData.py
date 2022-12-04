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
    cur.execute(f"SELECT sql FROM sqlite_master WHERE tbl_name='{Table_Name}' ")
    
    for r in cur.fetchall():
        r_ = str(r).replace(Table_Name, f'{Table_Name} ').replace('("CREATE TABLE ', '').replace('",)', '').replace(", ", ' || ').replace("             ", '')
        print(r_)

    cur.execute(f"SELECT * FROM {Table_Name}")
    print("-------------------------------------------------------------------------------")
    
    for rows in cur.fetchall():
        for row in rows:
            print(row, end=" || ")
        print('')
    print('')
    
    
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

def add_row():
    while (True):
        os.system('cls')
        show_Table_info()   # 업데이트 된 테이블 row 목록 보여주기
        
        print("추가할 내용을 입력하세요.", "(마침: 제품 코드란에 기입하지 않고 Enter)", "\n") # 인풋 받고,
        
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
        
        # show_Table_info()
        
        # while(True):
        #     ismore = input("더 추가하시겠습니까? <Y/N>: ")
            
        #     if ismore == 'Y' or ismore == 'y':
        #         break;
            
        #     elif ismore == 'N' or ismore == 'n':
        #         end = True;
                
        #     else:
        #         print("선택을 바르게 입력해주세요.")
        #         continue;
    
def del_row(res):
    while(True):
        if res != '':
            del_select = f"DELETE FROM {Table_Name} WHERE pCode = '"+ res +"' "
            cur.execute(del_select)
            os.system('cls')
            show_Table_info()  
            input(f"{del_Num}: 삭제가 완료되었습니다! (Enter)")
            break;

        # elif del_Num == "all kill":
        #     cur.execute(f"DELETE FROM {Table_Name}")
        #     print("테이블 전체 삭제가 완료되었습니다.")
        #     break;
              
        else:
            input("Error: row 이름을 찾지 못하였습니다.. (Enter)")
        
def add_table(table_Name):
    
    field_dic = {}
    
    for n in range(4):
        os.system('cls')
        print("type =>  NULL-[0]  INTEGER-[1]  TEXT-[2]  BLOB-[3]", "\n")
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
    if tesk == '1': # 만약 1번 테스크라면,
        
        while(True): # 계속 반복
            os.system("cls")
            print("                 <Table 추가/삭제>", "\n")
            show_Table_names()  # 테이블 보여주기
            print("[1] table 추가" +' | '+ "[2] table 삭제" +' | '+ "[0] 이전으로", "\n")   # 목록에서 선택 유도
            tesk_Num = input("접근할 번호를 입력해주세요: ")    # 인풋 받기
            print('')
        
            ## table 추가 ##
            if tesk_Num == '1': # 1번 테스크에서 1번 작업이라면,
                while(True): # 계속 반복
                    os.system("cls")
                    print("                    <Table 추가>", "\n")
                    show_Table_names()
                    print("                                          뒤로 [0]", "\n")
                    print("|| Table 추가 시도중...", "\n")# 테이블 목록 보여주고
                    Name = input("추가할 테이블 이름을 입력하세요: ") # 테이블 이름 입력 받기
                    
                    if Name != '0':
                        try:
                            add_table(Name) # 테이블 만드는 함수
                            print("<Table 추가 완료!>")
                            show_Table_names()  # 업데이트 된 테이블 보여주기
                            print(f"table: [{Name}] 이 추가 되었습니다", "\n")  # 추가 된 테이블 이름 출력
                        except:
                            print("테이블을 찾을 수 없습니다.", "\n")   # 오류 메시지
                    else:
                        break;
                    
            ## table 삭제 ##
            if tesk_Num == '2': # 1번 테스크에서 2번 작업이라면,
                while(True): # 계속 반복
                    os.system('cls')
                    print("                    <Table 삭제>)", "\n")
                    show_Table_names_select()   # 테이블 목록 보여주고 (+인덱싱),
                    
                    Table_Num = int(input("삭제할 Table 번호를 입력하세요: "))  # 인풋 받기
                    
                    if Table_Num != 0:
                        Table_Name = r_dic[Table_Num]   # 인풋을, 변수에 테이블 이름으로 저장
                    
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
    elif tesk == '2': # 만약 2번 테스크라면,
        while(True):
            os.system('cls')
            print("                    <Table 선택>", "\n")
            show_Table_names_select()   # 테이블 목록 보여주기 (+인덱싱)
            Table_Num = int(input("접근할 Table 번호를 입력하세요: "))  # 인풋 받고,
            
            if Table_Num == 0:
                break;
            
            Table_Name = r_dic[Table_Num]   # 인풋을, 변수에 테이블 이름으로 저장
                
            while(True): # 무한 반복
                os.system('cls')
                show_Table_info()   # 테이블 row 목록 보여주고,
                print("[1] row 추가" +' | '+ "[2] row 삭제" +' | '+ "[0] 이전으로", "\n")   # 목록에서 선택 유도
                tesk_Num = input("접근할 번호를 입력해주세요: ")    # 인풋 받고,
                print('')
                
                ## row 추가 ##
                if tesk_Num == '1': # 만약 인풋이 1이라면,
                    try:
                        add_row()   # row 추가 함수     
                    except:
                        print("Error: 오류가 발생했습니다.")    # 오류 메시지
                    else:
                        break;

                ## row 삭제 ##
                elif tesk_Num == '2':   # 만약 인풋이 2라면,
                    while(True): # 무한 반복
                        os.system('cls')
                        print("                    <row 번호 선택>)", "\n")
                        show_Table_info()
                        print("                                          뒤로 [0]", "\n")
                        del_Num = input("삭제할 모델 번호를 입력해주세요: ")
                        
                        if del_Num != '0':
                            
                            while(True):
                                YESorNO = input(f"'{del_Num}'을(를) 삭제 하시겠습니까? <Y/N>: ")
                                print('')
                                
                                if YESorNO == "Y" or YESorNO == 'y':
                                    try:
                                        del_row(del_Num)   # row 삭제 함수
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
                continue;
    
    ### End ###
    elif tesk == '0': # 만약 3번 테스크라면,
        SAVE_OR_NOT()   # 저장 할건지 말건지 함수
        
        print("모든 것을 마치고 종료합니다.")   # "모든 것을 마치고 종료한다" 알림
        con.close() # 종료함. 
        break;
        
    ### Re ###    
    else:
        input("Warning: 작업 인덱스를 다시 입력해주세요.")
        continue;