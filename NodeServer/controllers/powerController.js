const Power = require("../models/Power");

async function savePower(req, res) {
  try {
    const { formData, power } = req.body;
    console.log(formData, power);

    const newPower = new Power({
      temperature: parseFloat(formData.Air_temperature),
      pressure: parseFloat(formData.Pressure),
      windSpeed: parseFloat(formData.Wind_speed),
      power: power,
    });

    await newPower.save();

    res.status(201).json({
      msg: "Power saved successfully",
    });
  } catch (error) {
    console.log(error);
  }
}

module.exports = savePower;
