# e-commerce_project
e-commerce with user creation, authentication, SQL DB, and checkout


Para poder ejecutar el backend realizar los siguientes pasos:

1-  instalar python3  mediante los siguientes comandos en funcion del SO que se este utilizando:

        Windows
            Descargar version 3.13 de -->> https://www.python.org/downloads/release/python-3132/ e instalar
            
            Utilizando PowerShell ir a la carpeta del proyecto que se clono del repositorio: e-commerce_project/ 

            Una vez dentro de la carpeta /e-commerce_project/ ejecutar el siguietne comando:

                py -3 -m venv .venv

            Esto permite la creacion del entorno de trabajo (enviroment).
            Luego de creado hay que activarlo para lo que se debe ejecutar el siguiente comando:

                .venv\Scripts\activate

            Realizar esto cada vez que se vuelve a trabajar en el proyecto y el ambiente no este activo o se haya estado trabajando
            en otro proyecto que tenga su propio ambiente.

            Una vez se haya activado el ambiente, se debe instalar Flask, para esto, ejecutar el siguiente comando:

                pip install Flask

            Una vez instalado, para correr el backend, ejecutar el siguiente comando:

                flask run

            Esto mostrará en el terminal/power shell, la direccion ip en la que se está corriendo el proyecto en el entorno de 
            desarrollo. También se puede correr el backend en mode debug (permite actualziar el proyecto cada que se realice 
            un cambio en el mismo utilizando solo la tecla F5.) Además del refresh, el modo debug  muestra un traceback que permite
            identificar el origen de los error que se produzcan. Para correr flask en modo debug realizar lo siguiente.
            Colocar las siguientes lineas de código luego de haber inicializado la app en app.py:

            app.debug = True

            if __name__ == "__main__":
            app.run(debug=True)

            Una vez agregadas ejecutar:

                FLASK_ENV = "development"
                flask run

        MACOS
            Descargar version 3.13 de -->> https://www.python.org/downloads/release/python-3132/ e instalar
            
            Utilizando Terminal ir a la carpeta del proyecto que se clono del repositorio: e-commerce_project/ 

            Una vez dentro de la carpeta /e-commerce_project/ ejecutar el siguietne comando:

                python3 -m venv .venv

            Esto permite la creacion del entorno de trabajo (enviroment).
            Luego de creado hay que activarlo para lo que se debe ejecutar el siguiente comando:

                .venv/bin/activate

            Realizar esto cada vez que se vuelve a trabajar en el proyecto y el ambiente no este activo o se haya estado trabajando
            en otro proyecto que tenga su propio ambiente.

            Una vez se haya activado el ambiente, se debe instalar Flask, para esto, ejecutar el siguiente comando:

                pip install Flask

            Una vez instalado, para correr el backend, ejecutar el siguiente comando:

                flask run

            Esto mostrará en el terminal/power shell, la direccion ip en la que se está corriendo el proyecto en el entorno de 
            desarrollo. También se puede correr el backend en mode debug (permite actualziar el proyecto cada que se realice 
            un cambio en el mismo utilizando solo la tecla F5.) Además del refresh, el modo debug  muestra un traceback que permite
            identificar el origen de los error que se produzcan. Para correr flask en modo debug realizar lo siguiente.
                        Colocar las siguientes lineas de código luego de haber inicializado la app en app.py:

            app.debug = True

            if __name__ == "__main__":
            app.run(debug=True)

            Una vez agregadas ejecutar:
            

                export FLASK_ENV=development
                flask run
