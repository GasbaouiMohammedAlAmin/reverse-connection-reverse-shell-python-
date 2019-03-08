import sqlite3
conn=sqlite3.connect('db_config.db')
c = conn.cursor()
           
def create_data():
     with conn:
           c.execute("""CREATE TABLE if not exists configuration (
                           ip text,
                           port integer
                           )""")

def insert_data():
    with conn:
          c.execute("INSERT INTO configuration VALUES (:ip, :port)", {'ip': '192.168.1.1', 'port': 9999 })

def get_data():
          c.execute("SELECT * FROM configuration ")
          return c.fetchone()

def update_data(ip, port):
    with conn:
          c.execute("UPDATE configuration SET ip = :ip , port = :port",   {'ip': ip, 'port': port })
def get_count():
         r= c.execute("select count (*) from configuration ")
         r=c.fetchone()
         return r


create_data()

if (get_count( )[0]==0):
       insert_data()
      
print("\033[1;31m")
print("_____________________________________________")

print("|           GASA HACKING.....")
print("|____________________________________________")
print(""+"|**actual configuration**|")
print(''+"__________________________________________")

print("\033[1;32m")

print("|  LHOST  :"+str(get_data()[0])+" |  LPORT :"+str(get_data()[1])+" |")
print("_____________________________________________")

test=True 
while  test :
              print("_______________________________")
              print("")
              print("|  [1]: change  LHOST and LPORT")
              print("|  [2]: show configuration")
              print("|  [3]: quit configuration")
              print("|_______________________________")
              a=int (input("choose number : "))
              if a==1 :
                 b=str(input("set LHOST : "))
                 d= input("set LPORT : ")
                 update_data(b ,d)
              elif a==2 :         
                 print("lhost : "+str(get_data()[0]))
                 print("lport : "+str(get_data()[1]))
              elif a==3 :
                 test=False
conn.commit()
conn.close()

