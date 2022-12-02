import sqlite3
print("DB엔진 version: {0}"
      .format(sqlite3.sqlite_version), "\n")

## 함수 ##
def confirm():
    print("")
    cur.execute(f"SELECT * FROM {Table_Name}")
    print("pCode   pName    price   amount")
    print("--------------------------------")
    for rows in cur.fetchall():
        for row in rows:
            print(row, end=" || ")
        print("")
    print("")

## 변수 선언 ##
con, cur = None, None
data1, data2, data3, data4 = "","","",""
sql = ""

## 메인 코드 ##
con = sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

r_dic = {}
cnt = 0
for r in cur.fetchall():
    cnt +=1
    r_ = str(r).replace('(', '').replace(',)', '').replace("'", '')
    print("||", r_, f'[{cnt}]')
    r_dic[cnt] = r_
print("")

Table_Num = int(input("접근할 Table 번호를 입력하세요: "))
Table_Name = r_dic[Table_Num]

confirm()

print("추가할 부분을 입력하세요.", "(마침: 제품 코드란에 기입하지 않고 Enter)")

while (True):
    data1 = input("제품 코드 ==> ")
    
    if data1 == "":
        print("제품 입력이 완료되었습니다.", "\n")
        break;
    
    elif data1 == "del all":
        cur.execute(f"DELETE FROM {Table_Name}")
        print("테이블 전체 삭제가 완료되었습니다.")
        continue;
    
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
        
confirm()

while(True):
    res = input("변경 사항이 맞습니까? (Y/N): ")

    if res == "Y" or res == "y":
        con.commit()
        print(f"[{Table_Name}]: 커밋 완료", "\n")
        con.close()
        break;
    
    elif res == "N" or res == "n":
        print(f"[{Table_Name}]: 저장하지 않음", "\n")
        con.close()
        break;
 
    else:
        print("올바른 값을 입력해주세요.", "\n")
        continue;
    
    
