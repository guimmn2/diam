import './App.css';
import React, { Fragment } from "react"; //(7)
import Header from "./components/Header";
import Home from "./components/Home";

function App() {
  return (
    <Fragment>
      <Header />
      <Home />
    </Fragment>
  );
}

export default App;
