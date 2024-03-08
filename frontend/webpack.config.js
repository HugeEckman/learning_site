const path = require('path');

module.exports = {
  entry: "./src/index.js",
  mode: 'development',
  output: {
    path: path.resolve(__dirname, "../static/frontend/"),
    filename: 'index.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};