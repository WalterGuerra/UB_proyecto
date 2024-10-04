from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import router as user_router
from routes.perfil_routes import router as perfil_router
from routes.herramienta_routes import router as herramienta_router 
from routes.camiones_routes import router as camiones_router 
from routes.atributo_routes import router as atributo_router
from routes.atributoxusuario_routes import router as atributoxusuario_router

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(perfil_router)
app.include_router(herramienta_router)
app.include_router(camiones_router)
app.include_router(atributo_router)
app.include_router(atributoxusuario_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)