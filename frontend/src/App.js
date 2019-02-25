// frontend/src/App.js

import React, { Component } from "react";
import EmissionChart from "./components/emission_chart";

class App extends Component {

  render() {
	return (
	  <main className="content">
		<h1 className="text-white text-uppercase text-center my-4">World emissions</h1>
		<div className="row ">
		  <div className="col-md-6 col-sm-10 mx-auto p-0">
			<div className="card p-3">
			  <div className="">
                <EmissionChart/>
			  </div>
			</div>
		  </div>
		</div>
	  </main>
	);
  }
}
export default App;
