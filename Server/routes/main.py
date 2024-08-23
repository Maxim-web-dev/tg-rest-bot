from fastapi import FastAPI
from schemas import Order
import uvicorn

def main():
    app = FastAPI()   

    @app.post('/order')
    def create_order(order: Order) -> dict:
        return order

if __name__ == '__main__':
    uvicorn.run(app = main(), reload = True)