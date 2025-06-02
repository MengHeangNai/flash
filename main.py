from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
import uvicorn

# --- Data Model (using Pydantic for validation and serialization) ---
class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price: int
    color: str
    condition: int = Field(..., ge=0, le=5) # Example: condition rating 0-5
    sold: bool

# --- In-memory "database" for demonstration ---
# In a real application, this would connect to a database like PostgreSQL, MySQL, etc.
cars_db: List[Car] = [
    Car(id=0, brand="Ford", model="Mustang", year=1965, price=45000, color="white", condition=4, sold=False),
    Car(id=1, brand="Chevrolet", model="Camaro", year=1970, price=48000, color="red", condition=2, sold=False),
    Car(id=2, brand="Dodge", model="Charger", year=1969, price=58000, color="black", condition=4, sold=True),
    Car(id=3, brand="Porsche", model="911", year=1985, price=85000, color="silver", condition=5, sold=False),
    Car(id=4, brand="Jaguar", model="E-Type", year=1967, price=56000, color="green", condition=2, sold=True),
    # Add more car data as needed, similar to your sql/index.js
]

app = FastAPI(
    title="Advanced Car API",
    description="An example of an advanced API server using FastAPI for managing car data.",
    version="1.0.0"
)

# --- API Endpoints ---

@app.get("/api/v1/cars", response_model=List[Car], summary="Get a list of cars")
async def get_cars(
    brand: Optional[str] = Query(None, description="Filter by car brand"),
    model: Optional[str] = Query(None, description="Filter by car model"),
    year: Optional[int] = Query(None, description="Filter by car year"),
    search: Optional[str] = Query(None, description="Search term for brand, model, or color"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
    take: int = Query(10, ge=1, le=100, description="Limit for pagination"),
    order_by: Optional[str] = Query("id", description="Field to order by (e.g., 'price', 'year')"),
    order: Literal["ASC", "DESC"] = Query("ASC", description="Order direction: ASC or DESC")
):
    """
    Retrieve a list of cars with optional filtering, searching, sorting, and pagination.
    """
    filtered_cars = cars_db

    if brand:
        filtered_cars = [car for car in filtered_cars if car.brand.lower() == brand.lower()]
    if model:
        filtered_cars = [car for car in filtered_cars if car.model.lower() == model.lower()]
    if year:
        filtered_cars = [car for car in filtered_cars if car.year == year]

    if search:
        search_term = search.lower()
        filtered_cars = [
            car for car in filtered_cars if
            search_term in car.brand.lower() or
            search_term in car.model.lower() or
            search_term in car.color.lower() or
            search_term in str(car.year)
        ]

    # Sorting
    if hasattr(Car, order_by): # Check if order_by is a valid field
        try:
            filtered_cars.sort(key=lambda car: getattr(car, order_by), reverse=(order == "DESC"))
        except AttributeError:
            # Handle cases where order_by might not be a directly sortable attribute or needs special handling
            pass # Or raise HTTPException for invalid order_by field

    # Pagination
    paginated_cars = filtered_cars[offset : offset + take]
    return paginated_cars

@app.get("/api/v1/cars/{car_id}", response_model=Car, summary="Get a specific car by ID")
async def get_car_by_id(car_id: int):
    """
    Retrieve a specific car by its unique ID.
    """
    try:
        return next(car for car in cars_db if car.id == car_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Car not found")

# --- How to run this server ---
# 1. Save this code as main.py (e.g., in a new directory like `advanced_python_server`).
# 2. Install FastAPI and Uvicorn: pip install fastapi "uvicorn[standard]"
# 3. Run the server: uvicorn main:app --reload
#
# You can then access the API at http://127.0.0.1:8000/api/v1/cars
# And the interactive API documentation at http://127.0.0.1:8000/docs

if __name__ == "__main__":
    # This part is for direct execution, e.g., for simple testing or if not using Uvicorn CLI
    # For production, Uvicorn is recommended as the ASGI server.
    uvicorn.run(app, host="0.0.0.0", port=8000)