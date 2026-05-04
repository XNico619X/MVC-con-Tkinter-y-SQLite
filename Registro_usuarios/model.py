import sqlite3

class modeloUsuario:
    def __init__(self, db_name='usuarios.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                contraseña TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def agregar_usuario(self, nombre, email, contraseña):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO usuarios (nombre, email, contraseña) VALUES (?, ?, ?)',
                (nombre, email, contraseña)
            )
            self.conn.commit()
            return True, cursor.lastrowid          # retorna el ID asignado
        except sqlite3.IntegrityError:
            return False, "El email ya está registrado."
        except Exception as e:                     # captura errores inesperados
            return False, str(e)

    def obtener_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nombre, email FROM usuarios ORDER BY id DESC')
        return cursor.fetchall()

    def email_existe(self, email):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id FROM usuarios WHERE email = ?', (email,))
        return cursor.fetchone() is not None

    def cerrar_conexion(self):
        self.conn.close()