import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse

contact_list = {"nazar": 380501051478}

app = FastAPI()


@app.get("/contact")
def get_all():
    return contact_list


@app.get("/contact/{name}")
def get(name: str):
    return contact_list.get(name, "такого контакта не существует")


@app.post("/contact", status_code=status.HTTP_201_CREATED)
def add(name: str, number: int):
    if contact_list.get(name) != None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="такой контакт существует"
        )

    contact_list[name] = number


@app.delete("/contact/{name}")
def delete(name: str):
    return contact_list.pop(name)


@app.get("/")
def root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app)
