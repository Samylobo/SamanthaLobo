from multiprocessing import connection
import sqlite3
import sqlite3 cx = sqlite3.connect("test.db") # test.db will be created or opened
 
DATABASE_NAME = "database.db" 

def create_table():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor() 

    cursor.execute('''
                    CREATE TABLE ALUNO (
    ID INTEGER PRIMARY KEY,
    NOME TEXT,
    SEXO TEXT,
    IDADE INTEGER
);

INSERT INTO ALUNO (ID, NOME, SEXO, IDADE) VALUES (6, 'GENERATION', 'F', 10);

SELECT * FROM ALUNO;

UPDATE ALUNO SET NOME = 'GENERATION 2' WHERE ID = 6;

DELETE FROM ALUNO WHERE ID = 6;
                   
                   )
                   ''') 
    
    connection.commit()
    connection.close() 

    if __name__ == "__main__":
        create_table()