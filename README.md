# Prac02 - Proyecto Dockerizado con Backend y Frontend

Este proyecto consiste en una aplicación simple con autenticación de usuarios y visualización de productos. Está compuesta por:

- Un backend en Node.js con conexión a MySQL.
- Un frontend estático servido por NGINX.
- Una base de datos MySQL con tabla de `clientes` y `productos`.

## Requisitos

- Docker
- Docker Compose

## Estructura del Proyecto

```
Prac02/
│
├── backend/             # Código del backend en Node.js
│   └── index.js
│
├── frontend/            # Archivos HTML estáticos
│   ├── index.html
│   └── productos.html
│
├── docker-compose.yml   # Orquestación de los servicios
└── README.md
```

## Pasos para levantar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/Prac02.git
cd Prac02
```

### 2. Construir los servicios

```bash
docker-compose build
```

### 3. Levantar los contenedores

```bash
docker-compose up -d
```

Esto levantará tres contenedores:

- `mysql_db`: base de datos MySQL con datos precargados.
- `backend_app`: servidor Node.js escuchando en el puerto 4000.
- `frontend_app`: servidor NGINX en el puerto 8080.

### 4. Verificar que está funcionando

- Abre tu navegador y visita: [http://localhost:8080](http://localhost:8080)

### 5. Acceder a la base de datos manualmente (opcional)

```bash
docker exec -it mysql_db mysql -u root -p123
```

## Notas

- El backend espera las credenciales del usuario en JSON para iniciar sesión (`/login`).
- Si el login es exitoso, se redirecciona automáticamente a la vista de productos (`productos.html`).

## Créditos

Desarrollado por [Tu Nombre].
