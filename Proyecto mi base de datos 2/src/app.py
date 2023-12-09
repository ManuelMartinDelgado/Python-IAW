from flask import Flask, render_template, request, redirect, url_for, session
import os
import database as db
import secrets

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)
app.secret_key = secrets.token_hex(16)

#Rutas de la aplicación
@app.route('/', methods=['GET'])
def home():
    return render_template('registro.html')


@app.route('/login', methods=['POST'])
def login():
    email=request.form['email']
    contraseña=request.form['contraseña']
    cur=db.database.cursor()
    cur.execute('SELECT * FROM registro WHERE email= %s AND contraseña = %s', (email,contraseña))
    user= cur.fetchone()
    cur.close()
    
    if user is not None:
        session['email'] = email
        session['contraseña'] = contraseña
        session['nombre']= user[1]
        session ['apellido']= user[2] 
        
        return redirect('crud')
    else:
        return render_template('login.html', message="Las credenciales no son correctas")   

#Cerrar sesión con el usuario conectado.
@app.route('/logout', methods=['GET'])
def logout():
    #Elimina todas las variables de sesión que estén generadas.
    session.clear()
    return redirect(url_for('home'))

#Registrar un usuario en la base de datos.
@app.route('/registro', methods=['POST'])
def registro():
    nombre= request.form['nombre']
    apellido= request.form['apellido']
    email = request.form['email']
    contraseña = request.form['contraseña']
    confirmar = request.form['confirmar']

    if  nombre and apellido and email and contraseña and confirmar :
        cursor = db.database.cursor()
        sql = "INSERT INTO registro (nombre, apellido, email, contraseña, confirmar) VALUES (%s,%s,%s, %s, %s)"
        data = (nombre, apellido, email, contraseña, confirmar)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('crud'))


@app.route('/crud', methods=['GET'])
def crud():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM info")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)



#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    coche = request.form['coche']
    rango = request.form['rango']

    if  nombre and usuario and coche and rango :
        cursor = db.database.cursor()
        sql = "INSERT INTO info (nombre,usuario, coche, rango) VALUES (%s, %s, %s, %s)"
        data = (nombre, usuario, coche, rango)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('crud'))

#Borrar los usuarios
@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM info WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('crud'))

#Editar los datos del formulario
@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    coche = request.form['coche']
    rango = request.form['rango']

    if nombre and usuario and coche and rango:
        cursor = db.database.cursor()
        sql = "UPDATE info SET nombre = %s, usuario = %s, coche = %s, rango = %s WHERE id = %s"
        data = (nombre, usuario, coche, rango, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('crud'))


    
if __name__ == '__main__':
    app.run(debug=True, port=4000)