import { result } from "../../sql/index.js";

export const post_brand = async (req, res) => {
  const brand = req.body.brand; // e.g., body with { "brand": "Ford" }
  const data = (await result({ brand })).rows;
  res.json(data);
};

// use query params // api?brand=Ford
// export const get_brand = async (req, res) => {
//   const brand = req.query.brand;
//   const data = (await result({ brand })).rows;
//   res.json(data);
// };

export const get_brand = async (req, res) => {
  const { brand, model, year, search, offset, take } = req.query;
  const data = (await result({ brand, model, year, search, offset, take }))
    .rows;

  res.json(data);
};
