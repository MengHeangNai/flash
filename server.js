import dotenv from "dotenv";
import express from "express";
import brand_router from "./routes/brand/brand_route.js";
import cors from "cors";
import helmet from "helmet"; // Added for security headers
import morgan from "morgan"; // Added for HTTP request logging
import rateLimit from "express-rate-limit"; // Added for API rate limiting
import { router } from "./routes/index.js";

dotenv.config();

const PORT = process.env.PORT || 3000;
const app = express();

app.use(helmet());

app.use(express.json());
app.use(cors());

if (process.env.NODE_ENV === "development") {
  app.use(morgan("dev"));
} else {
  app.use(morgan("common"));
}

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per `windowMs`
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
  message: "Too many requests from this IP, please try again after 15 minutes.",
});
app.use("/api", apiLimiter);

// --- Routes ---
app.use("/api/v1", router);
app.use("/api/v1/brand", brand_router);

app.use((req, res) => {
  res.status(404).json({
    message: "Endpoint not found. Please check the API documentation.",
  });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    message: "Internal Server Error. Please try again later.",
  });
});

const server = app.listen(PORT, () => {
  console.log(
    `Server is running on http://localhost:${PORT} in ${
      process.env.NODE_ENV || "development"
    } mode.`
  );
  console.log(`API base path: http://localhost:${PORT}/api/v1`);
});

const gracefulShutdown = (signal) => {
  console.log(`\n${signal} received. Shutting down gracefully...`);
  server.close(() => {
    console.log("HTTP server closed.");
    process.exit(0);
  });

  setTimeout(() => {
    console.error(
      "Could not close connections in time, forcefully shutting down"
    );
    process.exit(1);
  }, 10000); // 10 seconds timeout
};

process.on("SIGINT", () => gracefulShutdown("SIGINT")); // Ctrl+C
process.on("SIGTERM", () => gracefulShutdown("SIGTERM")); // kill command
