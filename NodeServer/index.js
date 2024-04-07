const express = require("express");
const app = express();
const cors = require("cors");
const mongoose = require("mongoose");

const powerRouter = require("./routes/powerRoutes");

mongoose
  .connect(
    "mongodb+srv://billify0:Billify0@cluster0.2nowzwf.mongodb.net/hackwave?retryWrites=true&w=majority&appName=Cluster0"
  )
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.log(err);
  });

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.use("/api/power", powerRouter);

app.listen(8004, () => {
  console.log("Listening on port 8004");
});
