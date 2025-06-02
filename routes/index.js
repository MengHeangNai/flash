import express from "express";
import { result } from "../sql/index.js";
export const router = express.Router();

router.get("/", async (req, res, next) => {
  // Added next parameter
  try {
    const queryResult = await result(); // Assuming result() returns a promise
    const data = queryResult.rows;
    res.json(data);
  } catch (error) {
    next(error); // Pass errors to the centralized error handler
  }
});
