* устанавливаем fastapi(2)	pip install fastapi  pip install "uvicorn[standard]"
* декоратор для получения страницы по адресу, FastAPI	@app.get("/")
* особенность по функциям возвращающим страницы FastAPI	они асинхронные
* разворачиваем рут-страницу fastapi(4)	from fastapi import FastAPI  app = FastAPI()  @app.get("/")  async def root(): ...
* что возвращает функция для fastapi 	dict[str:str]
* запускаем сервер FastAPI 	uvicorn main:app --reload
* http-метод PUT; декоратор fastapi для него	пользуется для обновления данных на сервере; @app.put("/stuff/{id}")
* http-метод DELETE; декоратор fastapi для него	пользуется для удаления данных с сервера; @app.delete("/stuff/{id}")
* typing.Optional альтернативная запись; расшифровка	Optional[int] или int | None; для аргументов которые можно опустить
* модуль pydantic?	валидация типов согласно тайп хинтам!; приведение внешних данных к формату тайп хинта, где это возможно
* Curl: расшифровка, функционал	Client URL; передача данных с сервера и на сервер
* curl-аргументы( -X)	метод HTTP-запроса; curl -X 'POST'|'PUT' etc
* curl-аргументы( -d) 	содержимое пакета
* curl- тип содержимого json(-H)(2) curl -H 'accept: application/json' -H 'Content-Type: application/json'
* валидация curl-put запросов(поля)	все обязательные поля должны быть указаны
* конечная точка api 	url-адрес по которому клиент отправляет запрос на сервер(типа рендерится не страничка, а что-то типизированное!)
* создаём конечную точку api 	 это просто запрос @app.get("page") async def do_stuff(obj_id): return {"stuff":"on_obj"}
* передаём по ссылке аргументы для функции(повтор) 	localhost:8000/items/?arg_one=10&arg_two=0  async def read_args(arg_one:str=20,arg_two:str=40)
* импортируем типы ответов 	from fastapi.responses import {HTMLResponse} 
* возвращаем страничку через FastAPI, хардкод 	@app.get("/",response_class=HTMLResponse)  async_def read_root():  return <h1>Hi</h1>
* тип возврата JSON 	{JSONResponce}  from fastapi.responses import {}
* возвращаем json-ответ 	@app.get("/message")  async def do():  stuff={True:False}  return JSONResponse(content=stuff,status_code=200)
* импортируем модуль для темплейтов 	from fastapi.templating import Jinja2Templates  templates = Jinja2Templates(directory="path") @app.get("/rend",response_class=HTMLResponse) async def rnd():  return templates.TemplateResponse("page.html",{"data":for_template})
* адрес основной автоматической документации swagger 	"/docs"
* адрес альтернативной документации ReDoc 	/redoc
* импортируем модуль для автодокументации 	from fastapi.openapi.utils import get_openapi
* указываем http-путь до файла документации 	app= FastAPI(openapi_url="/path/to/openapi.json")
* генерируем документацию 	def forge_docs():  if app.openapi_schema: return app.openapi_schema    openapi_schema = get_openapi(title='#',version="#",description='#',routes=app.routes)  app.openapi_schema= openapi_schema  return app.openapi_schema    app.openapi=forge_docs
* запускаем генерацию документации для перехода по /redoc или /docs 	переходим по адресу указанному в app= FastAPI(openapi_url="#")
