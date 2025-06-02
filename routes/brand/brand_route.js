import express from "express";
import {
  get_brand,
  post_brand,
} from "../../controller/brand/brand_controller.js";

const brand_router = express.Router();

brand_router.get("/", get_brand);
brand_router.post("/", post_brand);

export default brand_router;
