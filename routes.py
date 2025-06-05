from fastapi import APIRouter, HTTPException
from infrastructure.database import users_collection, posts_collection
from infrastructure.auth import get_password_hash, verify_password, create_access_token, get_current_user
from .models import UserCreate, UserLogin
from datetime import timedelta
from infrastructure.auth import decode_token, oauth2_scheme
from fastapi import APIRouter, HTTPException, Depends, Query
from bson.objectid import ObjectId

router = APIRouter(prefix="/users",tags=["users"])

@router.get("/profile")
def get_all_profiles(token: str = Depends(oauth2_scheme)):
    # Decode the JWT token
    user = decode_token(token)

    # Only allow admins
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admin can access this")

    # Get all users
    users_cursor = users_collection.find()
    users_data = []

    for db_user in users_cursor:
        username = db_user["username"]
        post_count = posts_collection.count_documents({"author": username})

        db_user["_id"] = str(db_user["_id"])
        db_user.pop("password", None)
        

        users_data.append({
            "user": db_user,
            "total_posts_uploaded": post_count
        })

    return {"users_profiles": users_data}



@router.get("/")
def get_users():
    users_cursor = users_collection.find()
    users = []
    for user in users_cursor:
        user["_id"]=str(user["_id"])
        user.pop("Password",None)
        users.append(user)
        return {"users":users}
    

@router.post("/signup")
def signup(user: UserCreate):
    if users_collection.find_one({"username":user.username,"email":user.email}):
        raise HTTPException(status_code=400,detail="Username or email already exists")
    hashed_pwd=get_password_hash(user.password)
    users_collection.insert_one({"username":user.username,"password":hashed_pwd,"role":user.role,"email":user.email})
    return{"messege":"User created successfully"}

@router.post("/login")
def login(user:UserLogin):
    db_user=users_collection.find_one({"username":user.username})
    if not db_user or not verify_password(user.password,db_user['password']):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    token = create_access_token({"sub":db_user["username"],"role":db_user["role"]}, timedelta(minutes=30))
    return {"access_token":token,"token_type":"bearer"}

@router.delete("/{user_id}")
def delete_user(user_id: str):
    try:
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User Deleted Successfully"}
    except:
        raise HTTPException(status_code=400, detail="Invalid user ID format")


