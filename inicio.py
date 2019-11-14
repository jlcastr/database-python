from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
import mysql.connector as mysql
import mysql.connector

#conección
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''


mysql = MySQL(app)

# sesion
app.secret_key = 'mysecretkey'

@app.route('/')
def menu():
    cur = mysql.connection.cursor()
    cur.execute("SHOW DATABASES")

    database = cur.fetchall()


    print(database)

    return render_template('menuprueba.html', dataall = database)


@app.route('/stablas')
def staclas ():
    app.config['MYSQL_DB'] = 'escuela'
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    cur.close()
    for table in tables:
        print(table)
    return render_template('selectable.html', tableallesc = tables)

@app.route('/agencia')
def agencia():
    app.config['MYSQL_DB'] = 'agencia'
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    cur.close()
    for table in tables:
        print(table)
    return render_template('prueba.html', tableallage = tables)

@app.route('/menu')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumnos2')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', alumnos = data)

#agencia
@app.route('/menuagencia')
def indexagencia():
    app.config['MYSQL_DB'] = 'agencia'
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM autos2')
    data = cur.fetchall()
    print(data)
    return render_template('menuagencia.html', autos=data)


@app.route('/add', methods = ['POST'])
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

#addautos
@app.route('/addauto', methods = ['POST'])
def addauto():
    if request.method == 'POST':
        fullmarca = request.form['fullmarca']
        fullmodel = request.form['fullmodel']
        year = request.form['year']
        fullcolor = request.form['fullcolor']
        carrera = request.form['fulltrans']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO autos2 (marca, modelo, Año, color, transmision) VALUES (%s, %s, %s, %s, %s)',
                    (fullmarca, fullmodel, year, fullcolor, carrera))
        mysql.connection.commit()
        flash('Registro agregado')
        return redirect(url_for('indexagencia'))
#editar alumnos
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumnos2 WHERE id = %s', (id))
    dataedit = cur.fetchall()
    cur.close()
    print(dataedit[0])
    return render_template('editarR.html', editR = dataedit[0])

    #fetchall obtener todos los datos

#editar autos
@app.route('/editautos/<id>', methods = ['POST', 'GET'])
def editautos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM autos2 WHERE id = %s', (id))
    dataedit2 = cur.fetchall()
    cur.close()
    print(dataedit2[0])
    return render_template('editarautos.html', editarautos = dataedit2[0])

#actualizar autos
@app.route('/updateautos/<id>', methods = ['POST'])
def updateautos(id):
    if request.method == 'POST':
        fullmarca = request.form['fullmarca']
        fullmodelo = request.form['fullmodelo']
        year = request.form['year']
        fullcolor = request.form['fullcolor']
        fulltrans = request.form['fulltrans']
        curup = mysql.connection.cursor()
        curup.execute("""
        UPDATE autos2
        SET marca = %s,
            modelo = %s,
            Año = %s,
            color = %s,
            transmision = %s
        WHERE id = %s
        """, (fullmarca, fullmodelo, year, fullcolor, fulltrans, id))
        flash('Registro actualizado')
        mysql.connection.commit()
        return redirect(url_for('indexagencia'))


#actualizar alumnos
@app.route('/update/<id>', methods = ['POST'])
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

#elimiar alumnos
@app.route('/delete/<string:id>')
def delete(id):
    cur2 = mysql.connection.cursor()
    cur2.execute('DELETE FROM alumnos2 WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('Index'))

#eliminar autos
@app.route('/deleteauto/<string:id>')
def deleteautos(id):
    cur2 = mysql.connection.cursor()
    cur2.execute('DELETE FROM autos2 WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('indexagencia'))

@app.route('/constable')
def consultable():
    cursor = consultable.cursor()
    cursor.execute("escuela")
    cursor.execute("SHOW TABLES")
    tables=cursor.fetchall()
    print(tables)




if __name__ == '__main__':
    app.run(port = 3001, debug= True)