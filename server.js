import express from "express";
import brand_router from "./routes/brand/brand_route.js";
import cors from "cors";
import { router } from "./routes/index.js";

const PORT = process.env.PORT || 3000;
const app = express();

app.use(express.json());
app.use(cors());

app.use("/api/v1", router);
app.use("/api/v1/brand", brand_router);

app.use((req, res) => {
  res.status(404).json({
    message: "Endpoint not found. Please check the API documentation.",
  });
});

// log ddos attacks
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    message: "Internal Server Error. Please try again later.",
  });
});

// default url is http://localhost:3000/api/v1
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}/api/v1`);
});
