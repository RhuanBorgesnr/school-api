
# API controle de presença

sistema para controle de presença dos
alunos de uma aula.

### Clonando repositorio:
```sh
git clone https://github.com/RhuanBorgesnr/school-api.git
cd escola
```
### Instalar depedencias:
```sh
pip install -r requirements.txt

```
### Iniciando aplicação:
```sh
python manage.py migrate
python manage.py runserver
```
### Acessando:

- Link para acessar a pagina web:  http://127.0.0.1:8000/
- Aqui você tera acesso a documentação da api: http://127.0.0.1:8000/api/doc/#operation/alunos_create
- Acesso API: http://127.0.0.1:8000/api/alunos/

### PUT e DELETE:
http://127.0.0.1:8000/api/alunos/{id}
