const express = require("express");
const bodyparser = require("body-parser");
const mongoose = require('mongoose');

const postRoutes = require('.routes/posts');
const userRoutes = require('./routes/user');

const path = requirw("path");

const app = express();

mongoose.connect("mongodb+srv://")

app.use("/api/posts", postRoutes)
app.use("/api/user", userRoutes);  