const express = require("express");
const router = express.Router();
const products = require("../data/products");

router.get("/health", (req, res) => {
  res.status(200).json({
    status: "ok",
    service: "product-service"
  });
});

router.get("/products", (req, res) => {
  res.status(200).json(products);
});

router.get("/products/:id", (req, res) => {
  const id = parseInt(req.params.id, 10);
  const product = products.find((p) => p.id === id);

  if (!product) {
    return res.status(404).json({
      message: "Product not found"
    });
  }

  res.status(200).json(product);
});

module.exports = router;