def insert(dbCon, dbCursor, fname, lname, rate, hours, paid):

    balance = int(paid) - (int(rate)*int(hours))
    # if balance > 0:
    #     balance = "+" + balance

    dbCursor.execute("INSERT INTO clients(client_fname, client_lname, client_rate, total_hours, amount_paid, balance) VALUES (?,?,?,?,?,?)",(fname,lname,rate,hours,paid,str(balance)))
    dbCon.commit()


def read_table(dbCursor, table):
    dbCursor.execute('SELECT * FROM {}'.format(table))
    records = dbCursor.fetchall()
    return records    

    












