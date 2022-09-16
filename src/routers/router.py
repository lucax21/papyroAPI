from fastapi import APIRouter

from src.routers import login, user, genre, book, rate, comment, like, feed, notification, follow, user_book

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(genre.router, prefix="/genre", tags=["genres"])
router.include_router(book.router, prefix="/getBook", tags=["books"])
router.include_router(user_book.router, prefix="/userBook", tags=["userBook"])
router.include_router(rate.router, prefix="/rate", tags=["rates"])
router.include_router(comment.router, prefix="/comments", tags=["comments"])
router.include_router(like.router, prefix="/like", tags=["likes"])
router.include_router(feed.router, prefix="/feed", tags=["feed"])
router.include_router(notification.router, prefix="/notification", tags=["notification"])
router.include_router(follow.router, prefix="/follow", tags=["followers"])
