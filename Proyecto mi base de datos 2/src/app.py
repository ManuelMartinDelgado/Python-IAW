from flask import Flask, render_template, request, redirect, url_for, session
import os
import database as db
import secrets

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)
app.secret_key = secrets.token_hex(16)

#Rutas de la aplicación
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('registro.html')


@app.route('/login', methods=['POST', 'GET'])
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
        
        return redirect(url_for('crud'))
    else:
        return render_template('login.html', message="Las credenciales no son correctas")   

#Cerrar sesión con el usuario conectado.
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    #Elimina todas las variables de sesión que estén generadas.
    session.clear()
    return render_template('login.html')

#Registrar un usuario en la base de datos.
@app.route('/registro', methods=['POST'])
def registro():
    nombre= request.form['nombre']
    apellido= request.form['apellido']
    email = request.form['email']
    contraseña = request.form['contraseña']
    confirmar = request.form['contraseña']

    if  nombre and apellido and email and contraseña and confirmar :
        cursor = db.database.cursor()
        sql = "INSERT INTO registro (nombre, apellido, email, contraseña, confirmar) VALUES (%s, %s, %s, %s, %s)"
        data = (nombre, apellido, email, contraseña, confirmar)
        cursor.execute(sql, data)
        db.database.commit()
    return render_template('login.html')

#Formulario
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



#Ruta para guardar datos de usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    try:
        nick = request.form['nick']
        coche = request.form['coche']
        elo = request.form['elo']
        partidos = int(request.form['partidos'])
        region = request.form['region']

        if  nick and coche and elo and partidos and region:
            cursor = db.database.cursor()
            sql = "INSERT INTO info (nick, coche, elo, partidos, region) VALUES (%s, %s, %s, %s, %s)"
            data = (nick, coche, elo, partidos, region)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('crud'))
    except ValueError:
        return render_template('index.html', message='Error: El valor de "partidos" debe ser numerico')
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
    
    nick = request.form['nick']
    coche = request.form['coche']
    elo = request.form['elo']
    partidos = request.form['partidos']
    region = request.form['region']

    if nick and coche and elo and partidos and region:
        cursor = db.database.cursor()
        sql = "UPDATE info SET nick = %s, coche = %s, elo = %s, partidos = %s, region = %s WHERE id = %s"
        data = (nick, coche, elo, partidos, region, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('crud'))


    
if __name__ == '__main__':
    app.run(debug=True, port=4000)