// Setup with:
//   npm install express
//   npm install -g nodemon

// Run with:
//   nodemon app.js

// Load page with:
//   http://localhost:3000/autocomplete.html

var express = require('express');
var app = express();

app.use("/static", express.static("static"));

app.use(express.static("templates"));

app.get("/helloworld", function (req, res) {
    res.send("Hello World!");
});

app.get("/search", function (req, res) {
    var params = req.query;
    res.set({"Content-Type": "application/json"});
    res.json({"query": params.q, "results": [
        "result 1",
        "result 2"
    ]});
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log("Example app listening at http://%s:%s", host, port);
});
