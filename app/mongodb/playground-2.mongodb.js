/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

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
