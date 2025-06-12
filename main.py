<<<<<<< HEAD
from fastapi import FastAPI, Depends, Query
=======
from fastapi import FastAPI, Depends, HTTPException, Query
>>>>>>> cf8039a313634c9477b480605ffd3a7376d3ce4d
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Game, Provider
from database import get_db
<<<<<<< HEAD
from typing import Optional, List
=======
from typing import Optional
>>>>>>> cf8039a313634c9477b480605ffd3a7376d3ce4d
from pydantic import BaseModel

app = FastAPI()

<<<<<<< HEAD
class SearchResult(BaseModel):
    games: List[int] = []
    providers: List[int] = []
=======

class SearchResult(BaseModel):
    games: list[int] = []
    providers: list[int] = []

>>>>>>> cf8039a313634c9477b480605ffd3a7376d3ce4d

@app.get("/search/", response_model=SearchResult)
async def search(
        query: Optional[str] = Query(None, min_length=2, max_length=100),
        db: AsyncSession = Depends(get_db)
):
    result = SearchResult()

    if query:
<<<<<<< HEAD
        
        games_stmt = select(Game.id).where(Game.title.ilike(f"%{query}%"))
        games_result = await db.execute(games_stmt)
        result.games = [row[0] for row in games_result.fetchall()]

        
        providers_stmt = select(Provider.id).where(Provider.name.ilike(f"%{query}%"))
        providers_result = await db.execute(providers_stmt)
        result.providers = [row[0] for row in providers_result.fetchall()]
=======
        # Поиск игр
        games_stmt = select(Game.id).where(Game.title.ilike(f"%{query}%"))
        games_result = await db.execute(games_stmt)
        result.games = [row[0] for row in games_result]

        # Поиск провайдеров
        providers_stmt = select(Provider.id).where(Provider.name.ilike(f"%{query}%"))
        providers_result = await db.execute(providers_stmt)
        result.providers = [row[0] for row in providers_result]
>>>>>>> cf8039a313634c9477b480605ffd3a7376d3ce4d

    return result