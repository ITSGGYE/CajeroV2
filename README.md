<h1>Cajero Automático Ver.2</h1>

La versión 2 del cajero automático, corre sobre un raspberry pi b2 y pasó de Java a Python 2.7.
Se utiliza la librería TKinter muy ligera y dinámica para el aspecto gráfico.

<br/>

**Requisitos:**

Librería TKinter 8.6 para Ubuntu

`sudo apt-get install python python-tk`

Instalar el conector para MySQL

`sudo pip install mysql-connector` 

Instalar el conector para PostgreSQL

`sudo pip install psycopg`

Instalar el sensor de teclado

`sudo pip install keyboard`

Instalar SSHtunnel

`sudo apt install libffi-dev` --Requisito para Raspberry<br/>
`sudo pip install sshtunnel`

Instalar Pdfkit


Habilitar el acceso a root al GUI para este proyecto

`xhost +`

Ver más acerca de xhost

`http://aprendiendognulinux.blogspot.com/2010/10/solucion-al-problema-gtk-warning-cannot.html`

Ejecución

`sudo python main.py`