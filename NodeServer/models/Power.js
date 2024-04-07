const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const PowerSchema = new Schema(
  {
    temperature: {
      type: Number,
      required: true,
    },
    pressure: {
      type: Number,
      required: true,
    },
    windSpeed: {
      type: Number,
      required: true,
    },
    power: {
      type: Number,
      required: true,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Power", PowerSchema);
