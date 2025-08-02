const express = require("express");
const app = express();
const PORT = 5000;

app.get("/", (req, res) => {
  res.send("Hello from Node.js + Docker! tolonggggg");
});

app.get("/rahasia", (req, res) => {
  res.send("boom awoakwoawkakw");
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
