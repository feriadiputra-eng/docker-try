const express = require("express");
const app = express();
const PORT = 5000;

app.get("/", (req, res) => {
  res.send("kamu akhirnya bisa fer");
});

app.get("/rahasia", (req, res) => {
  res.send("boom awoakwoawkakw");
});

app.listen(5000, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});