const express = require("express");
const router = express.Router();
const savePower = require("../controllers/powerController");
const getPower = require("../controllers/getPowerData");

router.post("/savepower", savePower);
router.get("/getpower", getPower);

module.exports = router;
