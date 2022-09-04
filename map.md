# Map

General plan and details

---

## Description

### User/manager schemas

>MongoDB collection ["users"]
>user = {
>"_id": id
>"username": str,
>"email": str,
>"password": str,
>"varified": bool,
> }
---

>MongoDB collection ["managers"]
>manager = {
>"_id": id,
>"user_id": user_id,
> }
---

>MongoDB collection ["habits"]
>"user_id": _id,
>"title": str,
>"description": str,
>"tracker": [
>{
>"status": bool,
>"date": date,
>}
>]

### Tasks

- create JWT token
- User CRUD(registration, login, delete, update, get user info)
- email verification
- resend (code verification)
- refresh jwt
- logout
- password reset
- user/manager scopes
- get user list
