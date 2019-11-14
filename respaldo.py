from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import mysql.connector as mysql
import mysql.connector

# conección
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'escuela'
mysql = MySQL(app)

# sesion
app.secret_key = 'mysecretkey'


@app.route('/menu')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumnos2')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', alumnos=data)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        fullname = request.form['fullname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        carrera = request.form['carrera']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO alumnos2 (nombre, apellidos, correo, telefono, carrera) VALUES (%s, %s, %s, %s, %s)',
                    (fullname, lastname, email, phone, carrera))
        mysql.connection.commit()
        flash('Registro agregado')
        return redirect(url_for('Index'))


@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumnos2 WHERE id = %s', (id))
    dataedit = cur.fetchall()
    cur.close()
    print(dataedit[0])
    return render_template('editarR.html', editR=dataedit[0])

    # fetchall obtener todos los datos


@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        nombre = request.form['fullname']
        apellidos = request.form['lastname']
        correo = request.form['email']
        telefono = request.form['phone']
        carrera = request.form['carrera']
        curup = mysql.connection.cursor()
        curup.execute("""
        UPDATE alumnos2
        SET nombre = %s,
            apellidos = %s,
            correo = %s,
            telefono = %s,
            carrera = %s
        WHERE id = %s
        """, (nombre, apellidos, correo, telefono, carrera, id))
        flash('Registro actualizado')
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete(id):
    cur2 = mysql.connection.cursor()
    cur2.execute('DELETE FROM alumnos2 WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('Index'))


@app.route('/constable')
def consultable():
    cursor = consultable.cursor()
    cursor.execute("escuela")
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(tables)


if __name__ == '__main__':
    app.run(port=3001, debug=True)