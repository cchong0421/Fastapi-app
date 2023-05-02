# 待辦事項

[ ] 在家裡的 Mac Mini 的 Ubuntu 開發環境安裝 MongoDB, 並建立登入使用者 cchong0421

```mongo
// Select the database to use.
use("admin");

// Create a new role
db.adminCommand({
  createRole: "users",
  privileges: [
    {
      resource: { db: "CashflowDB", collection: "" },
      actions: ["find", "update", "insert", "remove"],
    },
  ],
  roles: [{ role: "read", db: "admin" }],
  writeConcern: { w: "majority", wtimeout: 5000 },
});

// Create a new user
db.createUser({
  user: "cchong0421",
  pwd: "sit",
  roles: ["users"],
});
```

[ ]
[ ]
[ ]