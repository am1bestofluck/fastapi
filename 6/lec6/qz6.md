# https://gbcdn.mrgcdn.ru/uploads/asset/5295277/attachment/ad87c5fc88b6d10a61949c16e80a5db5.pdf
в pydantic создаём связь между классами 	в тайп-хинте указываем другой класс  class Item(BaseModel):  name:str    class Order(BaseModel): items: List[Item]
* импортируем валидацию полей pydantic 	from pydantic import Field
* валидация строки name, класса User не длиннее 10 символов 	class User(BaseModel):  name:str = Field(max_length=10)
* параметры Field: по умолчанию, больше чем, меньше или равно 	Field(default=0 gt=-1, le=1)
* параметры Field: оглавление документации, текст документации 	Field(title="",description="")
* где смотреть список актуальных параметров Field 	документация FastAPI
* если объект из ответа не соответствует модели то? бросается исключение
* устанавливаем драйвер базы данных, все вместе 	pip install databases
* устанавливаем один конкретный драйвер(aiosqlite) 	pip install databases[aiosqlite]
* декоратор "в случае события" 	@app.on_event("event")
* аргументы @app.on_event(): запуск сервера; завершение работы 	@app._on_event("startup"); @app.on_event("shutdown")
* подключаемся/отключаемся к рабочей базе 	@app.on_event("startup")  async def startup():  await database.connect() #disconnect()
* metadata 	информация о другой информации; раскрывает признаки и связи таблиц базы данных
* connection pool 	абстракция, управляющая и оптимизирующая  подключение к базе
* dialect 	взаимодействие бд и api
* engine 	объединяет connection pool и диалект
* подключаем базу данных(5) 	DB_URL="sqlite:///path_to.db"  db = databases.Database(DB_URL)  mtdt = sqlalchemy.MetaData()  engine = sqlalchemy.create_engine(DB_URL)  mtdt.create_all(engine)
* Операции CRUD 	 create read update delete
* разрешаем sqlite обрабатывать разные запросы в одном потоке 	engine = create_engine(DB_URL, connect_args = {"check_same_thread":False})
* синтаксис выполнения запроса 	await db.execute(query)
* синтаксис добавления в базу 	query=table_name.create().values(arg1="1",arg2=2)  await db.execute(query)
* указываем тип возврата для @app.{get}() 	 response_model=List[int]
* получаем из таблицы table все записи 	@app.get("/all/")  asynce def get_all():  query = table.select()  return await database.fetch_all(query)
* query и запрос результата на получение одного item из таблицы table по inc_id  query= table.select().where(table.c.id == inc_id) return await db.fetch_one(query)
* что нужно для update 	признак записи к изменению, новый контент
* запрос на изменение/удаление строки 	query = table.{update()/delete()}.where(table.c.id == inc_id).values(\*\*new_row.dict())
* как тестируем CRUD- операции 	через curl  или swagger ui(/docs/)
* импорт валидации на уровне http-пути	from fastapi import Path
* fastapi.Path, что делает	валидация параметров переданных адресом /body/for/fastapi+path
* где применяется fastapi.Path 	это дефолтный аргумент функций-ответов на маршруты    @app.get("/items/{item_id}")  async def show_item( item_id:int=Path())
* fastapi.Path параметр- обязательный аргумент 	int_arg:int = Path(...)
* fastapi.Path параметр - название для автодокументации 	Path(title="name for /docs")
* fastapi.Query что делает	валидация опциональных параметров /path?query=0&param=1
* проверка строки arg через Query, по умолчанию None, не короче 5 знаков) 	async def get_query(arg:str=Query(None, min_length = 5)): return arg
* общее между fastapi.Path, fastapi.Query, pydantic.Field 	они находятся в одной иерархии классов, являясь подклассами pydantic.Param > pydantic.FieldInfo
