import sqlite3




class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("""
                         create table if not exists Contacts
                         (id integer primary key,fname text, lname text, address text, phone text)
                         """)
    def insert(self,fname,lname,address,phone):
        self.cur.execute("""
                         insert into Contacts values(NULL,?,?,?,?)
                         """,(fname,lname,address,phone))
        self.con.commit()
    def fetch(self):
        self.cur.execute('select * from Contacts order by id desc')
        rows = self.cur.fetchall()
        return rows
    def remove(self,id):
        self.cur.execute('delete from Contacts where id = ?',(id,))
        self.con.commit()
    def update(self,id,fname,lname,address,phone,):
        self.cur.execute("""
                         update Contacts set address=?, phone=? where id =?
                         """,(address,phone,id))
        self.con.commit()
    def search(self,id):
        self.cur.execute('select * from Contacts where id =? order by id desc' ,(id))
        rows = self.cur.fetchall()
        return rows
        
        # self.cur.execute("select * from Contacts where mix like % ? % ",(input_))
        # # self.cur.execute("""
        # #                  select *from Contacts where fname =? or lname = ? or  address =? or phone = ?
        # #                  """,(input_,input_,input_,input_))
        # return self.cur.fetchall()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    