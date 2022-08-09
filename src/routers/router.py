from fastapi import APIRouter

from src.routers import login, user, genre, book, rate, comment, message, like, feed

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(genre.router, prefix="/genre", tags=["genres"])
router.include_router(book.router, prefix="/getBook", tags=["books"])
router.include_router(rate.router, prefix="/avaliacoes", tags=["avaliacoes"])
router.include_router(comment.router, prefix="/comments", tags=["comments"])
router.include_router(message.router, prefix="/mensagens", tags=["mensagens"])
router.include_router(like.router, prefix="/like", tags=["likes"])
router.include_router(feed.router, prefix="/feed", tags=["feed"])
