import express from "express";
import { result } from "../sql/index.js";
export const router = express.Router();

router.get("/", async (req, res) => {
  const data = (await result()).rows;
  res.json(data);
});
