const Power = require("../models/Power");

async function getPower(req, res) {
  try {
    const power = await Power.find({}).sort({ createdAt: -1 }).limit(5);

    res.status(200).json({
      msg: "Power got successfully",
      data: power,
    });
  } catch (error) {
    console.log(error);
  }
}

module.exports = getPower;
